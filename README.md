# django-api-tools

## Detail

Ce projet django sera un projet pour visualiser les données d'API, s'inspirant de [Postman](https://www.postman.com)

## Instalation
### Virtual Env
> Entrez les commandes suivantes dans le terminal à la racine du projet
> ou exécutez le fichier **initialiser.sh**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd api-tool/
python3 manage.py migrate
python3 manage.py runserver
```

### Lancement du site
> Entrez les commandes suivantes dans le terminal à la racine du projet
> ou exécutez le fichier **lancer.sh**
>> vous pouvez ajouter un numero après lancer.sh pour préciser le port : ./lancer.sh 7 => port 7000 
```
source venv/bin/activate
cd api-tool/
python3 manage.py runserver
```

## Utilisation