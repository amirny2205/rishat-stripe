выполнение тестового https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

## инструкция по запуску:
я включил .env в целях упрощения, здесь так можно т.к. это не продовый проект

python -m venv env

source ./env/bin/activate на линуксе, ./env/Scripts/activate на виндовс

pip install -r requirements.txt

python manage.py makemigrations --settings=config.settings.local

python manage.py migrate --settings=config.settings.local  

загружаем fixture, там 3 объекта.

python manage.py loaddata fixtures/Item_01.json --settings=config.settings.local

python manage.py runserver --settings=config.settings.local

заходим на http://127.0.0.1:8000/item/1-3/, всё должно работать.
