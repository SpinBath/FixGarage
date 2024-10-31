# FixGarage

![FixGarage-BannerImage](https://github.com/XRayBinary/assets/blob/main/FixGarage-1280x640.png?raw=true)

> [!NOTE]  
> Project under development but currently functional.

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
	 
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

venv\Scripts\activate
```
Install Dependencies

```
pip install -r requirements.txt
```

Set Up Environment Variables

Create an .env file in the project’s root directory with the necessary configurations (such as environment variables for the database and security settings). 
An example .env file:

To generate a Django SECRET_KEY you can use https://djecrety.ir/ made by https://github.com/mrouhi13

```
echo SECRET_KEY="your_secret_key" > .env
```

Start the Development Server
To start the development server, run:

```
python manage.py runserver ip:port
```

Enjoy it !!

