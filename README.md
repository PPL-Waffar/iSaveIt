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

## iSaveIt Heroku Link:
https://isaveit.herokuapp.com/


### iSaveIt: A financial management application
iSaveIt is a money management application that hope to organize budget and expenses with the intent that users can spend their money responsibly. The features we hope to implement are creating multiple pockets as needed, input transactions, keep track of the money users might've borrowed from other people, viewing the finance report, and reading newsletter about finance and economy. 


**Changes:**
The changes made in this sprint is the progress on Newsletter Epic. There is a modification made for the backlog task. Initially we wanted the admin to retrieve online article API and published them into the newsletter section of our application. However, we find that backlog to be quite challenging, so we switch it into admin writing the articles (copy and paste) into backend website where they can post the article text, title, creditted website, and add image. This is successfully created in the newsletter app, where the admin can write, publish, and delete articles. There's also an update for the front end for displaying the list of articles and article text. 

Another changes is that we have managed to connect the edit profile, borrow transaction, and report epics. 

### List of iSaveIt Features:
Register
**Before the users can access the features of the application, they are required to register themselves by inputting their personal information.**
**The details of the information includes:**
1. Name
2. Email
3. Password
4. Password confirmation

**Login**
Once the users have registered themselves, they are required to login to the application in order to access the remaining features. To login to the application, they are required to input the same emails and password that they have used in the registration process.

**Budget Tracker**
**This feature mainly focuses on giving the users the options to input their budget as well as expense. Budget Tracker allows users to:**
1. Input their expense and put categories on each of their spending 
2. Input their income to increase their budget
3. Check the list of their transactions from the pocket page or the report page
4. Choose to input their debt in a form of expense (debt)
5. Choose to input the money they have borrowed to other people in a form of expense (lending money)
6. View the list of expenses that are categorized as either debt or lending money

**Budget Categories**
**The Budget Categories feature focuses on dividing the user’s budget into several categories based on their needs, the budget is referred to as pocket. By utilizing Budget Categories feature, the users are able to:**
1. Create new pocket, by allocating their budget into some categories that are provided by iSaveIt application, as well as creating new categories title that they desired
2. Delete the pocket they have created
3. View the details of their pocket
4. Edit the details of the pocket they have created
5. View the list of pocket categories that they are free to choose

**Planned Payment**
**The planned payment feature focuses on keeping track of the user’s subscription/recurring payments, such as Spotify, Netflix, HBO,etc. This feature provides users with access to:**
1. Input the subscription
2. Remove the subscription
3. See the details of their subscription
4. Update the details of their subscription
5. See the list of subscriptions they have


**Finance Report**
**The finance report feature displays the details of the user’s financial report, including:**
1. Spending report divided into categories, will be displayed in a form of pie chart
2. The list of individual income and expense, including the information of the payment and the amount
3. Download finance report button option

**Newsletter**
**The Newsletter feature provides articles and news related to finance, money management, saving money tips and tricks, etc, that are available for the users to choose and read. Newsletter feature flow:**
1. The admin will retrieve online article API to be displayed on the user’s newsletter page
2. The users can click on and read each article
3. The admin can choose to delete the newsletters that are no longer required

**Feedback Report**
**The Feedback Report feature focuses on providing an option for the users to share their opinions and feedback regarding the application.** 
1. The users are able to create feedback report
2. The users are able to delete the feedback report
3. The admins will fix the application based on the users’ feedback
4. The users are able to update the application once the admins have fixed the problem relating to the application

**Edit Profile**
During the registration process, the users are asked to input details regarding their personal information, which later will be displayed on their profile page. The Edit Profile feature allows users to create changes on their personal information. The updated information will then be displayed on their profile page.

## Summary of SQA
### Sprint 1
[UAT sprint 1 test cases](https://docs.google.com/spreadsheets/d/1wVKp_U2KGYYdOu7ktalVgQA0ULiJT_J4Y4Sbqrq7LX0/edit?usp=sharing)

[codecov staging](https://app.codecov.io/gh/PPL-Waffar/iSaveIt/tree/staging)

[code factor staging](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/issues)

### Sprint 2
[UAT sprint 2 test cases](https://docs.google.com/spreadsheets/d/1wVKp_U2KGYYdOu7ktalVgQA0ULiJT_J4Y4Sbqrq7LX0/edit?usp=sharing)

[codecov staging](https://app.codecov.io/gh/PPL-Waffar/iSaveIt/tree/staging)

[code factor staging](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/issues)

### Sprint 3
[UAT sprint 3 test cases](https://docs.google.com/spreadsheets/d/1wVKp_U2KGYYdOu7ktalVgQA0ULiJT_J4Y4Sbqrq7LX0/edit?usp=sharing)

[codecov staging](https://app.codecov.io/gh/PPL-Waffar/iSaveIt/tree/staging)

[code factor staging](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/issues)

### Sprint 4
[UAT sprint 4 test cases](https://docs.google.com/spreadsheets/d/1wVKp_U2KGYYdOu7ktalVgQA0ULiJT_J4Y4Sbqrq7LX0/edit?usp=sharing)

[codecov staging](https://app.codecov.io/gh/PPL-Waffar/iSaveIt/tree/staging)

[code factor staging](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/issues)

### Sprint 5
[UAT sprint 5 test cases](https://docs.google.com/spreadsheets/d/1wVKp_U2KGYYdOu7ktalVgQA0ULiJT_J4Y4Sbqrq7LX0/edit?usp=sharing)

[codecov staging](https://app.codecov.io/gh/PPL-Waffar/iSaveIt/tree/staging)

[code factor staging](https://www.codefactor.io/repository/github/ppl-waffar/isaveit/issues)
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


