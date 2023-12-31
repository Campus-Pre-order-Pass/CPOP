include script/makefiles/create_venv.mk 


PATH_DIR = script/shell

# Set the path to the directory containing your scripts
SCRIPTS_DIR = script/shell

build:give_execute_permission activate
# cd $(PATH_DIR)/run &&  ./enter_venv.sh

# Target to give execute permission to all shell scripts in the directory
give_execute_permission:
	chmod +x $(SCRIPTS_DIR)/*/*.sh



.PHONY: give_execute_permission
