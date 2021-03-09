# Animegan_Paddle

> Docker version API for AnimeGANv2!

The webapp is deployed Divio-Online here - https://animegan-paddle.us.aldryn.io/

The webapp is deployed Divio-Test - https://animegan-paddle-stage.us.aldryn.io/

The webapp is deployed Aliyun Severless here - 

---

## What is this?

- Original address of the project[AnimeGANv2](https://github.com/TachibanaYoshino/AnimeGANv2)
- The project used by this version[Animegan2-Pytorch](https://github.com/bryandlee/animegan2-pytorch)


### Explain
AnimeGANv2(Look at the picture)

<img src="https://pcdn.wxiou.cn/20210222172914.jpg" width="960"> &nbsp; 
<img src="https://pcdn.wxiou.cn/20210222172934.jpg" width="960"> &nbsp; 
<img src="https://pcdn.wxiou.cn/20210222172953.jpg" width="960"> &nbsp; 

## Compiled project on [hub.docker.com](https://hub.docker.com/)

- [Normal version](https://hub.docker.com/layers/138992015/literature/animegan-paddle/latest/images/sha256-4440352090b0c978b41825c5118217679df080e444c9b41176b553cf0912aaf6?context=explore)
- [GPU version](https://hub.docker.com/layers/138991480/literature/animegan-paddle/gpu/images/sha256-53449d6fb2fb4cd7e0bcba4ee2b7abe01dba8ea4250cabbfca391b948f6c6621?context=explore)
- [Heroku version](https://hub.docker.com/layers/138990300/literature/animegan-paddle/heroku/images/sha256-bd4c78b9cd7abe2afd4f0e325eb42f420e79ce393b263514e43fd4491b971252?context=explore)

## Build
> Make sure you have `docker` installed
1. Clone the Animegan repository:
    ```
    git clone https://github.com/LiteraturePro/Animegan_Paddle.git
    cd Animegan_Paddle
    ```
2. Input command to build image：
    ```
    docker build -t animegan .
    ```
    - I also provided the compilation command for `Heroku`, just replace the last command of dockerfile file with each other,
    - For general
    ```
    CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
    ```
    - For heroku
    ```
    CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
    ```
3. Running image (You can specify the running port yourself)：
    ```
    docker run -p 8080:8080 animegan
    ```
## Install
> Make sure you have `docker` installed


I have built the image and can install it directly. The installation command is as follows(You can specify the running port yourself)：
- For general
    ```
    docker pull literature/animegan-paddle:latest
    docker run -p 8080:8080 literature/animegan-paddle:latest
    ```
- For heroku
    ```
    docker pull literature/animegan-paddle:heroku
    ```
    [Please see the specific tutorial for installing container application in heroku](https://github.com/LiteraturePro/Cartoonize#using-heroku)

- For Aliyun Serverless
    ```
    docker pull literature/animegan-paddle:sf
    ```
    [Please see the specific tutorial for installing container application in Aliyun Serverless](https://github.com/LiteraturePro/Cartoonize#using-aliyun-severless)
Now your service has started to run, but it runs on the local port. If you need to realize the external network call, you need to act as an agent to proxy the service to your domain name，

## Use
> The call I have shown is based on the agent I have done. If you need to call it, you need to do it yourself

- provided that you have installed `docker`. After you deploy correctly, both `GET` and `POST` requests can be accessed. The actual display is as follows
  - `Interface`: `http://your domain/api` or `http://127.0.0.1:8080/api` can be accessed.
  - `Parameter`: image  `value`: a picture
  - `Return value`: the base64 data stream after processing the image
![](https://pcdn.wxiou.cn/20210221141131.png)
![](https://pcdn.wxiou.cn/20210221141230.png)


## Other
  Thanks for the work of the original author and the revised author. If you like, please give a `star`.

