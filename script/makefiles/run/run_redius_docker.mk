# Makefile

run-redius-docker:
    # docker stop redis-lab || true
    # docker rm redis-lab || true
    docker run --name redis-lab -p 6379:6379 -d redis
