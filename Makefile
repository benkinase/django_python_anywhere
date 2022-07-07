superuser:{
	benji:123456 => dev
# 	tilapea:123456
#   benkinase::justcoding
}


create_env:
     python -m  venv env-name 
	 virtualenv env_name
	 
activate env:
    source venv/Scripts/activate

use requirment.tx template:
    pip install -r requirements.txt

de-activate env:
    deactivate

run-server:
	python manage.py runserver

remove db:
rm -f db.sqlite3
rm -r store/migrations

show-migrations:
	python manage.py showmigrations

reset-migrations:
	./reset-migrations.sh

clear-migration-history:
	python manage.py migrate --fake courses zero

migrate:
dev:
	python manage.py makemigrations or python manage.py makemigrations app_name
	python manage.py migrate
prod:
    python manage.py migrate (applies the migration file committed from dev)

test:
	python manage.py test