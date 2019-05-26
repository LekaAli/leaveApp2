# LeaveApp2
Leave application that allows an employee to apply for a leave

# How to Install Dependencies
pip3 install virtualenv <br/>
mkdir -p ~/.virtualenvs <br/>
pip3 install virtualenvwrapper <br/>
mkvirtualenv leave_env <br/>
If the virtual environment is not activated, type "workon leave_env" <br/> 
pip3 install -r requirements.txt

# Setup the application
To create DB model: python manage.py makemigrations leave_manager <br/>
python manage.py migrate <br/>
python manage.py createsuperuser <br/>
Follows the prompts to create the user account up until it is successfully created <br/>

# How to Run Application
cd leaveApp2 <br/>
cd leave <br/>
workon leave_env <br/>
python manage.py runserver

# Creating access token for use to access the services
Open browser or api testing application: http://127.0.0.1:8000/api/auth/access-token/ <br/>
Prompted for username and password. <br/>
When successfully validated, an access-token and a refresh-token will be created. <br/>
Refresh token is used for access-token creation since access-token is only valid for 5 minutes while refresh-token is valid for 24 hours. <br/>

# Accessing the web services

Open api testing application(i.e. Postman)<br/>
Type the following address in the request url section: http://127.0.0.1:8000/api <br/>
Set request authorisation using the generated access-token.<br/>
Available services: <br/>
1. /api/employee/ - accept both get and post request <br/>
  - GET: retrieve employee given the emp_number.<br/>
  - POST: create/update employee account.<br/>
2. /api/leave/ - accept both get and post request <br/>
  - GET: retrieve employee leave request. <br/>
  - POST: create/update employee leave request. <br/>
3. /api/auth/refresh-token/ - accept post request <br/>
 - POST: If refresh token is valid, this service will generate a new access-token.<br/>
# Running test cases using coverage
coverage run manage.py test tests -v 2



