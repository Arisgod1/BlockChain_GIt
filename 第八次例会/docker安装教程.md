```
# 更新软件包索引
sudo apt update

# 升级已安装的包（可选，推荐执行）
sudo apt upgrade -y

```

# 卸载旧版本的docker

sudo apt remove -y docker docker-engine docker.io containerd runc

## 安装仓库依赖包

sudo apt install -y ca-certificates curl gnupg lsb-release

## 删除原有源文件
sudo rm -f /etc/apt/sources.list.d/docker.list
## 添加腾讯云源
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/docker.gpg] https://mirrors.cloud.tencent.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
## 导入腾讯云 GPG 密钥
curl -fsSL https://mirrors.cloud.tencent.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg
## 更新源并安装
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io

## 安装docker引擎

```
# 再次更新包索引（加载新添加的Docker仓库）
sudo apt update

# 安装Docker核心组件（Docker Engine + containerd + Docker Compose）
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

```


## 启动docker并设置开机自启
```
# 启动Docker服务
sudo systemctl start docker

# 设置开机自动启动Docker
sudo systemctl enable docker

# 检查Docker服务状态（确认是否运行正常）
sudo systemctl status docker

```


## 将普通用户加入docker组(可选)
```
# 将当前用户加入docker组（替换为你的用户名，如ubuntu）
sudo usermod -aG docker $USER

# 刷新组权限（无需重启，立即生效）
newgrp docker

```