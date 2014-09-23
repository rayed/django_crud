# Django CRUD Example Apps

Here you will find two small CRUD applications for managing a books table, one application is implemented using Class Based Views (books\_cbv), and the other will implemented using Function Based Views (books\_fbv).

## Installation

Move the directories "books_cbv" and "books_fbv" to your Django application directory. 

Add to your "setting.py":

    INSTALLED_APPS = (
    :
    'books_cbv',
    'books_fbv',
    :
    )


Add to "urls.py":

    urlpatterns = patterns('',
    :
    url(r'^books_cbv/', include('books_cbv.urls', namespace='books_cbv')),
    url(r'^books_fbv/', include('books_fbv.urls', namespace='books_fbv')),
    :
    )

Make sure you sync your DB using:

    ./manage.py syncdb 

or for Django 1.7:

    ./manage.py makemigrations
    ./manage.py migrate

Now you can access the two application on the URLs <http://localhost:8000/books_fbv> and <http://localhost:8000/books_cbv>
