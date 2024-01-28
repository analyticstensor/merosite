# Merosite Web Application designed with Django Web Framework

## Introduction
Merosite is a simple web application built with Django web framework. In devanagari script, `mero` means `my`. So, merosite means mysite.

## Features
### Custom User Authentication and Authorization
It has custom user authentication and authorization implemented via Django authentication system.
User can sign up with valid email address.
* User can signup, login/logout.
* User can view and update their profile.
* User can change password.
* User can reset password when password was forgotten.

### Admin Interface
It has default built-in admin interface provided by Django. User logged as `superuser` or `admin` can manage other users and well as register new user, change user information, activate/deactivate user via admin page. Registered model such as user, and contact can be viewed from admin page.

### Contact Page
The contact page facilitate logged user as well as visitor to send their comments/queries to site administrator. An email notification will be send to user for valid email only. It uses `smtp` to send an email. Contact information will also be stored `contact` table. When user is logged then full name and email will be automatically retrieved from user table.

### Logging 
An application logs as well as some user interaction log will be stored into `logs` directory.

## Prerequisite
Make sure you have latest version(>=3.12) of Python.

1. Install any Django supported database. _This site uses MySQL database._
    * Create same database user, and password defined in environment variable file stored at `~/.merosite_env`
    * Login to database server either from CLI or console.
    * Create `merosite` database.

    ```bash
    $ mysql -u username -p 
    Type your database password
    ```
    Once logged in create database.
    ```bash
    mysql> create database if not exists merosite;
    mysql> exit;
    ```
2. Create virtual environment and activate. [More info](https://docs.python.org/3/library/venv.html)

    * Using `venv`
    ```bash
    # create virtual environment
    $ python -m venv webapps_venv

    # activate virtural enironment
    $ source webapps_venv/bin/activate

    ```
    OR

    * Using `conda`
    ```bash
    # create virtual environment of Python 3.12
    $ conda create --name webapps_venv python=3.12

    # list virtual environment
    $ conda env list 

    # activate virtural enironment
    $ conda activate webapps_venv
    ```
3. Clone source code

    Clone source code from git repo.
    ```bash
    $ git clone https://github.com/analyticstensor/merosite.git
    $ cd merosite
    $ ls
    ```
    You should see all the directory and file listed in git.
4. Install required packages from requirement.txt
    ```bash
    pip install -r requirements.txt
    ```
    _*Note*_: If there is an error while installing `mysqlclient` then follow this [link](https://github.com/PyMySQL/mysqlclient/blob/main/README.md).

5. Create `~/.merosite_env` file that stores environment variable used in `setting.py`
Copy + Paste the below lines.
    ```
    # Database
    DB_NAME='dbname'
    DB_USER='username'
    DB_PASSWORD='password'
    DB_HOST='dbhostname'
    DB_PORT=port

    # Email
    EMAIL_HOST='emailhostname'
    EMAIL_HOST_USER='username'
    EMAIL_HOST_PASSWORD='password'
    EMAIL_PORT=port
    EMAIL_TIMEOUT=300
    DEFAULT_FROM_EMAIL='email_address'
    ```
    _*Note*_: Update the above information based on your database server and email provider settings.
6. Set environment variable from `.merosite_env` file
    ```bash
    $ export $(grep -v '^#' ~/.merosite_env | xargs)
    ```
7. Create required table objects define in `model.py`
    ```bash
    $ python manage.py makemigration
    $ python manage.py migrate authenticate
    $ python manage.py migrate contact
    $ python manage.py migrate
    ```
8. Create super user (aka admin) for web application
    ```bash
    # enter username, email, and password
    $ python manage.py createsuperuser
    ```
9. Run server to start web application. _*Note*_: Make sure your using same shell while running below command otherwise environment variable will not work.
    ```bash
    # use defaul port 8000
    $ python manage.py runserver
    ```
    _*Note*_: If port 8000 is not available or above command did not serve the application then run below command.
    ```bash
    # use port 8200
    $ python manage.py runserver http://127.0.0.1:8200
    ```    
10. Launch web application   
    Open the web browser and go to [local host](http://localhost:8000) or http://127.0.0.1:8000

    Open the web browser and go to [local host](http://localhost:8200) or http://127.0.0.1:8200

    _*Note*_: Admin console login is available at `/admin` in url e.g. http://localhost:8000/admin/ when port is 8000 or provide right port.
11. (Optional) Follow one of the deactive step below for cleaning the resources. It is used to deactivate and delete all the package which was installed earlier. You can only deactivate and keep the file for future usage. When you want to run application later follow the step from 6 to 10. 
* Deactivate the enviroment for `venv`
    ```bash
    # deactivate enironment 
    $ deactivate

    # delete virtual environment directory
    $ rm -rf webapps_venv
    ```
* Deactivate the enviroment for `conda`
    ```bash
    # deactivate enironment 
    $ conda deactivate

    # remove environment
    $ conda remove --name webapps_venv --all
    ```
* Delete source code
    ```bash
    # delete source code
    $ rm -rf merosite
    ```

#### Enjoy Merosite Web Application.

Email us at info@analyticstensor.com for any questions/comments/supports.