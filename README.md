# newsletter-manager

### A basic newsletter api manager with Django REST framework
## Running
### - Clone this repository
### - cd into newsletter-manager directory
```bash
cd newsletter-manager/
```
- ## With docker
### - Create .env and provide token for external api
```bash
(venv) touch .env
```
### .env sample
```
SECRET_KEY = mysecret
DEBUG = 1
ALLOWED_HOSTS=localhost
TOKEN=my_token
```
### Build and spin docker containers
```bash
(venv) docker-compose up --build
```

- ## Without docker
### - Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```
### - Create .env and provide redis credentials for celery (default is localhost)
### You can still use any other broker
```bash
(venv) touch .env
```
### .env sample
```
SECRET_KEY = mysecret
DEBUG = 1
ALLOWED_HOSTS=localhost

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
TOKEN=my_token
```
### - Run migrations and run server
```bash
(venv) python manage.py migrate
(venv) python manage.py runserver
```
### - Run celery worker (make sure redis is spinned before)

Linux:
```bash
(venv) celery -A config worker -l INFO
```

Windows10+ : At the moment of writing this prefork(--pool=processes by default) concurrency doesn't work on windows10+, set --pool to solo or threads
```bash
(venv) celery -A config worker -l INFO --pool=solo
```
### Demo version available on [newsletter-manager](https://).

## Next steps :
- [x] Dockerize
- [ ] Testing
- [ ] Improve clients filtering