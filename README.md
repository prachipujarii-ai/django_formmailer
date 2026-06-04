# Django Form Mailer

## Overview
A Django web application that handles form submissions, stores entries in a SQLite3 database, and sends email notifications after successful form filling.  
It also includes an admin interface for managing data and users.

## Features
- Form submission with validation
- Email notifications after form completion
- SQLite3 database for storing entries
- Django admin panel for managing submissions
- User authentication for admin access

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-formmailer.git
   cd django-formmailer

2. Install dependencies:
   ```pip install django```

3. Run initial setup:
   ```django-admin startproject mysite .```
   ```python manage.py startapp job_application```
   ```python manage.py makemigrations```
   ```python manage.py migrate```

4. Create a superuser for the admin interface:
   python manage.py createsuperuser

   Example:
   Username: xxxxxx
   Password: xxxxxx
   Email: xxxxxx

5. Start the server:
   ```python manage.py runserver```
   
   Visit: http://127.0.0.1:8000/admin/ (127.0.0.1 in Bing)

## Usage
- Fill out the form on the webpage.
- Submitted data is stored in the SQLite3 database.
- An email notification is sent after successful submission.
- Admins can log in at /admin/ to view and manage entries.

## Project Structure
- mysite/ → Django project configuration
- job_application/ → App handling forms and submissions
- db.sqlite3 → Database file
- README.md → Project documentation


   
