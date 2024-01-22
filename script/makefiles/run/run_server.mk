# Run Django server
run_server: 
	# cd Server && python manage.py runserver 0.0.0.0:8000  --settings=Backend.settings_dev
	cd Server && python manage.py runserver 0.0.0.0:8000  



run_test_server: 
	cd Server && python manage.py runserver 0.0.0.0:8000  --settings=Backend.settings_test


build_server:
	cd Server && python manage.py runserver 0.0.0.0:8000  --settings=Backend.settings_dev