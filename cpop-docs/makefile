PORT = 9001
check_and_kill:
	@if lsof -i :$(PORT); then \
		echo "Port $(PORT) is already in use. Killing the process..."; \
		lsof -ti :$(PORT) | xargs kill -9; \
	fi


run:
	yarn run start --host 0.0.0.0


all: check_and_kill run
