# Homework Alex Matveenko

***

[![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django__alex-matveenko/actions/workflows/main-workflow.yml/badge.svg)](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django__alex-matveenko/actions/workflows/main-workflow.yml)

### Django project

#### Include app:

* **Greetings**
* **Base**
* **users_generator**
* **phone_book**
* **session_app**
* **accounts**
* **middlewares**
* **drf_crud**

### Main commands:

* `make homework-i-run` - *start project*
* `make init-dev` - *install requirements*
* `make pre-commit-run-all` - *run pre-commit tool for all files*
* `python manage.py generate_info NUMBER` - *generate required amount of users (by default 10)*
* `python manage.py generate_info -i or --ignore NUMBER` - *generate required amount of users (by default 10) and set
  is_auto_generated field in model to False*
* `python manage.py delete_info` - *delete auto generate users info*
* `python manage.py delete_info --all` - *delete ALL users info*
* `make d-homework-i-run` - *start project in docker*
* `make d-homework-i-purge` - *make all actions needed for purge homework related data.*
* `make d-run-i-local-run` - *run postgres locally*
* `python manage.py delete_session_info -ds or --delete_sessions` - *delete all sessions info from DB*

### Main routes:

**Link "Home"**

* `/` - *home page*

**Link "Greetings"**

* `/greetings/` - *home page with greetings for random name*
* `/greetings/(some name)` - *greetings for some name*

**Link "Users"**

* `/users/` - *view random users with name, email and password, by default 10 users*
* `/users/?amount=(some integer)` - *view random user info by the specified value*

**Link "Phone Book"**

* `/phone-book/` - *view phone book with name, phone number and date of birthday*

1) Link `Add user` - *inside link* `Phone Book`

* `/phone-book/add-user/`

2) Link `Search user` - *inside link* `Phone Book`

* `/phone-book/search-user/` - *you can enter phone number or user ID and see info about him*

3) Button `Delete user` - *delete user*(login required)
4) Button `Update user` - *updater user info*(login required, can't confirm updates without log in)

**Link "Session Info"**

* `/session/` - *view user session info*

1) View session key
2) View number of visits
3) View last time of user visit

**Link `Log In`**
*`/login/`* - *view log in form*

**Link `Log In`**
*`/logout/`* - *logout from account*

**Link `Register`**
*`/accounts/signup/`* - *registration form*

**Link `Edit profile`**
*`/accounts/edit/<pk>`* - *views if you authorize. here you can edit your profile*

**Link `Middleware`** - *main page of middleware and session info(name it like this to easy understanding)*

1) Link `All info about actions` - *inside link* `Middleware`

* *info about all users sessions, activity and last visit*

2) Link `Info about current session actions` - *inside link* `Middleware`

* *info about current session, activity and last visit*

3) Link `Info about current user actions` - *inside link* `Middleware`

* *info about current user session, activity and last visit*

**API Links `Edit profile`**

1) `api/v1/contacts/` - *list all contacts as API* (require auth)
2) `api/v1/create/` - *API endpoint to create contact* (require auth)
3) `api/v1/show/contact_pk` - *API endpoint to show one contact* (require auth)
4) `api/v1/update/contact_pk` - *API endpoint to update one contact* (require auth)
5) `api/v1/delete/contact_pk` - *API endpoint to delete one contact* (require auth)