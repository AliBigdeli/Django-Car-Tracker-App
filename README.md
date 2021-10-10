<h1 align="center">Django GPS Car Tracker App</h1>
<h3 align="center">this is a simple car tracking server as in backend and front to control your car locations </h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="sqlite" width="90" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>
<img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/>
</p>


### Overview
- [Overview](#overview)
- [demo](#demo)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [options](#options)
- [Reformat and check](#reformat-and-check)
- [Heroku setup](#heroku-setup)
  - [development](#development)
  - [production](#production)
- [Database schema](#database-schema)
- [Todo](#todo)
- [Bugs or Opinion](#bugs-or-opinion)


### demo
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/136673813-47b9bf4a-eee7-42d1-8aaf-85832cb3c534.gif" width="300"/>
</p>

### Features
- Django LTS
- Class Based views (ApiView)
- Django RestFramework
- User authentication
- Black
- Flake8
- Responsive Design
- Bootstrap5
- heroku
- postman exported api



### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/alibigdeli/Django-Car-Tracker-App
```

### Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```bash
python -m venv venv
```

Make sure to install the dependencies of the project through the requirements.txt file.
```bash
pip install -r requirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python manage.py migrate
```

### options
Project it self has the user creation form but still in order to use the admin you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
python manage.py createsuperuser
```

And lastly let's make the App run. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
python manage.py runserver
```

Once the server is up and running, head over to http://127.0.0.1:8000 for the App.

### Reformat and check
If you want your code to be check by pep8 and all the guide lines, there are two packages added to requirements in order to check and reformat code.
you can use it by this command:
```bash
black -l 79 . && flake8
```

### Heroku setup
1 - Create an account in heroku
- <a>https://id.heroku.com/login</a>

2 - Download and install heroku cli
- <a>https://devcenter.heroku.com/articles/heroku-cli</a>- 

3 - login to your heroku account
- you will be redirected to heroku web page to login
```bash 
heroku login
```


#### development

in linux you might run into problem with install psycopg2 and here is a fix to that, just install theses packages and then re install the python package.

Note: i am not sure if you will ran in to problem with windows or not but still linux is good to go.

```bash
sudo apt install python3-dev libpq-dev
pip install psycopg2
```
after installing all dependencies all you have to do is to run the server.
```bash
heroku local
```

or

you can simply run "manage.py runserver" as normal project but dont forget to install dependencies.
#### production
In order to use this repo for production in heroku service, you have to push the repo to your heroku app.

1- create an app:
```bash
heroku create APP_NAME
```
2- setup git directory for repo (go to your directory)
```bash
git init .
git add .
```
3 - deploy to heroku app
```bash
git commit -am "Initial commit"
git push heroku master
```

Note: you can use the one click deploy on the top of the readme too
### Database schema
A simple view of the project model schema.
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/136673503-c8b0d232-db03-4236-83a5-e40cf07baf31.png" alt="database schema" width="600"/>
</p>

### Todo
- [x] add heroku config files
- [x] complete the documentation
- [x] add one click deploy mechanism
- [ ] add google api as env to configs
- [ ] test post data on gprs module
- [ ] create a video tutorial

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
