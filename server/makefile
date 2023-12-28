
# run
include makefiles/run/run_server.mk
include makefiles/run/run_server_wsgi.mk

# check 
include makefiles/check/check_and_kill.mk

# orther
include makefiles/create_venv.mk
include makefiles/install_dependencies.mk


# with wsgi
run-wsgi:check_and_kill activate run_server_wsgi

# 啟動test server 模式
run:check_and_kill  run_server


# 啟動虛擬環境
act: activate

# test case 
test: 
	./manage.py test Order.tests.OrderPayTest


# all:  install_dependencies run_server


# Detect operating system
# ifeq ($(OS),Windows_NT)
# 	VENV_CREATE = python -m venv venv
# 	VENV_ACTIVATE = .venv\Scripts\activate
# 	SOURCE = source
# else
# 	VENV_CREATE = python3 -m venv venv
# 	VENV_ACTIVATE = .venv/bin/activate
# 	SOURCE = .
# endif

# # Activate virtual environment in the current directory
# activate:
# 	cd $(SOURCE) && . $(VENV_ACTIVATE)

# # Check if virtual environment already exists
# check_venv:
# 	@if [ -e $(VENV_ACTIVATE) ]; then \
# 		echo "Virtual environment already exists."; \
# 	else \
# 		make create_venv; \
# 	fi

# # Create virtual environment if it doesn't exist
# create_venv:
# 	$(VENV_CREATE)

# # Install dependencies
# install: activate
# 	pip install -r requirements.txt

# # Check and kill the process on port 8000
# check_and_kill:
# 	@if lsof -i :8000; then \
# 		echo "Port 8000 is already in use. Killing the process..."; \
# 		lsof -ti :8000 | xargs kill -9; \
# 	fi

# # Run Django server
# run: check_and_kill activate
# 	python manage.py runserver 0.0.0.0:8000

# # Define 'all' target to check venv, install, and run
# all: check_venv activate install run


