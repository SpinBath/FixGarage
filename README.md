# FixGarage

> [!NOTE]  
> This project is currently under development.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:

## Requirements

To run this project, make sure you have the following installed:

All requirements are

```
$ pip install -r requirements.txt
```

  * asgiref = 3.8.1
  * Django = 5.1.2
  * python-dotenv = 1.0.1
  * sqlparse = 0.5.1
  * tzdata = 2024.2
    
## Setup

Clone this repository to your local machine and navigate to the project folder:

```
git clone https://github.com/XRayBinary/FixGarage.git
cd FixGarage
```

Create a Virtual Environment (Optional but Recommended)

To avoid dependency conflicts, it’s recommended to create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
Install Dependencies

```
pip install -r requirements.txt
```

Set Up Environment Variables

Create an .env file in the project’s root directory with the necessary configurations (such as environment variables for the database and security settings). 
An example .env file:

```
SECRET_KEY="your_secret_key"
```

Run Database Migrations
To set up the database, run the initial migrations:

```
python manage.py migrate
```

Start the Development Server
To start the development server, run:

```
python manage.py runserver
```


