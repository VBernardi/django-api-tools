python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd api-tool/
python3 manage.py migrate
python3 manage.py runserver