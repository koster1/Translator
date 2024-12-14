Hello, this is my translator application, at the moment it translates only from English to Finnish, and there are some problems with translating names etc. 

# Installation Instructions #

With these you'll get the translator working.

## Prerequisites ##

You need python 3.6+ and pip for this.

- **Python 3.6+**: This project requires Python version 3.6 or higher.  
  [Download Python](https://www.python.org/downloads/)

- **pip**: Python’s package installer should be installed by default when you install Python. To check if you have it installed, run:
  ```bash
  pip --version

# Steps
## 1. Clone the repository

    git clone https://github.com/koster1/translator_app.git
    cd translator_app

## 2. Set up a virtual environment (optional but recommended)

It’s a good practice to use a virtual environment to isolate the project’s dependencies from the global Python environment.

Create a virtual environment:

    python -m venv venv

Activate the virtual environment:

On Windows:

    venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

## 3. Install the dependencies

Once the virtual environment is activated, install the required dependencies listed in requirements.txt:

    pip install -r requirements.txt


## 4. Run the application

With all dependencies installed and the .env file set up, you can run the Flask application:

    python app.py

By default, the app will start a local development server. Open your web browser and go to http://127.0.0.1:5000/ to view the app.
## 5. Stop the server

To stop the Flask development server, simply press Ctrl+C in your terminal.
