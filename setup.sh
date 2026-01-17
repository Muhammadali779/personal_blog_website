#!/bin/bash

# Blog & Education Platform Setup Script

echo "========================================="
echo "Blog & Education Platform Setup"
echo "========================================="

# Check Python version
python --version || python3 --version

# Create virtual environment
echo "
Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate

# Install dependencies
echo "
Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Copy env file
if [ ! -f .env ]; then
    echo "
Creating .env file..."
    cp .env.example .env
    echo "Please edit .env file with your database credentials!"
fi

# Create database (PostgreSQL)
echo "
Setting up database..."
echo "Make sure PostgreSQL is running and create database:"
echo "  createdb blog_education_db"
read -p "Press enter when database is ready..."

# Run migrations
echo "
Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "
Creating superuser..."
python manage.py createsuperuser

# Collect static files
echo "
Collecting static files..."
python manage.py collectstatic --noinput

echo "
========================================="
echo "Setup Complete!"
echo "========================================="
echo "
To start the development server:"
echo "  python manage.py runserver"
echo "
Then visit: http://127.0.0.1:8000"
echo "Admin panel: http://127.0.0.1:8000/admin"
echo "========================================="
