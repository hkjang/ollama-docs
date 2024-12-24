# 템플릿

Ollama는 Go의 내장 템플릿 엔진을 기반으로 한 강력한 템플릿 엔진을 제공하여 대형 언어 모델을 위한 프롬프트를 구성할 수 있습니다. 이 기능은 모델의 잠재력을 최대한 활용하는 데 유용한 도구입니다.

## 기본 템플릿 구조

기본 Go 템플릿은 세 가지 주요 부분으로 구성됩니다:

* **레이아웃**: 템플릿의 전체 구조입니다.
* **변수들**: 템플릿이 렌더링될 때 실제 값으로 대체될 동적인 데이터의 자리 표시자입니다.
* **함수들**: 템플릿의 내용을 조작하는 데 사용할 수 있는 사용자 정의 함수 또는 논리입니다.

다음은 간단한 채팅 템플릿의 예입니다:

```gotmpl
{{- range .Messages }}
{{ .Role }}: {{ .Content }}
{{- end }}
```

이 예에서는 다음과 같은 요소가 있습니다:

* 기본 메시지 구조(레이아웃)
* 세 가지 변수: `Messages`, `Role`, `Content` (변수들)
* 배열의 항목을 반복하며 각 항목을 표시하는 사용자 정의 함수 (`range .Messages`)

## 모델에 템플릿 추가하기

기본적으로 Ollama에 가져온 모델은 `{{ .Prompt }}`라는 기본 템플릿을 가지고 있어 사용자의 입력이 그대로 LLM에 전송됩니다. 이는 텍스트 또는 코드 완성 모델에는 적합하지만 채팅 또는 지시 모델에는 필수적인 마커가 부족합니다.

이러한 모델에서 템플릿을 생략하면 사용자가 입력을 올바르게 템플릿화해야 하는 책임을 지게 됩니다. 템플릿을 추가하면 사용자가 모델에서 최상의 결과를 쉽게 얻을 수 있습니다.

모델에 템플릿을 추가하려면 Modelfile에 `TEMPLATE` 명령을 추가해야 합니다. 다음은 메타의 Llama 3을 사용하는 예입니다.

```dockerfile
FROM llama3.2

TEMPLATE """{{- if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>
{{- end }}
{{- range .Messages }}<|start_header_id|>{{ .Role }}<|end_header_id|>

{{ .Content }}<|eot_id|>
{{- end }}<|start_header_id|>assistant<|end_header_id|>

"""
```

## 변수들

`System` (문자열): 시스템 프롬프트

`Prompt` (문자열): 사용자 프롬프트

`Response` (문자열): 어시스턴트 응답

`Suffix` (문자열): 어시스턴트 응답 뒤에 삽입되는 텍스트

`Messages` (목록): 메시지 목록

`Messages[].Role` (문자열): 역할로, `system`, `user`, `assistant`, 또는 `tool` 중 하나일 수 있습니다.

`Messages[].Content` (문자열): 메시지 내용

`Messages[].ToolCalls` (목록): 모델이 호출하고자 하는 도구 목록

`Messages[].ToolCalls[].Function` (객체): 호출할 함수

`Messages[].ToolCalls[].Function.Name` (문자열): 함수 이름

`Messages[].ToolCalls[].Function.Arguments` (맵): 인자 이름과 인자 값의 매핑

`Tools` (목록): 모델이 접근할 수 있는 도구 목록

`Tools[].Type` (문자열): 스키마 유형. `type`은 항상 `function`입니다.

`Tools[].Function` (객체): 함수 정의

`Tools[].Function.Name` (문자열): 함수 이름

`Tools[].Function.Description` (문자열): 함수 설명

`Tools[].Function.Parameters` (객체): 함수 매개변수

`Tools[].Function.Parameters.Type` (문자열): 스키마 유형. `type`은 항상 `object`입니다.

`Tools[].Function.Parameters.Required` (목록): 필수 속성 목록

`Tools[].Function.Parameters.Properties` (맵): 속성 이름과 속성 정의의 매핑

`Tools[].Function.Parameters.Properties[].Type` (문자열): 속성 유형

`Tools[].Function.Parameters.Properties[].Description` (문자열): 속성 설명

`Tools[].Function.Parameters.Properties[].Enum` (목록): 유효한 값 목록

## 팁 및 모범 사례

Go 템플릿 작업 시 다음 팁과 모범 사례를 염두에 두세요:

* **점(.)에 유의하세요**: `range` 및 `with`와 같은 제어 흐름 구조는 컨텍스트 `.`을 변경합니다.
* **범위 밖 변수**: 현재 범위에 없는 변수를 참조하려면 `$.`를 사용하여 루트에서 시작합니다.
* **공백 제어**: 선행(`{{-`) 및 후행(`-}}`) 공백을 제거하려면 `-`를 사용합니다.

## 예시

### 예시 메시지

#### ChatML

ChatML은 인기 있는 템플릿 형식입니다. Databrick의 DBRX, Intel의 Neural Chat 및 Microsoft의 Orca 2와 같은 모델에 사용할 수 있습니다.

```gotmpl
{{- range .Messages }}<|im_start|>{{ .Role }}
{{ .Content }}<|im_end|>
{{ end }}<|im_start|>assistant
```

### 예시 도구

도구 지원은 템플릿에 `{{ .Tools }}` 노드를 추가하여 모델에 추가할 수 있습니다. 이 기능은 외부 도구를 호출하도록 훈련된 모델에 유용하며 실시간 데이터를 검색하거나 복잡한 작업을 수행하는 데 강력한 도구가 될 수 있습니다.

#### Mistral

Mistral v0.3 및 Mixtral 8x22B는 도구 호출을 지원합니다.

```gotmpl
{{- range $index, $_ := .Messages }}
{{- if eq .Role "user" }}
{{- if and (le (len (slice $.Messages $index)) 2) $.Tools }}[AVAILABLE_TOOLS] {{ json $.Tools }}[/AVAILABLE_TOOLS]
{{- end }}[INST] {{ if and (eq (len (slice $.Messages $index)) 1) $.System }}{{ $.System }}

{{ end }}{{ .Content }}[/INST]
{{- else if eq .Role "assistant" }}
{{- if .Content }} {{ .Content }}</s>
{{- else if .ToolCalls }}[TOOL_CALLS] [
{{- range .ToolCalls }}{"name": "{{ .Function.Name }}", "arguments": {{ json .Function.Arguments }}}
{{- end }}]</s>
{{- end }}
{{- else if eq .Role "tool" }}[TOOL_RESULTS] {"content": {{ .Content }}}[/TOOL_RESULTS]
{{- end }}
{{- end }}
```

### 예시 중간 채우기

중간 채우기 지원은 템플릿에 `{{ .Suffix }}` 노드를 추가하여 모델에 추가할 수 있습니다. 이 기능은 사용자 입력 중간에 텍스트를 생성하도록 훈련된 모델, 예를 들어 코드 완성 모델에 유용합니다.

#### CodeLlama

CodeLlama [7B](https://ollama.com/library/codellama:7b-code) 및 [13B](https://ollama.com/library/codellama:13b-code) 코드 완성 모델은 중간 채우기를 지원합니다.

```gotmpl
<PRE> {{ .Prompt }} <SUF>{{ .Suffix }} <MID>
```

> [!NOTE]
> CodeLlama 34B 및 70B 코드 완성 모델과 모든 지시 및 Python 미세 조정된 모델은 중간 채우기를 지원하지 않습니다.

#### Codestral

Codestral [22B](https://ollama.com/library/codestral:22b)는 중간 채우기를 지원합니다.

```gotmpl
[SUFFIX]{{ .Suffix }}[PREFIX] {{ .Prompt }}
```