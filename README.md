# CampusConnect

**Name:** Abigail Dorothy T. Larawan
**Section:** G1
**Course:** CSIT327 - Lab: Creating Your First Django Application

A Django app with sign-up, login, a dashboard, an admin panel, and an editable profile page, styled with Bootstrap 5 (CDN).

## Features
- Sign-up with a success message (Django messages framework)
- Login and logout
- Profile page using `UpdateView`; users can only edit their own profile
- Bootstrap 5 styling on all pages with a shared `base.html`
- Admin panel (administrators only)

## How to run
1. Clone the repo: `git clone <repo-url>` and `cd` into it
2. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate` (Windows)
3. Install Django: `pip install django`
4. Apply migrations: `python manage.py migrate`
5. (Optional) Create an admin: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`
7. Open http://127.0.0.1:8000/
