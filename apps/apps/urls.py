from django.urls import include, path
from django.contrib import admin

import theme.views

urlpatterns = [
    path('', theme.views.home),
    path('books_cbv/', include('books_cbv.urls')),
    path('books_fbv/', include('books_fbv.urls')),
    path('books_fbv_user/', include('books_fbv_user.urls')),

    # Enable built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),    
    # Enable built-in admin interface
    path('admin/', admin.site.urls),
]
