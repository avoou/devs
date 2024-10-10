# Simple Django Project

## Purpose

This project is intended as a learning exercise to understand Django.

## Setting Up the Environment

To ensure a clean environment and avoid conflicts with dependencies, create a virtual environment:

1. Navigate to your project directory:
    ```bash
    cd /path/to/your/project
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Ubuntu/Linux or macOS:
    ```bash
    source venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Navigate to the Django project directory.
2. Apply migrations:
    ```bash
    python manage.py migrate
    ```
3. Create new migrations. By default, SQLite DB is used:
    ```bash
    python manage.py makemigrations
    ```
4. (Optional) If you want to use the admin panel (to control users, projects, create tags, etc.), create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the server:
    ```bash
    python manage.py runserver
    ```

By default, the project's link is: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Using the Project

1. Sign up and log in with your new user.
2. Edit your profile.
3. Add some projects to your profile.
4. Vote and write comments on any projects.
5. Send messages to other users.

## API Usage

There is an API available to get information about specific projects.

### Get API Token

1. Go to: [http://127.0.0.1:8000/api/users/token/](http://127.0.0.1:8000/api/users/token/)
2. Fill in your username and password (you must have already signed up).

### Available API Endpoints

- Get a list of all projects:
    ```plaintext
    http://127.0.0.1:8000/api/projects/
    ```

- Get information about a specific project by ID:
    ```plaintext
    http://127.0.0.1:8000/api/projects/<project-id>/
    ```