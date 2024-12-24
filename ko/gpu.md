# GPU
## Nvidia
Ollama는 컴퓨트 능력 5.0 이상의 Nvidia GPU를 지원합니다.

지원되는 카드를 확인하려면 컴퓨트 호환성을 확인하세요:
[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

| 컴퓨트 능력 | 계열               | 카드                                                                                                       |
| ------------ | ------------------ | ----------------------------------------------------------------------------------------------------------- |
| 9.0          | NVIDIA             | `H100`                                                                                                      |
| 8.9          | GeForce RTX 40xx   | `RTX 4090` `RTX 4080 SUPER` `RTX 4080` `RTX 4070 Ti SUPER` `RTX 4070 Ti` `RTX 4070 SUPER` `RTX 4070` `RTX 4060 Ti` `RTX 4060`  |
|              | NVIDIA Professional | `L4` `L40` `RTX 6000`                                                                                       |
| 8.6          | GeForce RTX 30xx   | `RTX 3090 Ti` `RTX 3090` `RTX 3080 Ti` `RTX 3080` `RTX 3070 Ti` `RTX 3070` `RTX 3060 Ti` `RTX 3060` `RTX 3050 Ti` `RTX 3050`   |
|              | NVIDIA Professional | `A40` `RTX A6000` `RTX A5000` `RTX A4000` `RTX A3000` `RTX A2000` `A10` `A16` `A2`                          |
| 8.0          | NVIDIA             | `A100` `A30`                                                                                                |
| 7.5          | GeForce GTX/RTX    | `GTX 1650 Ti` `TITAN RTX` `RTX 2080 Ti` `RTX 2080` `RTX 2070` `RTX 2060`                                    |
|              | NVIDIA Professional | `T4` `RTX 5000` `RTX 4000` `RTX 3000` `T2000` `T1200` `T1000` `T600` `T500`                                 |
|              | Quadro             | `RTX 8000` `RTX 6000` `RTX 5000` `RTX 4000`                                                                 |
| 7.0          | NVIDIA             | `TITAN V` `V100` `Quadro GV100`                                                                             |
| 6.1          | NVIDIA TITAN       | `TITAN Xp` `TITAN X`                                                                                        |
|              | GeForce GTX        | `GTX 1080 Ti` `GTX 1080` `GTX 1070 Ti` `GTX 1070` `GTX 1060` `GTX 1050 Ti` `GTX 1050`                       |
|              | Quadro             | `P6000` `P5200` `P4200` `P3200` `P5000` `P4000` `P3000` `P2200` `P2000` `P1000` `P620` `P600` `P500` `P520` |
|              | Tesla              | `P40` `P4`                                                                                                  |
| 6.0          | NVIDIA             | `Tesla P100` `Quadro GP100`                                                                                 |
| 5.2          | GeForce GTX        | `GTX TITAN X` `GTX 980 Ti` `GTX 980` `GTX 970` `GTX 960` `GTX 950`                                          |
|              | Quadro             | `M6000 24GB` `M6000` `M5000` `M5500M` `M4000` `M2200` `M2000` `M620`                                        |
|              | Tesla              | `M60` `M40`                                                                                                 |
| 5.0          | GeForce GTX        | `GTX 750 Ti` `GTX 750` `NVS 810`                                                                            |
|              | Quadro             | `K2200` `K1200` `K620` `M1200` `M520` `M5000M` `M4000M` `M3000M` `M2000M` `M1000M` `K620M` `M600M` `M500M`  |

구형 GPU를 지원하기 위해 로컬에서 빌드하려면 [developer.md](./development.md#linux-cuda-nvidia)를 참조하세요.

### GPU 선택

시스템에 여러 개의 NVIDIA GPU가 있는 경우 Ollama가 특정 GPU 집합만 사용하도록 제한할 수 있습니다. 이 경우 `CUDA_VISIBLE_DEVICES`에 GPU 목록을 쉼표로 구분하여 설정하면 됩니다. 숫자 ID를 사용할 수 있지만 순서가 다를 수 있으므로 UUIDs를 사용하는 것이 더 신뢰할 수 있습니다. GPU의 UUID를 확인하려면 `nvidia-smi -L`을 실행하세요. GPU를 무시하고 CPU 사용을 강제하려면 잘못된 GPU ID(예: "-1")를 사용하세요.

### 노트북 일시 중지/재개

리눅스에서 일시 중지/재개 주기 후, 가끔 Ollama가 NVIDIA GPU를 발견하지 못하고 CPU에서 실행됩니다. 이 드라이버 버그를 우회하려면 `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm` 명령어로 NVIDIA UVM 드라이버를 다시 로드하면 됩니다.

## AMD 라데온
Ollama는 다음 AMD GPU를 지원합니다:

### 리눅스 지원
| 계열           | 카드 및 가속기                                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| AMD Radeon RX  | `7900 XTX` `7900 XT` `7900 GRE` `7800 XT` `7700 XT` `7600 XT` `7600` `6950 XT` `6900 XTX` `6900XT` `6800 XT` `6800` `Vega 64` `Vega 56`    |
| AMD Radeon PRO | `W7900` `W7800` `W7700` `W7600` `W7500` `W6900X` `W6800X Duo` `W6800X` `W6800` `V620` `V420` `V340` `V320` `Vega II Duo` `Vega II` `VII` `SSG` |
| AMD Instinct   | `MI300X` `MI300A` `MI300` `MI250X` `MI250` `MI210` `MI200` `MI100` `MI60` `MI50`                                                               |

### 윈도우 지원
ROCm v6.1을 사용하면 다음 GPU가 윈도우에서 지원됩니다.

| 계열           | 카드 및 가속기                                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| AMD Radeon RX  | `7900 XTX` `7900 XT` `7900 GRE` `7800 XT` `7700 XT` `7600 XT` `7600` `6950 XT` `6900 XTX` `6900XT` `6800 XT` `6800`    |
| AMD Radeon PRO | `W7900` `W7800` `W7700` `W7600` `W7500` `W6900X` `W6800X Duo` `W6800X` `W6800` `V620` |

### 리눅스의 오버라이드
Ollama는 AMD ROCm 라이브러리를 활용하며, 이는 모든 AMD GPU를 지원하지 않습니다. 경우에 따라 유사한 LLVM 타겟을 사용하도록 시스템을 강제할 수 있습니다. 예를 들어, Radeon RX 5400은 `gfx1034`(10.3.4로도 알려짐)이지만, ROCm은 현재 이 타겟을 지원하지 않습니다. 가장 가까운 지원은 `gfx1030`입니다. 환경 변수 `HSA_OVERRIDE_GFX_VERSION`을 `x.y.z` 구문으로 설정할 수 있습니다. 예를 들어, RX 5400에서 시스템을 실행하도록 강제하려면 서버의 환경 변수로 `HSA_OVERRIDE_GFX_VERSION="10.3.0"`을 설정하면 됩니다. 지원되지 않는 AMD GPU가 있는 경우 아래 지원되는 유형 목록을 사용하여 실험할 수 있습니다.

여러 개의 서로 다른 GFX 버전의 GPU가 있는 경우, 환경 변수에 숫자 장치 번호를 추가하여 개별적으로 설정할 수 있습니다. 예를 들어, `HSA_OVERRIDE_GFX_VERSION_0=10.3.0` 및 `HSA_OVERRIDE_GFX_VERSION_1=11.0.0`과 같이 설정합니다.

현재 리눅스에서 알려진 지원 GPU 유형은 다음 LLVM 타겟입니다. 이 표는 이러한 LLVM 타겟에 매핑되는 일부 예시 GPU를 보여줍니다:

| **LLVM 타겟** | **예시 GPU**           |
|---------------|------------------------|
| gfx900        | Radeon RX Vega 56      |
| gfx906        | Radeon Instinct MI50   |
| gfx908        | Radeon Instinct MI100  |
| gfx90a        | Radeon Instinct MI210  |
| gfx940        | Radeon Instinct MI300  |
| gfx941        |                        |
| gfx942        |                        |
| gfx1030       | Radeon PRO V620        |
| gfx1100       | Radeon PRO W7900       |
| gfx1101       | Radeon PRO W7700       |
| gfx1102       | Radeon RX 7600         |

AMD는 ROCm v6을 개선하여 향후 릴리스에서 더 많은 GPU 계열의 지원을 확대할 계획입니다.

추가 도움이 필요하면 [Discord](https://discord.gg/ollama)에서 문의하거나 [이슈](https://github.com/ollama/ollama/issues)를 제출하세요.

### GPU 선택

시스템에 여러 개의 AMD GPU가 있는 경우 Ollama가 특정 GPU 집합만 사용하도록 제한할 수 있습니다. 이 경우 `ROCR_VISIBLE_DEVICES`에 GPU 목록을 쉼표로 구분하여 설정하면 됩니다. 장치 목록을 보려면 `rocminfo`를 사용하세요. GPU를 무시하고 CPU 사용을 강제하려면 잘못된 GPU ID(예: "-1")를 사용하세요. 가능할 경우, 숫자 값 대신 `Uuid`를 사용하여 장치를 고유하게 식별하세요.

### 컨테이너 권한

일부 리눅스 배포판에서 SELinux는 컨테이너가 AMD GPU 장치에 접근하는 것을 차단할 수 있습니다. 호스트 시스템에서 `sudo setsebool container_use_devices=1`을 실행하여 컨테이너가 장치를 사용할 수 있도록 허용할 수 있습니다.

### Metal (Apple GPU)
Ollama는 Metal API를 통해 Apple 장치에서 GPU 가속을 지원합니다. ### GPU 목록 확인하기

`rocminfo` 명령어를 사용하면 GPU를 포함한 장치 목록을 확인할 수 있습니다. 만약 GPU를 무시하고 CPU를 강제로 사용하고 싶다면, 잘못된 GPU ID(예: "-1")를 사용하면 됩니다. 가능할 경우 숫자 값 대신 `Uuid`를 사용하여 장치를 고유하게 식별하는 것이 좋습니다.

### 컨테이너 권한

일부 리눅스 배포판에서는 SELinux가 컨테이너가 AMD GPU 장치에 접근하는 것을 차단할 수 있습니다. 호스트 시스템에서 `sudo setsebool container_use_devices=1` 명령어를 실행하면 컨테이너가 장치를 사용할 수 있도록 허용할 수 있습니다.

### Metal (애플 GPUs)

Ollama는 Metal API를 통해 애플 장치에서 GPU 가속화를 지원합니다.

---

# GPU

## Nvidia

Ollama는 컴퓨트 능력이 5.0 이상인 Nvidia GPU를 지원합니다.

지원되는 카드인지 확인하려면 컴퓨트 호환성을 확인하세요:
[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

| 컴퓨트 능력 | 패밀리               | 카드                                                                                                          |
| ------------ | -------------------- | ------------------------------------------------------------------------------------------------------------- |
| 9.0          | NVIDIA               | `H100`                                                                                                        |
| 8.9          | GeForce RTX 40xx     | `RTX 4090` `RTX 4080 SUPER` `RTX 4080` `RTX 4070 Ti SUPER` `RTX 4070 Ti` `RTX 4070 SUPER` `RTX 4070` `RTX 4060 Ti` `RTX 4060`  |
|              | NVIDIA Professional  | `L4` `L40` `RTX 6000`                                                                                         |
| 8.6          | GeForce RTX 30xx     | `RTX 3090 Ti` `RTX 3090` `RTX 3080 Ti` `RTX 3080` `RTX 3070 Ti` `RTX 3070` `RTX 3060 Ti` `RTX 3060` `RTX 3050 Ti` `RTX 3050`   |
|              | NVIDIA Professional  | `A40` `RTX A6000` `RTX A5000` `RTX A4000` `RTX A3000` `RTX A2000` `A10` `A16` `A2`                            |
| 8.0          | NVIDIA               | `A100` `A30`                                                                                                  |
| 7.5          | GeForce GTX/RTX      | `GTX 1650 Ti` `TITAN RTX` `RTX 2080 Ti` `RTX 2080` `RTX 2070` `RTX 2060`                                      |
|              | NVIDIA Professional  | `T4` `RTX 5000` `RTX 4000` `RTX 3000` `T2000` `T1200` `T1000` `T600` `T500`                                   |
|              | Quadro               | `RTX 8000` `RTX 6000` `RTX 5000` `RTX 4000`                                                                   |
| 7.0          | NVIDIA               | `TITAN V` `V100` `Quadro GV100`                                                                               |
| 6.1          | NVIDIA TITAN         | `TITAN Xp` `TITAN X`                                                                                            |
|              | GeForce GTX          | `GTX 1080 Ti` `GTX 1080` `GTX 1070 Ti` `GTX 1070` `GTX 1060` `GTX 1050 Ti` `GTX 1050`                       |
|              | Quadro               | `P6000` `P5200` `P4200` `P3200` `P5000` `P4000` `P3000` `P2200` `P2000` `P1000` `P620` `P600` `P500` `P520` |
|              | Tesla                | `P40` `P4`                                                                                                      |
| 6.0          | NVIDIA               | `Tesla P100` `Quadro GP100`                                                                                     |
| 5.2          | GeForce GTX          | `GTX TITAN X` `GTX 980 Ti` `GTX 980` `GTX 970` `GTX 960` `GTX 950`                                            |
|              | Quadro               | `M6000 24GB` `M6000` `M5000` `M5500M` `M4000` `M2200` `M2000` `M620`                                        |
|              | Tesla                | `M60` `M40`                                                                                                     |
| 5.0          | GeForce GTX          | `GTX 750 Ti` `GTX 750` `NVS 810`                                                                                |
|              | Quadro               | `K2200` `K1200` `K620` `M1200` `M520` `M5000M` `M4000M` `M3000M` `M2000M` `M1000M` `K620M` `M600M` `M500M`  |

로컬에서 더 오래된 GPU를 지원하도록 빌드하려면 [developer.md](./development.md#linux-cuda-nvidia)를 참조하세요.

### GPU 선택

시스템에 여러 Nvidia GPU가 있고 Ollama가 특정 GPU만 사용하도록 제한하려면, `CUDA_VISIBLE_DEVICES`를 GPU의 컴마로 구분된 목록으로 설정할 수 있습니다. 숫자 ID를 사용할 수 있지만, 순서가 변경될 수 있으므로 `Uuid` 사용이 더 신뢰할 수 있습니다. GPU의 `Uuid`를 확인하려면 `nvidia-smi -L` 명령어를 실행하세요. GPU를 무시하고 CPU를 강제로 사용하려면 잘못된 GPU ID(예: "-1")를 사용하세요.

### 노트북 서스펜드 및 재개

리눅스에서는 서스펜드/재개 사이클 후에 Ollama가 Nvidia GPU를 인식하지 못하고 CPU에서 실행될 수 있습니다. 이 드라이버 버그를 해결하려면 `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm` 명령어로 Nvidia UVM 드라이버를 다시 로드하세요.

## AMD Radeon

Ollama는 다음 AMD GPU를 지원합니다:

### Linux 지원

| 패밀리           | 카드 및 가속기                                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| AMD Radeon RX    | `7900 XTX` `7900 XT` `7900 GRE` `7800 XT` `7700 XT` `7600 XT` `7600` `6950 XT` `6900 XTX` `6900XT` `6800 XT` `6800` `Vega 64` `Vega 56`    |
| AMD Radeon PRO   | `W7900` `W7800` `W7700` `W7600` `W7500` `W6900X` `W6800X Duo` `W6800X` `W6800` `V620` `V420` `V340` `V320` `Vega II Duo` `Vega II` `VII` `SSG` |
| AMD Instinct     | `MI300X` `MI300A` `MI300` `MI250X` `MI250` `MI210` `MI200` `MI100` `MI60` `MI50`                                                               |

### Windows 지원

ROCm v6.1을 사용하면 다음 GPU가 Windows에서 지원됩니다.

| 패밀리           | 카드 및 가속기                                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| AMD Radeon RX    | `7900 XTX` `7900 XT` `7900 GRE` `7800 XT` `7700 XT` `7600 XT` `7600` `6950 XT` `6900 XTX` `6900XT` `6800 XT` `6800`    |
| AMD Radeon PRO   | `W7900` `W7800` `W7700` `W7600` `W7500` `W6900X` `W6800X Duo` `W6800X` `W6800` `V620` |

### 리눅스에서의 오버라이드

Ollama는 AMD ROCm 라이브러리를 활용하며, 이는 모든 AMD GPU를 지원하지 않습니다. 경우에 따라 비슷한 LLVM 타겟을 사용하도록 시스템을 강제할 수 있습니다. 예를 들어 Radeon RX 5400은 `gfx1034`(`10.3.4`로도 알려져 있음)이지만, ROCm은 현재 이 타겟을 지원하지 않습니다. 가장 가까운 지원 타겟은 `gfx1030`입니다. 서버의 환경 변수로 `HSA_OVERRIDE_GFX_VERSION`을 `x.y.z` 형식으로 설정하여 RX 5400에서 실행되도록 시스템을 강제할 수 있습니다. 예를 들어, `HSA_OVERRIDE_GFX_VERSION="10.3.0"`을 설정합니다. 지원되지 않는 AMD GPU가 있는 경우 아래 지원되는 유형 목록을 사용하여 실험할 수 있습니다.

다양한 GFX 버전을 가진 여러 GPU가 있는 경우, 환경 변수에 숫자 장치 번호를 추가하여 개별적으로 설정할 수 있습니다. 예를 들어, `HSA_OVERRIDE_GFX_VERSION_0=10.3.0` 및 `HSA_OVERRIDE_GFX_VERSION_1=11.0.0`와 같이 설정합니다.

현재 리눅스에서 알려진 지원 GPU 유형은 다음과 같은 LLVM 타겟입니다. 이 표는 이러한 LLVM 타겟에 매핑되는 일부 예시 GPU를 보여줍니다:

| **LLVM 타겟** | **예시 GPU**           |
| -------------- | ----------------------- |
| gfx900         | Radeon RX Vega 56       |
| gfx906         | Radeon Instinct MI50    |
| gfx908         | Radeon Instinct MI100   |
| gfx90a         | Radeon Instinct MI210   |
| gfx940         | Radeon Instinct MI300   |
| gfx941         |                         |
| gfx942         |                         |
| gfx1030        | Radeon PRO V620         |
| gfx1100        | Radeon PRO W7900        |
| gfx1101        | Radeon PRO W7700        |
| gfx1102        | Radeon RX 7600          |

AMD는 ROCm v6을 향상시켜 향후 릴리스에서 GPU 패밀리 지원을 확대함으로써 더 많은 GPU 지원을 늘리기 위해 작업 중입니다.

추가 지원이 필요하면 [Discord](https://discord.gg/ollama)에 문의하거나 [이슈](https://github.com/ollama/ollama/issues)를 제출하세요.

### GPU 선택

시스템에 여러 AMD GPU가 있고 Ollama가 특정 GPU만 사용하도록 제한하려면, `ROCR_VISIBLE_DEVICES`를 GPU의 컴마로 구분된 목록으로 설정할 수 있습니다. `rocminfo`를 사용하여 장치 목록을 확인할 수 있습니다. GPU를 무시하고 CPU를 강제로 사용하려면 잘못된 GPU ID(예: "-1")를 사용하세요. 가능할 경우 숫자 값 대신 `Uuid`를 사용하여 장치를 고유하게 식별하는 것이 좋습니다.

### 컨테이너 권한

일부 리눅스 배포판에서는 SELinux가 컨테이너가 AMD GPU 장치에 접근하는 것을 차단할 수 있습니다. 호스트 시스템에서 `sudo setsebool container_use_devices=1` 명령어를 실행하면 컨테이너가 장치를 사용할 수 있도록 허용할 수 있습니다.

### Metal (애플 GPUs)

Ollama는 Metal API를 통해 애플 장치에서 GPU 가속화를 지원합니다.