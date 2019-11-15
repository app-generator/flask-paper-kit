# [Flask Paper Kit](https://appseed.us/apps/flask-apps/flask-paper-kit)

**[Open-Source Web App](https://appseed.us/apps/flask-apps/flask-paper-kit)** coded in **Flask Web Framework** on top of **Paper Kit** design, crafted by Creative-Tim agency. Features:

- SQLite
- SQLAlchemy ORM
- Session-Based authentication (via **flask_login**)
- Forms validation
- **License MIT**

<br />

![Flask Paper Kit - Open-Source Web App coded in Flask.](https://raw.githubusercontent.com/app-generator/static/master/products/flask-paper-kit-intro.gif)

## Setup the environment
---

In order to use the boilerplate, we need [Python3](/what-is/python/) and `virtualenv` python library.

<br />

> *Note*: **Python2 is not supported**, the EOL of this version announced [here](https://www.python.org/doc/sunset-python-2/). In order to use our kits, please migrate to Pyhton3. Thank you!

<br />

```bash
$ # Test the Python install
$ python --version
$ Python 3.7.2
$
$ # install Virtualenv using PIP
$ pip3 install virtualenv
```

<br />

## Build from [sources](https://github.com/app-generator/flask-paper-kit)
---

<br />

```bash
$ # 1. Get the code
$ git clone https://github.com/app-generator/flask-paper-kit.git
$ cd flask-paper-kit
$
$ # Install modules using a virtualenv (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Install modules using a virtualenv (Windows based systems)
$ # virtualenv --no-site-packages env
$ # \env\Scripts\activate.bat
$ 
$ # 2. Install requirements
$ pip3 install -r requirements.txt
$
$ # 3. Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Create SQLite database using the Flask console
$ flask shell
>> from app import db
>> db.create_all()
>> quit()
$ # SQLite database.db should be created in the app folder:
$ # app\database.db
$
$ # 4. Run the application
$ flask run --host=0.0.0.0
$
$ # 5. Go to http://127.0.0.1:5000/, create an account and log in
```

<br />

## Project Structure

---

The boilerplate code is built with a modular structure that follows the recommended pattern used by many open-source projects. The most important files / directories are listed bellow:

- [run.py](https://github.com/app-generator/flask-paper-kit/blob/master/run.py)
- [app /](https://github.com/app-generator/flask-paper-kit/tree/master/app)
- [app / __init__.py](https://github.com/app-generator/flask-paper-kit/blob/master/app/__init__.py)
- [app / views.py](https://github.com/app-generator/flask-paper-kit/tree/master/app/views.py)
- [app / models.py](https://github.com/app-generator/flask-paper-kit/tree/master/app/models.py)

<br />

```bash
< ROOT > - Flask Paper Kit        # application root folder
    |
    |--- app/__init__.py          # application constructor  
    |--- app/views.py             # implement app routing
    |--- app/models.py            # define app models
    |--- app/forms.py             # forms used for login and registration
    |
    |--- requirements.txt         # App Requirements
    |
    |--- run.py                   # bootstrap the app
    |
    |-----------------------------
```

<br />

## Support

---

- Free support via eMail < [support @ appseed.us](https://appseed.us/support) > and [Github](https://github.com/app-generator/flask-paper-kit/issues/)
- 24/7 Live Support via [Discord](https://discord.gg/fZC6hup) for paid plans and commercial products.

<br />

## Links & Resources

- [Flask Paper Kit](https://appseed.us/apps/flask-apps/flask-material-kit) - Product page
- [Flask Paper Kit](https://docs.appseed.us/apps/flask-apps/flask-material-kit) - documentation
- [Flask Framework](https://www.palletsprojects.com/p/flask/) - Offcial website
- [Flask - Open-Source Boilerplates](https://dev.to/sm0ke/flask-boilerplate-open-source-apps-built-with-automation-tools-4925) - A popular article published on Dev.to platform

<br />

---
[Flask Paper Kit](https://appseed.us/apps/flask-apps/flask-paper-kit) - provided by **AppSeed**
