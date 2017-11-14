clean:
	find . -name '*.pyc' -delete

update: clean
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py collectstatic --noinput

run: clean
	python manage.py runserver

test: clean
	python manage.py test --settings=project.settings.test

circle-test:
	python manage.py collectstatic --noinput --settings=project.settings.test
	tox

coverage: clean
	coverage run --source=. manage.py test --settings=project.settings.test
	coverage html
	coverage report
	@echo "HTML report available in 'htmlcov/' directory."
