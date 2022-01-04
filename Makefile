build-no-cache:
	docker build . --no-cache -t fideliza-mais_web:latest

bash:
	docker-compose run web bash

makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py makemigrations

test:
	docker-compose run web python manage.py test

start:
	docker-compose up -d

close:
	docker-compose down
