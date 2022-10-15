# iSaveit
[![CodeFactor](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/badge)](https://www.codefactor.io/repository/github/ppl-waffar/isaveit)
**Product Owner:**
1. Anastasia Audi Wulandari - 2006607495
2. Anne Yuliana - 2006607513

**Devops:**
1. Winaldo Amadea Hestu - 2006520001

**Dev members:**
1. Firlandi Althaf Rizqi Ansyari - 2006489874
2. Raihan Fadhila Sukmana - 2006519971
3. Reynaldi Oktavianus 2006607601


### What is iSaveIt?
iSaveIt is a money management application that hope to oprganize budget and expenses with the intent that users can spend their money responsibly. The features we hope to implement are creating multiple pockets as needed, input transactions, keep track of the money users might've borrowed from other people, viewing the finance report, and reading newsletter about finance and economy. 

## Getting Started
This is a `Django` project that mainly contain the `back-end` materials.

## Requirements
- Python 3.9.5 or later
- pip
- venv

## How To Run This App Locally
### Backend & Database
1. Clone this repository

```bash
git clone https://github.com/PPL-Waffar/iSaveIt.git
```

2. Navigate to the branch `staging`

3. Create a python virtual environment

```bash
python -m venv env # depending on your computer/os, it may be python3
```

4. Activate the virtual environment

```bash
source env/bin/activate # MacOS / Linux

env\Scripts\activate # Windows
```

5. Install the required dependencies

```bash
pip install -r requirements.txt
```

6. In the directory, run make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6.5. (Optional) Run backend tests

```bash
coverage run --source='.' manage.py test
```
7. Create a superuser account and check the database in local Dhango admin
```
python manage.py createsuperuser
* input name and password
```

8. Run the application
```
python manage.py runserver
```
9. Check the local database

open `127.0.0:8000/admin`
