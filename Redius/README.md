# 使用 Docker 運行 Redis

## 下載 Redis Docker Image

首先，在 Docker 中透過 `docker pull` 指令取得 Redis image 檔。

```bash
docker pull redis
```

```bash
docker run --name redis-lab -p 6379:6379 -d redis
```

# https://marcus116.blogspot.com/2019/02/how-to-run-redis-in-docker.html
