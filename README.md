# Django-Api
- The api is created to monitor the time and date of people.
- the sample JSON file given here -
https://drive.google.com/open?id=1xZa3UoXZ3uj2j0Q7653iBp1NrT0gKj0Y
- This JSON file describes a list of users & their corresponding periods of activity across
multiple months.
- Now, design and implement a Django application with User and ActivityPeriod models, write
a custom management command to populate the database with some dummy data, and design
an API to serve that data in the json format given above.
---
###  Steps to run the program

  - Install the requirements.txt file using pip
  ```sh
$ pip install -r requirements.txt
```
 - Add the migration using the following commands
  ```sh
$ python manage.py makemigrations 
```
 - Migrate the data
  ```sh
$ python manage.py migrate 
```
 - Run the program
  ```sh
$ python manage.py runserver 
```
### Author Info
- Abhinav Jha
	* Junior Software Developer and Data Scientist
	* LinkedIn - [Abhinav Jha](https://www.linkedin.com/in/abhinavjha98/)
	* For any doubts contact : Abhinav Jha (abhinavjha98ald@gmail.com)

[Back To The Top](#read-me-template)

