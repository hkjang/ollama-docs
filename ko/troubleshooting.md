# 문제 해결 방법

때때로 올라마가 예상대로 작동하지 않을 수 있습니다. 문제의 원인을 파악하는 가장 좋은 방법 중 하나는 로그를 확인하는 것입니다. **맥(Mac)**에서는 다음 명령어를 실행하여 로그를 찾을 수 있습니다:

```shell
cat ~/.ollama/logs/server.log
```

**리눅스(Linux)** 시스템에서는 **시스템디(systemd)**를 사용하는 경우, 다음 명령어로 로그를 찾을 수 있습니다:

```shell
journalctl -u ollama --no-pager
```

**컨테이너(container)**에서 올라마를 실행할 때 로그는 컨테이너의 표준 출력/표준 오류(stdout/stderr)로 전송됩니다:

```shell
docker logs <container-name>
```
(`docker ps`를 사용하여 컨테이너 이름을 찾을 수 있습니다)

터미널에서 `ollama serve`를 수동으로 실행하면, 로그는 해당 터미널에서 확인할 수 있습니다.

**윈도우즈(Windows)**에서 올라마를 실행할 경우, 몇 가지 다른 위치에서 로그를 확인할 수 있습니다. `<cmd>+R`을 눌러 탐색기 창에서 다음을 입력하세요:
- `explorer %LOCALAPPDATA%\Ollama`를 입력하면 로그를 볼 수 있습니다. 가장 최근의 서버 로그는 `server.log`에 있으며, 이전 로그는 `server-#.log`에 있습니다.
- `explorer %LOCALAPPDATA%\Programs\Ollama`를 입력하면 바이너리 파일들을 탐색할 수 있습니다 (설치 프로그램이 이 경로를 사용자 PATH에 추가합니다).
- `explorer %HOMEPATH%\.ollama`를 입력하면 모델과 구성이 저장된 위치를 탐색할 수 있습니다.
- `explorer %TEMP%`를 입력하면 임시 실행 파일들이 `ollama*` 디렉토리에 저장된 위치를 확인할 수 있습니다.

문제 해결을 돕기 위해 추가적인 디버그 로깅(debug logging)을 활성화하려면, 먼저 **트레이 메뉴에서 실행 중인 앱을 종료한 후** PowerShell(파워셸) 터미널에서 다음을 입력하세요:
```powershell
$env:OLLAMA_DEBUG="1"
& "ollama app.exe"
```

로그 해석에 대한 도움이 필요하시면 [디스코드(Discord)](https://discord.gg/ollama)에 참여하세요.

## LLM 라이브러리들

올라마는 다양한 GPU들(그래픽 처리 장치)과 CPU 벡터 기능들에 맞춰 컴파일된 여러 LLM 라이브러리들을 포함하고 있습니다. 올라마는 시스템의 기능에 따라 최적의 라이브러리를 선택하려고 합니다. 이 자동 감지(autodetection)에 문제가 발생하거나 GPU에서 충돌이 생길 경우, 특정 LLM 라이브러리를 강제로 사용할 수 있습니다. `cpu_avx2`가 가장 성능이 좋고, 그 다음이 `cpu_avx`, 가장 느리지만 호환성이 높은 것은 `cpu`입니다. MacOS의 로제타(Rosetta) 에뮬레이션은 `cpu` 라이브러리와 함께 작동합니다.

서버 로그에서는 다음과 비슷한 메시지를 볼 수 있습니다(버전마다 다를 수 있음):

```
동적 LLM 라이브러리들 [rocm_v6 cpu cpu_avx cpu_avx2 cuda_v11 rocm_v5]
```

**실험적 LLM 라이브러리 오버라이드**

자동 감지를 우회하기 위해 OLLAMA_LLM_LIBRARY를 사용하여 사용 가능한 LLM 라이브러리 중 하나로 설정할 수 있습니다. 예를 들어, CUDA 카드가 있으나 AVX2 벡터 지원이 있는 CPU LLM 라이브러리를 강제로 사용하고자 할 경우, 다음과 같이 입력하세요:

```
OLLAMA_LLM_LIBRARY="cpu_avx2" ollama serve
```

CPU의 기능을 확인하려면 다음을 입력하세요.
```
cat /proc/cpuinfo | grep flags | head -1
```

## 리눅스(Linux)에서 이전 또는 미리 릴리스된 버전 설치하기

리눅스에서 문제가 발생하여 이전 버전을 설치하고 싶거나 공식 출시 전에 미리 릴리스된 버전을 사용해 보고 싶다면, 설치 스크립트에 설치할 버전을 지정할 수 있습니다.

```sh
curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION="0.1.29" sh
```

## 리눅스(Linux) noexec 플래그 설정된 tmp 디렉토리

시스템이 올라마가 임시 실행 파일을 저장하는 위치에 "noexec 플래그(noexec flag)"가 설정된 경우, OLLAMA_TMPDIR를 올라마가 실행되는 사용자에게 쓰기 가능한 위치로 설정하여 대체 위치를 지정할 수 있습니다. 예를 들어 OLLAMA_TMPDIR=/usr/share/ollama/로 설정할 수 있습니다.

## NVIDIA GPU 발견

올라마가 시작할 때, 시스템에 존재하는 GPU들을 조사하여 호환성과 사용 가능한 VRAM (비디오 메모리)의 양을 확인합니다. 때때로 이 발견 과정에서 GPU를 찾지 못할 수 있습니다. 일반적으로 최신 드라이버를 실행하면 최상의 결과를 얻을 수 있습니다.

### 리눅스(Linux) NVIDIA 문제 해결

올라마를 실행하기 위해 컨테이너(container)를 사용하는 경우, 먼저 [docker.md](./docker.md)에서 설명한 대로 컨테이너 런타임을 설정했는지 확인하세요.

때때로 올라마가 GPU 초기화에 어려움을 겪을 수 있습니다. 서버 로그를 확인하면 "3" (초기화되지 않음), "46" (장치 사용 불가), "100" (장치 없음), "999" (알 수 없음) 등의 다양한 오류 코드가 나타날 수 있습니다. 다음 문제 해결 기법이 문제를 해결하는 데 도움이 될 수 있습니다.

- 컨테이너를 사용 중이라면, 컨테이너 런타임이 작동하고 있는지 확인하세요. `docker run --gpus all ubuntu nvidia-smi`를 시도해보세요 - 이 명령이 작동하지 않으면 올라마가 NVIDIA GPU를 인식할 수 없습니다.
- uvm 드라이버가 로드되었는지 확인하세요. `sudo nvidia-modprobe -u`
- nvidia_uvm 드라이버를 다시 로드해보세요 - `sudo rmmod nvidia_uvm` 다음에 `sudo modprobe nvidia_uvm`
- 재부팅해보세요.
- 최신 NVIDIA 드라이버를 실행하고 있는지 확인하세요.

위의 방법들이 문제를 해결하지 못한다면, 추가 정보를 수집하고 이슈를 제출하세요:
- `CUDA_ERROR_LEVEL=50`을 설정하고 다시 시도하여 더 많은 진단 로그를 얻으세요.
- dmesg에서 오류를 확인하세요 `sudo dmesg | grep -i nvrm` 및 `sudo dmesg | grep -i nvidia`

## AMD GPU 발견

리눅스(Linux)에서 AMD GPU 접근은 일반적으로 `/dev/kfd` 장치에 접근하기 위해 `video` 및/또는 `render` 그룹의 멤버십을 요구합니다. 권한이 올바르게 설정되지 않으면, 올라마가 이를 감지하고 서버 로그에 오류를 보고합니다.

컨테이너(container)에서 실행할 경우, 일부 리눅스 배포판 및 컨테이너 런타임에서는 올라마 프로세스가 GPU에 접근할 수 없을 수 있습니다. 호스트 시스템에서 `ls -lnd /dev/kfd /dev/dri /dev/dri/*`를 사용하여 시스템의 **숫자** 그룹 ID를 확인하고, 필요한 장치에 접근할 수 있도록 추가 `--group-add ...` 인수를 컨테이너에 전달하세요. 예를 들어, 다음 출력에서 `crw-rw---- 1 0  44 226,   0 Sep 16 16:55 /dev/dri/card0`의 그룹 ID 열은 `44`입니다.

올라마가 처음에 GPU에서 잘 작동했지만, 이후 서버 로그에서 GPU 발견 실패 오류가 발생하면서 CPU로 전환되는 경우, Docker에서 시스템디(systemd) cgroup 관리를 비활성화하여 해결할 수 있습니다. 호스트에서 `/etc/docker/daemon.json`을 편집하고 `"exec-opts": ["native.cgroupdriver=cgroupfs"]`를 도커 구성에 추가하세요.

올라마가 GPU를 올바르게 발견하거나 추론에 사용하는 데 문제가 발생한다면, 다음 방법들이 실패 원인을 가려내는 데 도움이 될 수 있습니다.
- `AMD_LOG_LEVEL=3`을 설정하여 AMD HIP/ROCm 라이브러리에서 정보 로그 레벨을 활성화하세요. 이를 통해 문제 해결에 도움이 되는 더 자세한 오류 코드를 확인할 수 있습니다.
- `OLLAMA_DEBUG=1`을 설정하면 GPU 발견 중 추가 정보가 보고됩니다.
- amdgpu 또는 kfd 드라이버의 오류를 확인하세요 `sudo dmesg | grep -i amdgpu` 및 `sudo dmesg | grep -i kfd`

## 여러 AMD GPU 사용 시

리눅스(Linux)에서 여러 AMD GPU에 걸쳐 모델을 로드할 때 의미 없는 응답이 발생하는 경우, 다음 가이드를 참조하세요.

- https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/mgpu.html#mgpu-known-issues-and-limitations

## 윈도우즈(Windows) 터미널 오류

구버전의 윈도우즈 10 (예: 21H1)에서 표준 터미널 프로그램이 제어 문자를 올바르게 표시하지 않는 버그가 알려져 있습니다. 이로 인해 `←[?25h←[?25l`와 같은 긴 문자열이 표시되며, 때때로 `The parameter is incorrect`라는 오류가 발생할 수 있습니다. 이 문제를 해결하려면 윈도우즈 10 22H1 이상으로 업데이트하세요.