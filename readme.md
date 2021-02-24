How to setup

1. git clone https://github.com/rnjane/pula-yield-index-api.git
2. cd pula-yield-index-api
3. create a virtual environment - virtualenv -p python3 venv(if using virtualenv)
4. Activate virtual environment(source venv/bin/activate)
5. pip install -r requirements.txt
6. python manage.py runserver

setup frontend.
1. cd pula-yield-index-api/frontend
2. npm install
3. npm run dev

Go to http://localhost:8080/
Login with robertnjane as username and roba2020 as password. After login, reload the page(unfortunately there is something I've not worked on in the login process)

I've pushed the sqlite db to make it easier to test, without having to create test data.