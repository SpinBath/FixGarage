# FixGarage

![FixGarage-BannerImage](https://github.com/XRayBinary/assets/blob/main/FixGarage-1280x640.png?raw=true)

# General info

The application is a minimalistic web app that performs basic CRUD operations on a sample data model.

# Screenshots

![FixGarage-FixGarage-Login](https://github.com/XRayBinary/assets/blob/main/FixGarage-Login.PNG?raw=true)

![FixGarage-FixGarage-Clients](https://github.com/XRayBinary/assets/blob/main/FixGarage-Clients.PNG?raw=true)

![FixGarage-FixGarage-Services](https://github.com/XRayBinary/assets/blob/main/FixGarage-Services.PNG?raw=true)

![FixGarage-FixGarage-EditVehicle](https://github.com/XRayBinary/assets/blob/main/FixGarage-EditVehicle.PNG?raw=true)

# Setup

Clone this repository to your local machine and navigate to the project folder:

```
git clone https://github.com/XRayBinary/FixGarage.git

cd FixGarage
```

## Create a Virtual Environment (Optional but Recommended)

To avoid dependency conflicts, it’s recommended to create a virtual environment:

```
python3 -m venv venv

venv\Scripts\activate
```
## Install Dependencies

```
pip install -r requirements.txt
```

## Set Up Environment Variables

Create an .env file in the project’s root directory with the necessary configurations. 

An example .env file:

```
echo SECRET_KEY="your_secret_key" > .env
```
To generate a Django SECRET_KEY you can use https://djecrety.ir/ made by https://github.com/mrouhi13


## Start the Development Server

To start the development server, run:

```
python manage.py runserver ip:port
```


# Enjoy it !!

