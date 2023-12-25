# Detect operating system
ifeq ($(OS),Windows_NT)
	VENV_CREATE = python -m venv venv
	VENV_ACTIVATE = .venv\Scripts\activate
	SOURCE =
else
	VENV_CREATE = python3 -m venv venv
	VENV_ACTIVATE = .venv/bin/activate
	SOURCE = .
endif

# Activate virtual environment in the current directory
create_venv_activate:
	cd $(SOURCE) && . $(VENV_ACTIVATE)

# Check if virtual environment already exists
create_venv_check:
	@if [ -e $(VENV_ACTIVATE) ]; then \
		echo "Virtual environment already exists."; \
	else \
		make create_venv; \
	fi

# Create virtual environment if it doesn't exist
create_venv:
	$(VENV_CREATE)
