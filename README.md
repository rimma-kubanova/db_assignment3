# Health Report Project

A web application that allows users to manage health-related data, such as disease reports, patient information, and countries' health statistics. This project is built using Django REST Framework (DRF) and PostgreSQL as the database, deployed on Render.com.

DEPLOYED ON: https://health-report.onrender.com/api/

## Features

- **User Management**: Users can be created, updated, retrieved, and deleted.
- **Health Reports**: Disease reports including details like total patients and deaths per country.
- **Countries**: Information about countries' health data.
- **Disease Information**: Disease types and specific disease data.

## Requirements

- Python 3.8 or higher
- Django 3.0 or higher
- PostgreSQL
- Django REST Framework (DRF)

## Getting Started

### 1. Clone the repository

Clone the project to your local machine:

```
git clone https://github.com/your-username/health-report.git
cd health-report
```

### 2. Set up a virtual environment
Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate  # On Windows, use env\Scripts\activate
```

### 3. Install dependencies
Install the required Python packages:

```
pip install -r requirements.txt
```

### 4. Create a .env file
Create a .env file in the project root and add the following environment variables for your database configuration:

```
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://your_user:your_password@localhost:5432/your_db_name
```

### 5. Set up the database
Run the migrations to set up your PostgreSQL database:

```
python manage.py migrate
```

### 6. Run the server locally
Start the development server:

```
python manage.py runserver
```
