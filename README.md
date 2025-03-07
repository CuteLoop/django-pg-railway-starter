# Django Blog with Railway Template

A responsive Django Ready for quick deployment on Railway.

## Features

- **Responsive Design:** Built with Bootstrap 5.
- **Fixed Navbar:** Always accessible navigation.
- **Railway Ready:** Quick deployment via Railway.

## Local Development

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/CuteLoop/django-pg-railway-starter.git
   cd django-pg-railway-starter
   ```

python3 -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Open http://localhost:8000 in your browser.

## Connect your local repository to Railway
railway link (string that appears on your railway dashboard)
#### deploy
railway up

## For images and media files it might be worth to host on cloudinary or an S3 bucket
Cloudinary would be easier and faster to add to the project.

## Before going into production
Make sure you add a safe django key to enviroment variables on railway dashboard named SECRET_KEY

## generate django secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'




