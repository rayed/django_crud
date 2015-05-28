# Django CRUD Example Apps

Here you will find two small CRUD applications for managing a books table, one application is implemented using Class Based Views (books\_cbv), and the other will implemented using Function Based Views (books\_fbv).

## Running the Application


Make sure you create the your DB using:

    ./manage.py migrate

or for Django < 1.7:

    ./manage.py syncdb 

Now you can run the development webs server:

    ./manage.py runserver 

To access the two applications go to the URL <http://localhost:8000/> 
