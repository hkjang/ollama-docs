# Ollama 도커 이미지

### CPU 전용

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### Nvidia GPU
[NVIDIA 컨테이너 툴킷](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)을 설치합니다.

#### Apt를 이용한 설치
1. 저장소 구성
    ```bash
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
        | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
    curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
        | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
        | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    sudo apt-get update
    ```
2. NVIDIA 컨테이너 툴킷 패키지 설치
    ```bash
    sudo apt-get install -y nvidia-container-toolkit
    ```

#### Yum 또는 Dnf를 이용한 설치
1. 저장소 구성

    ```bash
    curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo \
        | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
    ```

2. NVIDIA 컨테이너 툴킷 패키지 설치

    ```bash
    sudo yum install -y nvidia-container-toolkit
    ```

#### Docker를 Nvidia 드라이버 사용하도록 구성
```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

#### 컨테이너 시작

```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

> [!NOTE]  
> NVIDIA JetPack 시스템에서 실행 중인 경우, Ollama는 자동으로 올바른 JetPack 버전을 발견할 수 없습니다. 컨테이너에 환경 변수 `JETSON_JETPACK=5` 또는 `JETSON_JETPACK=6`을 전달하여 버전 5 또는 6을 선택하세요.

### AMD GPU

AMD GPU를 이용하여 Ollama를 도커로 실행하려면 `rocm` 태그와 다음 명령어를 사용하세요:

```
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

### 모델 로컬 실행

이제 모델을 실행할 수 있습니다:

```
docker exec -it ollama ollama run llama3.2
```

### 다양한 모델 시도

더 많은 모델은 [Ollama 라이브러리](https://ollama.com/library)에서 확인할 수 있습니다.