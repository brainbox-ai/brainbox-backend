# brainbox-backend 

Backend API built using Django, Django REST Framework, and Openai

Setup Instructions:

1. Add environment file and keys

Create .env file in root directory and declare two variables. Generate Django SECRET_KEY by running below command in terminal and copy value into .env file.

```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Obtain OPENAI_KEY from https://platform.openai.com/account/api-keys and copy into .env file. .env file should look like:

```
SECRET_KEY = "..."

OPENAI_KEY = "..."
```

2. Create Virtual Environment

From root directory, run the following commands. This will create a "env" folder. If you choose to name the folder to something else, ensure .gitignore is updated accordingly

```
python -m env
source env/bin/activate
```

3. Install app dependencies

```
pip install -r requirements.txt
```

4. Migrations and Start Server
 
Navigate into brainbox_api, run migrations and start server

```
cd brainbox_api
python manage.py migrate
python manage.py runserver
```

Test api runs correctly by navigating to http://localhost:8000
