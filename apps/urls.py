from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books_cbv/', include('books_cbv.urls', namespace='books_cbv')),
    url(r'^books_fbv/', include('books_fbv.urls', namespace='books_fbv')),
    url(r'^books_fbv_user/', include('books_fbv_user.urls', namespace='books_fbv_user')),
    url(r'^$', 'apps.views.home'),
]
