from . import views
from django.urls import path

app_name = 'firstbook'

urlpatterns = [#path('', include(router.urls)),
                path('index/', views.basiclayout, name='index'),
                path('books_list/', views.books_list, name='books_list'),
                path('books/<int:pk>/', views.book_detail, name='book_detail'),
                path('libs_list/', views.libs_list, name='libs_list'),
                path('libs/<int:pk>/', views.lib_detail, name='lib_detail'),



                #DRF urls
                path('api/books/', views.BookListCreateView.as_view(), name='book_list_api'),
                path('api/books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail_api'),
                path('api/libs/', views.LibraryListCreateView.as_view(), name='library_list_api'),
                path('api/libs/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail_api'),
]