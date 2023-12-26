# run
include ./makefiles/run/run_redius_docker.mk

ifeq ($(OS),Windows_NT)
    # Windows
    SERVER_EXECUTABLE = .\server.exe
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Darwin)
        # macOS
        SERVER_EXECUTABLE = ./server
    else
        # Assume Linux (add more conditions if needed)
        SERVER_EXECUTABLE = ./server
    endif
endif


# 執行server
runser:
	cd $(SERVER_EXECUTABLE) ; $(MAKE) run

# 更新server 或是 web 套件
# update:


redius: run-redius-docker

# 正式啟動
all:
    docker-compose up


