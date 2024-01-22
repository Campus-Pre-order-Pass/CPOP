include script/makefiles/venv.mk

include script/makefiles/run/run_server.mk
include script/makefiles/check/check_and_kill.mk

# docker
include script/makefiles/docker/docker.mk

PATH_DIR = script/shell

# Set the path to the directory containing your scripts
SCRIPTS_DIR = script/shell

DOCKER_NAME = docker-compose
DEOCKER_TESTS_DIR = docker/test


.DEFAULT_GOAL := help

help:
	@echo "make build -> build proj"
	@echo
	@echo "build-test  -> build test docker-compose"
	@echo
	@echo "make runser -> run local proj"
	@echo
	@echo "make build-test -> run redius gitLab ...tools"

# build: venv-check 

runser: venv-check  check_and_kill run_server

build-server: venv-check check_and_kill build_server

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


#  test =================================================================


build-test:
	cd ./docker/test && docker-compose up -d



test-re-build: docker-rm docker-build

test-update:
	cd ./docker/test && $(DOCKER_NAME) down
	cd ./docker/test &&$(DOCKER_NAME) build
	# $(DOCKER_NAME) up -d
	cd ./docker/test && $(DOCKER_NAME) up 

test-stop:
	cd $(DEOCKER_TESTS_DIR) && $(DOCKER_NAME) down 




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


gui:
	python3 cli.py gui

gui-build:
	pyinstaller --onefile --add-data "./conf/gui.json:./conf" --add-data "./script/GUI/logo.png:./script/GUI" gui.py



# stop-rm:
# 	docker rm -f $$(docker ps -aq)


# docker run -d -p 8000:8000 --name cpop-server-1 s990093/cpop-server:latest

re-docker:
	net start docker


.PHONY: give_execute_permission build
