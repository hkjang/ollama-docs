# 개발

필요한 도구 설치:

- Go 버전 1.22 이상
- 운영 체제에 맞는 C/C++ 컴파일러 (아래 참조)
- GNU Make

## 개요

Ollama는 GPU와 인터페이스하기 위해 Go와 C/C++ 코드를 혼합하여 사용합니다. C/C++ 코드는 CGO 및 GPU 라이브러리 전용 컴파일러로 컴파일됩니다. 프로젝트를 컴파일하기 위해 일련의 GNU Makefiles가 사용됩니다. GPU 라이브러리는 해당 라이브러리에서 사용하는 일반적인 환경 변수를 기반으로 자동 감지되지만, 필요 시 재정의할 수 있습니다. 기본 메이크 타겟은 리포지토리 디렉토리 내에서 실행될 러너와 주요 Go Ollama 애플리케이션을 빌드합니다. 아래 예시에서는 빌드를 가속화하기 위해 5개의 병렬 작업을 제안하는 `-j 5` 옵션을 사용합니다. CPU 코어 수에 따라 작업 수를 조정하여 빌드 시간을 줄일 수 있습니다. 빌드된 바이너리를 다른 위치로 이동하려면 `dist` 타겟을 사용하고 `./dist/$OS-$ARCH/`에 있는 파일을 원하는 위치로 재귀적으로 복사하면 됩니다. 다른 메이크 타겟에 대한 정보는 `make help`를 사용하여 확인할 수 있습니다.

GPU/CPU 러너를 빌드한 후에는 `go build .` 명령어로 주요 애플리케이션을 컴파일할 수 있습니다.

### MacOS

[Go 다운로드](https://go.dev/dl/)

```bash
make -j 5
```

이제 `ollama`를 실행할 수 있습니다:

```bash
./ollama
```

#### Xcode 15 경고

Xcode 버전 14 이상을 사용 중인 경우, `go build` 중에 `ld: warning: ignoring duplicate libraries: '-lobjc'`라는 경고가 발생할 수 있습니다. 이는 Golang의 문제로 안전하게 무시할 수 있습니다. 경고를 억제하려면 다음 명령어를 사용하세요.

```bash
export CGO_LDFLAGS="-Wl,-no_warn_duplicate_libraries"
```

### 리눅스

#### 리눅스 CUDA (NVIDIA)

_귀하의 운영 체제 배포판에는 이미 NVIDIA CUDA 패키지가 포함되어 있을 수 있습니다. 배포판 패키지는 종종 더 선호되지만, 설치 방법은 배포판에 따라 다릅니다. 가능하다면 배포판별 문서를 참조하여 종속성을 확인하세요!_

`make`, `gcc`, `golang` 및 [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads) 개발 및 런타임 패키지를 설치합니다.

일반적으로 Makefile은 CUDA를 자동으로 감지하지만, 리눅스 배포판이나 설치 방식에서 대체 경로를 사용하는 경우 `CUDA_PATH`를 CUDA 툴킷의 위치로 재정의하여 지정할 수 있습니다. 또한, `CUDA_ARCHITECTURES`를 설정하여 대상 CUDA 아키텍처를 사용자 정의할 수 있습니다 (예: `CUDA_ARCHITECTURES=50;60;70`).

```bash
make -j 5
```

v11 및 v12 툴킷이 모두 감지되면 기본적으로 두 주요 버전의 러너가 빌드됩니다. v12만 빌드하려면 다음 명령어를 사용하세요.

```bash
make cuda_v12
```

#### 이전 리눅스 CUDA (NVIDIA)

Compute Capability 3.5 또는 3.7을 지원하기 위해 [Unix Driver Archive](https://www.nvidia.com/en-us/drivers/unix/)에서 이전 버전의 드라이버(470으로 테스트됨)와 [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) (CUDA V11으로 테스트됨)를 사용해야 합니다. Ollama를 빌드할 때, 다음과 같이 두 개의 메이크 변수를 설정하여 Ollama가 지원하는 최소 컴퓨팅 능력을 조정해야 합니다.

```bash
make -j 5 CUDA_ARCHITECTURES="35;37;50;52" EXTRA_GOLDFLAGS="-X=github.com/ollama/ollama/discover.CudaComputeMajorMin=3" "-X=github.com/ollama/ollama/discover.CudaComputeMinorMin=5"
```

이전 GPU의 컴퓨팅 능력을 확인하려면 [GPU Compute Capability](https://developer.nvidia.com/cuda-gpus)를 참조하세요.

#### 리눅스 ROCm (AMD)

_귀하의 운영 체제 배포판에는 이미 AMD ROCm 패키지가 포함되어 있을 수 있습니다. 배포판 패키지는 종종 더 선호되지만, 설치 방법은 배포판에 따라 다릅니다. 가능하다면 배포판별 문서를 참조하여 종속성을 확인하세요!_

먼저 [ROCm](https://rocm.docs.amd.com/en/latest/) 개발 패키지를 설치하고, `make`, `gcc`, `golang`을 설치합니다.

일반적으로 빌드 스크립트는 ROCm을 자동으로 감지하지만, 리눅스 배포판이나 설치 방식에서 비정상적인 경로를 사용하는 경우, ROCm 설치 위치(일반적으로 `/opt/rocm`)에 `HIP_PATH` 환경 변수를 지정하여 위치를 설정할 수 있습니다. AMD GPU 대상을 사용자 정의하려면 `HIP_ARCHS`를 설정하세요 (예: `HIP_ARCHS=gfx1101;gfx1102`).

```bash
make -j 5
```

ROCm은 런타임에 GPU에 접근하기 위해 상승된 권한이 필요합니다. 대부분의 배포판에서는 사용자 계정을 `render` 그룹에 추가하거나 루트로 실행할 수 있습니다.

#### 컨테이너화된 리눅스 빌드

도커와 buildx가 가능하다면, CUDA 및 ROCm 종속성이 포함된 `./scripts/build_linux.sh` 스크립트를 사용하여 리눅스 바이너리를 빌드할 수 있습니다. 결과 아티팩트는 `./dist`에 배치되며, 기본적으로 스크립트는 arm64와 amd64 바이너리 모두를 빌드합니다. amd64만 빌드하려면 다음 명령어를 사용하세요.

```bash
PLATFORM=linux/amd64 ./scripts/build_linux.sh
```

### 윈도우

CPU 추론 지원을 빌드하기 위해 필요한 최소 개발 환경 도구는 다음과 같습니다.

- Go 버전 1.22 이상
  - [Go 다운로드](https://go.dev/dl/)
- Git
  - [Git 다운로드](https://git-scm.com/download/win)
- clang과 gcc 호환, Make. 윈도우에서 이 도구를 설치하는 방법에는 여러 가지 옵션이 있으며, 다음 방법을 확인했지만 다른 방법도 작동할 수 있습니다:
  - [MSYS2](https://www.msys2.org/)
    - 설치 후, MSYS2 터미널에서 다음 명령어를 실행하여 필요한 도구를 설치합니다.
    ```bash
    pacman -S mingw-w64-clang-x86_64-gcc-compat mingw-w64-clang-x86_64-clang make
    ```
  - 위에서 MSYS2의 기본 설치 접두사를 사용한 경우, `C:\msys64\clang64\bin` 및 `C:\msys64\usr\bin`을 빌드 단계를 수행할 환경 변수 `PATH`에 추가하세요 (예: 시스템 전체, 계정 수준, PowerShell, cmd 등).

> [!참고]  
> 유니코드 지원을 위한 GCC C++ 라이브러리의 버그로 인해, 윈도우에서 Ollama는 clang으로 빌드해야 합니다.

```bash
make -j 5
```

#### GPU 지원

GPU 도구는 Microsoft 네이티브 빌드 도구를 요구합니다. CUDA 또는 ROCm 중 하나를 빌드하려면 먼저 Visual Studio를 통해 MSVC를 설치해야 합니다:

- Visual Studio 설치 시 `C++를 사용한 데스크탑 개발`을 작업 부하로 선택해야 합니다.
- 도구가 제대로 등록되기 위해 CUDA 또는 ROCm 설치 전에 Visual Studio 설치를 완료하고 한 번 실행해야 합니다.
- **64비트(x64)** 컴파일러(`cl.exe`)의 위치를 `PATH`에 추가하세요.
- 주의: 기본 개발자 셸은 32비트(x86) 컴파일러를 구성할 수 있으며, 이는 빌드 실패로 이어질 수 있습니다. Ollama는 64비트 툴체인을 요구합니다.

#### 윈도우 CUDA (NVIDIA)

위에 설명된 일반 윈도우 개발 도구와 MSVC 외에도:

- [NVIDIA CUDA 설치 가이드](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

#### 윈도우 ROCm (AMD Radeon)

위에 설명된 일반 윈도우 개발 도구와 MSVC 외에도:

- [AMD HIP SDK](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)

#### 윈도우 arm64

기본 `VS 2022용 개발자 PowerShell`은 x86으로 기본 설정될 수 있습니다. arm64 개발 환경을 보장하려면 일반 PowerShell 터미널을 시작하고 다음을 실행하세요:

```powershell
import-module 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Microsoft.VisualStudio.DevShell.dll'
Enter-VsDevShell -Arch arm64 -vsinstallpath 'C:\Program Files\Microsoft Visual Studio\2022\Community' -skipautomaticlocation
```

`write-host $env:VSCMD_ARG_TGT_ARCH`으로 확인할 수 있습니다.

https://www.msys2.org/wiki/arm64/ 의 지침을 따라 arm64 MSYS2 환경을 설정하세요. Ollama는 컴파일을 위해 `gcc`와 `mingw32-make`가 필요하며, 현재 윈도우 arm64에서는 사용할 수 없지만, `mingw-w64-clang-aarch64-gcc-compat`를 통해 gcc 호환 어댑터를 사용할 수 있습니다. 최소한 다음을 설치해야 합니다:

```bash
pacman -S mingw-w64-clang-aarch64-clang mingw-w64-clang-aarch64-gcc-compat mingw-w64-clang-aarch64-make make
```

Ollama를 소스에서 빌드하기 위해 `PATH`에 `go`, `cmake`, `gcc` 및 `clang mingw32-make`를 포함해야 합니다 (일반적으로 `C:\msys64\clangarm64\bin\`).

## 고급 CPU 벡터 설정

x86에서 `make`를 실행하면 여러 CPU 러너가 컴파일되어 다양한 CPU 계열에서 실행할 수 있습니다. 런타임 시 Ollama는 최적의 변형을 자동 감지하여 로드합니다. GPU 라이브러리가 빌드 시 존재하면 Ollama는 `AVX` CPU 벡터 기능이 활성화된 GPU 러너도 컴파일합니다. 이는 GPU와 CPU에 걸쳐 분할된 대형 모델을 로드할 때 광범위한 호환성으로 우수한 성능 균형을 제공합니다. 일부 사용자는 벡터 확장 기능 없이 빌드를 선호할 수 있으며 (예: 구형 Xeon/Celeron 프로세서 또는 벡터 기능을 마스킹하는 하이퍼바이저), 다른 사용자는 모델 로드 성능 향상을 위해 더 많은 벡터 확장 기능을 활성화하는 것을 선호할 수 있습니다.

CPU 러너와 모든 GPU 러너에 대해 활성화된 CPU 벡터 기능 집합을 사용자 정의하려면 빌드 시 `CUSTOM_CPU_FLAGS`를 사용하세요.

벡터 플래그 없이 빌드하려면:

```bash
make CUSTOM_CPU_FLAGS=""
```

AVX와 AVX2를 모두 포함하여 빌드하려면:

```bash
make CUSTOM_CPU_FLAGS=avx,avx2
```

AVX512 기능을 활성화하여 빌드하려면:

```bash
make CUSTOM_CPU_FLAGS=avx,avx2,avx512,avx512vbmi,avx512vnni,avx512bf16
```

> [!참고]  
> 서로 다른 플래그를 실험하는 경우, 새 컴파일러 플래그로 모든 것이 재빌드되도록 각 변경 사항 사이에 `make clean`을 수행하세요. 빌드 시 Ollama는 `AVX` CPU 벡터 기능을 활성화한 GPU 러너를 컴파일합니다. 이는 대형 모델을 GPU와 CPU에 걸쳐 분할하여 로드할 때 좋은 성능 균형을 제공합니다. 일부 사용자는 벡터 확장이 없는 것을 선호할 수 있으며(예: 구형 Xeon 또는 Celeron 프로세서나 벡터 기능을 마스킹하는 하이퍼바이저) 다른 사용자는 분할 모델 로드의 성능을 더욱 향상시키기 위해 더 많은 벡터 확장을 활성화하는 것을 선호할 수 있습니다.

CPU 러너와 모든 GPU 러너에 대해 활성화할 CPU 벡터 기능 집합을 사용자 정의하려면 빌드 중에 `CUSTOM_CPU_FLAGS`를 사용하십시오.

벡터 플래그 없이 빌드하려면:

```
make CUSTOM_CPU_FLAGS=""
```

AVX와 AVX2를 모두 활성화하여 빌드하려면:
```
make CUSTOM_CPU_FLAGS=avx,avx2
```

AVX512 기능을 활성화하여 빌드하려면:

```
make CUSTOM_CPU_FLAGS=avx,avx2,avx512,avx512vbmi,avx512vnni,avx512bf16
```

> [!NOTE]  
> 다양한 플래그를 실험할 경우, 각 변경 사항 사이에 `make clean`을 실행하여 모든 것이 새로운 컴파일러 플래그로 다시 빌드되도록 해야 합니다.