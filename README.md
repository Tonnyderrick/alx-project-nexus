# Online Poll System Backend

This project is a backend system for managing online polls. It supports poll creation, real-time voting, and result computation. Designed using Django and PostgreSQL, it includes a Swagger-powered API documentation interface.

---

## Features

* Create polls with multiple choices
* Set expiration for each poll
* Vote once per user per poll
* Real-time vote count and result computation
* Swagger UI for API documentation at `/api/docs`

---

## Tech Stack

* **Backend:** Django (DRF)
* **Database:** PostgreSQL
* **Documentation:** Swagger (drf-yasg)

---

## Project Structure
poll_system/
├── api/ # DRF views, serializers, urls
├── polls/ # Models and business logic
├── manage.py
├── requirements.txt
└── README.md

Getting Started

Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Tonnyderrick/poll-system-backend.git
cd poll-system-backend

##Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate

##Install dependencies

bash
pip install -r requirements.txt


##Configure PostgreSQL

Update your settings.py with your PostgreSQL credentials:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'poll_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

##Run migrations and start the server

bash

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

 ##API Endpoints
Method	Endpoint	Description
POST	/api/polls/	Create a new poll
GET	/api/polls/	List all polls
POST	/api/polls/<id>/vote/	Cast a vote
GET	/api/polls/<id>/results/	View poll results

Full Swagger Docs available at: /api/docs

##Future Improvements
Add user authentication

Poll result visualization (charts)

Limit poll access to certain users/groups

Author
Built by Tonny DERICK
GitHub: @Tonnyderrick