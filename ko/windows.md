<Free Translation>

# Ollama Windows

Ollama for Windows에 오신 것을 환영합니다.

이제 더 이상 WSL이 필요 없습니다!

Ollama는 이제 NVIDIA 및 AMD Radeon GPU 지원을 포함하여 네이티브 Windows 애플리케이션으로 실행됩니다. Ollama for Windows를 설치한 후에는 Ollama가 백그라운드에서 실행되며, `{ollama}` 명령줄은 `cmd`, `파워셸` 또는 선호하는 터미널 애플리케이션에서 사용할 수 있습니다. 기존과 같이 Ollama [API](./api.md)는 `http://localhost:11434`에서 제공됩니다.

## 시스템 요구사항

* Windows 10 22H2 이상, Home 또는 Pro
* NVIDIA 카드가 있는 경우 NVIDIA 452.39 이상 드라이버
* Radeon 카드가 있는 경우 [AMD Radeon 드라이버](https://www.amd.com/en/support)

Ollama는 진행 상황 표시를 위해 유니코드 문자를 사용하며, 일부 오래된 Windows 10 터미널 글꼴에서는 알 수 없는 사각형으로 표시될 수 있습니다. 이 경우 터미널 글꼴 설정을 변경해 보세요.

## 파일 시스템 요구사항

Ollama 설치는 관리자 권한이 필요 없으며 기본적으로 홈 디렉터리에 설치됩니다. 이진 파일 설치를 위해 최소 4GB의 공간이 필요합니다. Ollama를 설치한 후에는 대형 언어 모델을 저장하기 위한 추가 공간이 필요하며, 이 모델들은 수십에서 수백 GB의 크기를 가질 수 있습니다. 홈 디렉터리에 충분한 공간이 없으면 이진 파일이 설치되는 위치와 모델이 저장되는 위치를 변경할 수 있습니다.

### 설치 위치 변경

Ollama 애플리케이션을 홈 디렉터리와 다른 위치에 설치하려면 다음 플래그와 함께 설치 프로그램을 시작하세요:

```powershell
OllamaSetup.exe /DIR="d:\some\location"
```

### 모델 위치 변경

Ollama가 다운로드한 모델을 홈 디렉터리 대신 다른 위치에 저장하도록 변경하려면 사용자 계정에서 환경 변수 `OLLAMA_MODELS`를 설정하세요.

1. 설정(Windows 11) 또는 제어판(Windows 10) 애플리케이션을 시작하고 _환경 변수_를 검색합니다.
2. _계정에 대한 환경 변수 편집_을 클릭합니다.
3. 모델을 저장할 위치에 대한 `OLLAMA_MODELS` 변수를 수정하거나 새 변수를 만듭니다.
4. 확인 또는 적용을 클릭하여 저장합니다.

Ollama가 이미 실행 중인 경우, 트레이 애플리케이션을 종료하고 시작 메뉴에서 다시 실행하거나, 환경 변수를 저장한 후 새로 시작한 터미널에서 다시 실행하세요.

## API 접근

다음은 `파워셸`에서 API 접근을 보여주는 간단한 예입니다:

```powershell
(Invoke-WebRequest -method POST -Body '{"model":"llama3.2", "prompt":"Why is the sky blue?", "stream": false}' -uri http://localhost:11434/api/generate ).Content | ConvertFrom-json
```

## 문제 해결

Windows에서 Ollama는 여러 다른 위치에 파일을 저장합니다. `<윈도우 키>+R`을 눌러 탐색기 창에서 다음을 입력하여 확인할 수 있습니다:

- `explorer %LOCALAPPDATA%\Ollama`에는 로그 및 다운로드한 업데이트가 포함되어 있습니다.
    - *app.log*에는 GUI 애플리케이션의 최근 로그가 포함되어 있습니다.
    - *server.log*에는 가장 최근의 서버 로그가 포함되어 있습니다.
    - *upgrade.log*에는 업그레이드에 대한 로그 출력이 포함되어 있습니다.
- `explorer %LOCALAPPDATA%\Programs\Ollama`에는 이진 파일이 포함되어 있습니다(설치 프로그램이 사용자 PATH에 추가함).
- `explorer %HOMEPATH%\.ollama`에는 모델 및 구성 파일이 포함되어 있습니다.
- `explorer %TEMP%`에는 하나 이상의 `ollama*` 디렉토리에 임시 실행 파일이 포함되어 있습니다.

## 제거

Ollama Windows 설치 프로그램은 제거 프로그램을 등록합니다. Windows 설정의 `프로그램 추가 또는 제거`에서 Ollama를 제거할 수 있습니다.

> [!NOTE]
> `OLLAMA_MODELS` 위치를 변경한 경우, 설치 프로그램이 다운로드한 모델을 제거하지 않습니다.

## 독립 실행형 CLI

Windows에서 Ollama를 설치하는 가장 쉬운 방법은 `OllamaSetup.exe` 설치 프로그램을 사용하는 것입니다. 이 설치 프로그램은 관리자 권한 없이 계정에 설치됩니다. 우리는 최신 모델을 지원하기 위해 Ollama를 정기적으로 업데이트하며, 이 설치 프로그램은 최신 상태를 유지하는 데 도움을 줄 것입니다.

Ollama를 서비스로 설치하거나 통합하고자 하는 경우, 독립 실행형 `ollama-windows-amd64.zip` ZIP 파일이 제공되어 Ollama CLI와 Nvidia 및 AMD에 대한 GPU 라이브러리 종속성만 포함되어 있습니다. 이를 통해 기존 애플리케이션에 Ollama를 통합하거나 `ollama serve`를 통해 시스템 서비스로 실행할 수 있습니다. [NSSM](https://nssm.cc/)과 같은 도구를 사용할 수 있습니다.

> [!NOTE]  
> 이전 버전에서 업그레이드하는 경우, 먼저 이전 디렉터리를 제거해야 합니다.