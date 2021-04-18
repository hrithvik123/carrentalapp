# JHS Car Rental

JHS Car Rental is a car rental service webapp built using Django. Below is everything you need to get started with the JHS Car Rental app.

## Table of contents

- [Running Locally](#running-locally)
  - [Installing python](#installing-python)
  - [Installing Django](#installing-django)
  - [Running JHS Car rental](#running-jhs-car-rental)
- [Contributor documentation](#contributor-documentation)
  - [Folder/File explanation](#folderfile-explanation)
    - [Project](#project)
    - [Apps](#apps)
      - [Users](#users)
      - [Integrations](#integrations)

## Running Locally

### Installing python

You will first need to install [python 3](https://www.python.org/downloads/) and `pip`. If you have done this successfully then on windows you should be able to run:

<details>
 <summary>Windows</summary>
	<code>python --version</code> and <code>pip --version</code>
</details>
<details>
 <summary>MacOS/Linux</summary>
	<code>python3 --version</code> and <code>pip3 --version</code>
</details>

You should see `Python 3.X.X` (number may be different but anything 3.8+ is fine) and
`pip 21.0.1 from c:\users\YOUR_USERNAME\appdata\local\programs\python\python39\lib\site-packages\pip (python 3.X)` (Just make sure the python version number in brackets matches the number from above) respectively

### Installing Django

If you have never used Django I would highly recommend looking into either the [official tutorial](https://www.djangoproject.com/start/), or the [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction), or the [video crash course]([(2) Python Django Crash Course - YouTube](https://www.youtube.com/watch?v=e1IyzVyrLSU)).

To install Django run:

<details>
 <summary>Windows</summary>
	<code>pip install django</code>
</details>
<details>
 <summary>MacOS/Linux</summary>
	<code>pip3 install django</code> or <code>sudo pip3 install django</code>
</details>

To make sure it's installed properly run `django-admin help` and you should see:

```bash
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    ... # list continues
```

### Running JHS Car rental

To make sure you all required dependencies installed, run `pip install -r requirements.txt`
To setup the database, run `python manage.py makemigrations` followed by `python manage.py migrate`
Next step is to create an admin to access the admin panel. To do so, run `python manage.py createsuperuser` and follow the instructions.
To run the project simply run `python manage.py runserver` and you can naviagte to [http://localhost:8000](http://localhost:8000) to see the server.

## Contributor documentation

### Folder/File explanation

At the top level there are a few files `README.md` (what you're reading), `manage.py` and `.gitignore`. `manage.py` does not need to be touched, it is the file that runs when you start the app, and is setup by default from Django. `.gitignore` is used to ignore files that we don't need in the git repo (caches of files etc.).

The rest of the folders are the actual code. Django itself is structured into an app/project distinction, so I will tailor the rest of the documentation around that.

#### Project

everything inside `/carrentalapp` is the "project". Amoung other things this contains:

- The list of installed apps
- The global URL list
- The settings that are global across all apps
- Boilerplate file for running the server (wsgi and asgi)

You can think of this folder as mainly the server configuration, and each app as more of a particular peice of functionality.

#### Apps

Each app is essentially a particular peice of functionality that includes:

- The backend code (the models that drive the views that render the frontend templates)
- The frontend templates associated with the functionality
- Any additional URL routing changes that need to be made or URL patterns that need to be defined

There are a few apps inside the project, and they are detailed below.

##### users

This app contains the models, views and templates associated with getting the user logged in and accessing their data. One thing to note here is that the current homepage for the site exists here (in `/users/templates/users/index.html`)

## License

[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)
