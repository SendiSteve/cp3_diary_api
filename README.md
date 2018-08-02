[![Build Status](https://travis-ci.com/SendiSteve/cp3_diary_api.svg?branch=develop)](https://travis-ci.com/SendiSteve/cp3_diary_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/1ca30df1db0d24dfe4ed/maintainability)](https://codeclimate.com/github/SendiSteve/cp3_diary_api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/SendiSteve/cp3_diary_api/badge.svg?branch=develop)](https://coveralls.io/github/SendiSteve/cp3_diary_api?branch=develop)

# Diary API
This is a simple api that allows users to create, read, update and delete their diary entries. It uses  postgres database to persist the data.


## Technologies used
1. Python 3.6.4
2. Flask==1.0.2
3. Virtualenv
4. Postgresql

## Getting Started
The following instructions will help to set up the application on a local development machine.

1. Install Postgresql
Follow the following steps to have postgres running on your local machine.

* Install postgres: ``brew install postgresql``
* In terminal type ``psql``.
* In postgres interactive shell, type` ``CREATE DATABASE test_db;``
* Update the database_uri  with the created database from steps above. Use postgres as your user`


2. Clone the repository
```
https://github.com/SendiSteve/cp3_diary_api.git```
```

3. Navigate to the repository
```
cd cp3_diary_api
``` 

4. Create a virtual environment
```
virtualenv venv
```

5. Activate the virtual environment
```
source venv/bin/activate
```

6. Install dependencies
```
pip install -r requirements.txt
```


7. Run the application 
```
python run.py 
```

8. To run the tests  
```
# in root
pytest 
```

## API End points

Test the endpoints below using Postman


| End Point                      | Method        |   Functionality               |   Functionality  |
| -----------------------------  | ------------- | -------------------------     | ---------------- |   
| `/api/v2/auth/register`           |  POST       | User can register      | PUBLIC          |
| `/api/v2/auth/login`           |  POST       | User can login      | PUBLIC          |
| `/api/v2/entries`           |  GET       | User can GET all entries      | PRIVATE          |
| `/api/v2/entries`           |  POST       | User can ADD all entries      | PRIVATE          |
| `/api/v2/entries/<int:entry_id>`| DELETE | User can DELETE an entry by its id  | PRIVATE         |
| `/api/v2/entries/<int:entry_id>`| PUT    | User can UPDATE an entry by its id  | PRIVATE           |
