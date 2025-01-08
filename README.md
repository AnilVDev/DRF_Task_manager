# Django Task Manager Backend

A backend for a Task Manager application built with Django. It provides essential functionalities such as user creation, login, task creation, and task management, including task updating and deletion.

## Features:
- User Registration: Allows new users to create accounts.
- User Authentication: Enables login and generation of JWT tokens for authenticated access.
- Task Management: Enables authenticated users to create, update, and delete tasks associated with their accounts.

### Detailed Task View:
- Display a list of task including their title, descriptions, and completion statuses.
- Provide actions to Add, Update, and Remove task.
- Allow marking todos as "Pending," "In Progress," or "Completed."

## Setup

### Backend (Django)

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>


2. Create a virtual environment (optional but recommended):

   ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install backend dependencies: Make sure to have Python 3.11.1 installed.

   ```bash
    pip install -r requirements.txt

4. Apply migrations:

   ```bash
    python manage.py migrate

5. Run the backend:

   ```bash
    python manage.py runserver

The backend will be accessible at http://127.0.0.1:8000/.


## Testing

### Backend Testing (Django)
The backend includes a comprehensive suite of tests to validate key functionality, including authentication, and task management.

**Running Tests**

1. Ensure the virtual environment is activated.

2. Run the test suite:

   ```bash
   pytest

**Test Details**

- **Authentication** : Verifies token-based authentication and unauthorized access restrictions.
- **Task Tests** :
   - Creating task .
   - Validates permissions to ensure users cannot access or modify task in unauthorized projects.
   - Duplicate task tiltle for same user are restricted.



## Dependencies

- asgiref==3.8.1
- cfgv==3.4.0
- colorama==0.4.6
- distlib==0.3.9
- Django==5.1.4
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- drf-yasg==1.21.8
- filelock==3.16.1
- identify==2.6.5
- inflection==0.5.1
- iniconfig==2.0.0
- nodeenv==1.9.1
- packaging==24.2
- platformdirs==4.3.6
- pluggy==1.5.0
- pre_commit==4.0.1
- PyJWT==2.10.1
- pytest==8.3.4
- pytz==2024.2
- PyYAML==6.0.2
- sqlparse==0.5.3
- tzdata==2024.2
- uritemplate==4.1.1
- virtualenv==20.28.1




## Project Structure

   ```bash
    Task Manager/
    ├── task manager/                  # Django backend files
    │   ├── manage.py
    │   ├── requirements.txt      # Backend dependencies
    │   └── ...                
    └── venv/                     # Virtual environment (if created)


   
