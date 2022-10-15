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

### Main commands:

* `make homework-i-run` - *start project*
* `make init-dev` - *install requirements*
* `make pre-commit-run-all` - *run pre-commit tool for all files*
* `python manage.py generate_info NUMBER` - *generate required amount of users (by default 10)*
* `python manage.py generate_info -i or --ignore NUMBER` - *generate required amount of users (by default 10) and set
  is_auto_generated field in model to False*
* `python manage.py delete_info` - *delete auto generate users info*
* `python manage.py delete_info --all` - *delete ALL users info*

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

3) Button `Delete user` - *delete user*
4) Button `Update user` - *updater user info*

**Link "Session Info"**

* `/session/` - *view user session info*

1) View session key
2) View number of visits
3) View last time of user visit