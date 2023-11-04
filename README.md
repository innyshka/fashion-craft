# Fashion Craft Project 👗

Django project for managing the production of fashion clothing

## Check it out!
[Fashion Craft project deployed to render.com](https://fashion-craft.onrender.com/)

### Test User

```
username: best_test_user
password: 1QAZcde3
```

## Installation

Python3 must be already installed

```shell
git clone https://github.com/innyshka/fashion-craft.git
cd fashion_craft
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver #starts Django server
```

## Features

* Authentication and Registration functionality for Designer/User
* Managing clothes, designers, sizes, materials and clothes types from website interface
* Powerful admin panel for advanced managing

## Demo
![Website Interface](demo/img.png)

## DB structure
![DB structure](demo/db_structure.png)
