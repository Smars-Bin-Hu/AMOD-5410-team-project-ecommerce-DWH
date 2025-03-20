# Linux Container Initialize

```bash
apt update && apt install -y \
    iputils-ping \
    net-tools \
    netcat \
    procps \
    vim \
    nano \
    curl \
    wget \
    telnet \
    dnsutils \
    htop \
    tree \
    openssh-server \
    pkg-config \
    libmysqlclient-dev
    && rm -rf /var/lib/apt/lists/*
```