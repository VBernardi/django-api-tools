source venv/bin/activate
cd api-tool/
if [ ! $# -eq 0 ]; then
    python3 manage.py runserver 127.0.0.1:"$1"000
else
    python3 manage.py runserver
fi