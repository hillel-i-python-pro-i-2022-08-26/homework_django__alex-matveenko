# Homework Alex Matveenko

***

[![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django__alex-matveenko/actions/workflows/main-workflow.yml/badge.svg)](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django__alex-matveenko/actions/workflows/main-workflow.yml)

### Django project

#### Include app:

* **Greetings**

### Main commands:

* `make homework-i-run` - *start project*
* `make init-dev` - *install requirements*
* `make pre-commit-run-all` - *run pre-commit tool for all files*

### Main routes:

**Link "Home"**

* `/` - *home page*

**Link "Greetings"**

* `/greetings/` - *home page with greetings for random name*
* `/greetings/(some name)` - *greetings for some name*

**Link "Users"**

* `/users/` - *view random users with name, email and password, by default 10 users*
* `/users/?amount=(some integer)` - *view random user info by the specified value*