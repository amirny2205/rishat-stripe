выполнение тестового https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

## инструкция по запуску:
я включил .env в целях упрощения, здесь так можно т.к. это не продовый проект
python manage.py makemigrations --settings=config.settings.local
python manage.py migrate --settings=config.settings.local  
python manage.py createsuperuser --settings=config.settings.local
python manage.py runserver --settings=config.settings.local
идем в http://127.0.0.1:8000/admin/ и создаём item'ы
