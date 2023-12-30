
# run
include makefiles/run/run_server.mk
include makefiles/run/run_server_wsgi.mk

# check 
include makefiles/check/check_and_kill.mk

# orther
include makefiles/create_venv.mk
include makefiles/install_dependencies.mk

# celery
include makefiles/celery/celery.mk


# with wsgi
run-wsgi:check_and_kill activate run_server_wsgi

# 啟動test server 模式
run:check_and_kill  run_server


# 啟動虛擬環境
act: activate

# test case 
test: 
	./manage.py test Order.tests.TestPayOrderAPIView

command:
	./manage.py line


migrate:
	python manage.py makemigrations
	python manage.py migrate


django-q:
	python manage.py qcluster
	# python manage.py qmonitor
	# python manage.py qmonitor --port=8888



# 啟動 celery 用 flower 監控
start-flower: check_and_kill_5555
	celery -A Backend flower -l info --basic_auth=twtrubiks:password123
