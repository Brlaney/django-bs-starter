# Django-Bootstrap-boilerplate

The goal of this repository it to provide users with an easily customizable Django web-app that's styled with the latest stable Bootstrap (v4.6).

## Let's get started

### Clone this repo & change directories

`git clone https://github.com/brlaney42/Django-Bootstrap-Boilerplate`

`cd django-bootstrap-boilerplate`

You can use a different method to starting a virtual environment if you prefer

`virtualenv <your-env>`

#### Windows terminal

`<your-env>\scripts\activate.bat`

![Desktop Screenshot 2021 05 24 - 09 09 50 56](https://user-images.githubusercontent.com/64326462/119365246-c0696a80-bc7d-11eb-9215-fc6a01cb6d9a.png)

</br>

### Project folder structure

- **config** (*project-name*)
- **pages** (*application-name*)
- **static** (*static files location*)
- **virtual-env** (*example virtual environment name*)
- *manage.py*
- *requirements.txt*
  
</br>

- **config**
  - **__pycache__**
  - __init__.py
  - asgi.py
  - settings.py
  - urls.py
  - wsgi.py
- **pages**
  - **__pycache__**
  - **migrations**
  - **templates**
    - **components**
      - *footer.html*
      - *navbar.html*
    - pages
      - *base.html*
      - *index.html*
  - __init__.py
  - admin.py
  - apps.py
  - models.py
  - tests.py
  - urls.py
  - views.py
- **virtual-env**
- *manage.py*
- *requirements.txt*
  
### **Note**

In the projects core directory, where **manage.py** & **requirements.txt** are located, you will also find the following I did not include above:

- .gitignore
- README.md
- LICENSE

</br>

## Links to latest (stable) releases **05/24/2021**

[Django v3.2.3](https://www.djangoproject.com/)
</br>

[Bootstrap v5.0.1](https://getbootstrap.com/docs/5.0/getting-started/download/)
