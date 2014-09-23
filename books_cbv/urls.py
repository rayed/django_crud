from django.conf.urls import patterns, url

from books_cbv import views

urlpatterns = patterns('',
  url(r'^$', views.BookList.as_view(), name='book_list'),
  url(r'^new$', views.BookCreate.as_view(), name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
)