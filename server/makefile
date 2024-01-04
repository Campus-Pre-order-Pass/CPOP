
build:
	docker-compose down
	docker-compose up --build
# # run
# include script/makefiles/run/run_server.mk
# include script/makefiles/run/run_server_wsgi.mk

# # check 
# include script/makefiles/check/check_and_kill.mk

# # orther
# include script/makefiles/create_venv.mk
# include script/makefiles/install_dependencies.mk

# # celery
# include script/makefiles/celery/celery.mk


# # with wsgi
# run-wsgi:check_and_kill activate run_server_wsgi

# # 啟動test server 模式
# run:check_and_kill  run_server


# # 啟動虛擬環境
# act: activate

# # test case 
test: 
	./manage.py test Order.tests.TestAPIView.test_post_PayOrder

api-test:
	./manage.py test Order.tests.TestAPIView && \
	./manage.py test Shop.tests.TestAPIView && \
	./manage.py test MenuItem.tests.TestAPIView && \
	./manage.py test Customer.tests.TestAPIView && \
	echo "\033[32mAll tests passed.\033[0m"



command:
	./manage.py $(CMD)


migrate:
	python manage.py makemigrations
	python manage.py migrate



# django-q:
# 	python manage.py qcluster
# 	# python manage.py qmonitor
# 	# python manage.py qmonitor --port=8888


# # 啟動 celery 用 flower 監控
# start-flower: check_and_kill_5555
# 	celery -A Backend flower -l info --basic_auth=twtrubiks:password123

app:
	./python manage.py startapp $(APP)
	echo "# This is $(APP) Swagger configuration" > $(APP)/drf.py

dumpdata:
	./manage.py dumpdata Shop > static/json/Shop.json
	./manage.py dumpdata MenuItem > static/json/MenuItem.json
	./manage.py dumpdata Customer > static/json/Customer.json
	./manage.py dumpdata Order > static/json/Order.json


loaddata:
	./manage.py loaddata  static/json/Shop.json
	./manage.py loaddata  static/json/MenuItem.json
	./manage.py loaddata  static/json/Customer.json
	./manage.py loaddata  static/json/Order.json

# loaddata:
# 	./manage.py loaddata static/json/production_data.json

# dumpdata:
# 	./manage.py dumpdata >  static/json/production_data.json

.PHONY: api-test dumpdata loaddata  migrate app
 