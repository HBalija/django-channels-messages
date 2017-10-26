clean:
	find . -name '*.pyc' -delete

run:
	python manage.py runserver

test: clean
	python manage.py test --settings=project.settings.test
