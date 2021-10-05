sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd core2/
python manage.py test profiles_api/tests
celery -A core worker -l debug -c 3