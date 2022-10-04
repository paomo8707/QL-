
#### 🚩 一键安装青龙面板命令


#### 🚩 全自动提交助力码到互助池


- 使用方式
```sh
docker exec -it qinglong bash -c "task /ql/jd/1-5.sh && python3 /ql/jd/1-5.py"
docker exec -it qinglong bash -c "task /ql/jd/6-10.sh && python3 /ql/jd/6-10.py"
docker exec -it qinglong bash -c "task /ql/jd/11-15.sh && python3 /ql/jd/11-15.py"
docker exec -it qinglong bash -c "task /ql/jd/16-20.sh && python3 /ql/jd/16-20.py"
docker exec -it qinglong bash -c "task /ql/jd/21-25.sh && python3 /ql/jd/21-25.py"
docker exec -it qinglong bash -c "task /ql/jd/26-30.sh && python3 /ql/jd/26-30.py"
docker exec -it qinglong bash -c "task /ql/jd/31-35.sh && python3 /ql/jd/31-35.py"

```
#
- 为防止系统没安装curl，使用不了一键命令，使用一键安装青龙面板命令之前先执行一次安装curl命令

- 安装curl请注意区分系统，openwrt千万别另外安装curl，openwrt本身自带了，另外安装还会用不了
#

- 使用root用户登录ubuntu或者debian系统，后执行以下命令安装curl
```sh
apt -y update && apt -y install curl
```

- 使用root用户登录centos系统，后执行以下命令安装curl
```sh
yum install -y curl wget
```
#
- 国外鸡地址，执行下面一键命令安装青龙+依赖+任务+maiark自由选择（安装完毕后再次使用命令可以对应用进行升级）
```sh
bash -c "$(curl -fsSL https://raw.githubusercontent.com/paomo8707/QL-/main/lang1.sh)"
```
- 国内鸡地址，执行下面一键命令安装青龙+依赖+任务+maiark自由选择（安装完毕后再次使用命令可以对应用进行升级）
```sh
bash -c "$(curl -fsSL https://ghproxy.com/https://raw.githubusercontent.com/paomo8707/QL-/main/lang1.sh)"
```


## 第二步

#### 🚩 docker版本fdd
```
docker run -dit \
  -v $PWD/fdd/config:/fdd/config \
  -v $PWD/fdd/mysql:/fdd/mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -e MYSQL_DATABASE=emotion \
  -e SERCET_KEY=abcd \
  -p 8088:80 \
  -p 3301:3306 \
--name fdd \
--restart always \
eyesouls/fdd:v2.0
```
- 
#### 🚩 单独安装某项的一键脚本


- 一键单独安装docker
```sh
bash -c "$(curl -fsSL https://ghproxy.com/https://raw.githubusercontent.com/shidahuilang/QL-/main/docker.sh)"
```

- 一键安装单独青龙的依赖
```sh
docker exec -it qinglong bash -c  "$(curl -fsSL https://ghproxy.com/https://raw.githubusercontent.com/shidahuilang/QL-/main/npm.sh)"
```

- 傻妞docker版交互模式 ```docker attach sillygirl```
```
docker run \
    -itd \
    --name sillygirl \
    --restart always \
    -v  "$(pwd)"/sillyGirl:/etc/sillyGirl \
    mzzsfy/sillygirl:latest
```    



```

## 感谢！


> [`shidahuilang`]


