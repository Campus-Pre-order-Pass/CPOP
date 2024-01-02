include script/makefiles/venv.mk

include script/makefiles/run/run_server.mk
include script/makefiles/check/check_and_kill.mk

# docker
include script/makefiles/docker/docker.mk

PATH_DIR = script/shell

# Set the path to the directory containing your scripts
SCRIPTS_DIR = script/shell

DOCKER_NAME = docker-compose
.DEFAULT_GOAL := help

help:
	@echo "make build -> build proj"
	@echo
	@echo "make runser -> run local proj"
	@echo
	@echo "make build-test -> run redius gitLab ...tools"

# build: venv-check 

runser: venv-check  check_and_kill run_server

VENV_NAME := .venv

test:
	. $(VENV_NAME)/bin/activate && \
	python -V && \
	cd server && python manage.py runserver 0.0.0.0:8000



# Target to give execute permission to all shell scripts in the directory
give_execute_permission:
	chmod +x $(SCRIPTS_DIR)/*/*.sh

build:
	docker-compose down
	docker-compose up --build

build-test:docker-build

test-re-build: docker-rm docker-build

test-update:
	$(DOCKER_NAME) down
	$(DOCKER_NAME) build
	# $(DOCKER_NAME) up -d
	$(DOCKER_NAME) up 


server-cmd:
	docker exec -it cpop-server-1 python manage.py $(CMD)


test-port:
	@nc -zv localhost 6379 || echo "Redis is not running on port 6379"
	@nc -zv localhost 5672 || echo "RabbitMQ is not running on port 5672"
	@nc -zv localhost 15672 || echo "RabbitMQ Management Interface is not running on port 15672"


stop: 
	./script/test/docker-compose down

# 停止所有images
docker-stop-all:stop-all



.PHONY: give_execute_permission build
