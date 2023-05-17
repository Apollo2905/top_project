from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('post/<slug>', views.post, name='post'),
    path('delete/<slug>', views.delete_post, name='delete_post'),
    path('edit/<slug>', views.edit_post, name='edit_post'),
    path('like/<slug>', views.like, name='like'),
    path('dislike/<slug>', views.dislike, name='dislike'),
    path('comment_delete/<int:pk>', views.comment_delete, name='comment_delete'),
    path('comment_edit/<int:pk>', views.comment_edit, name='comment_edit'),
]
# namespace - для работы со ссылками

# urlpatterns += staticfiles_urlpatterns()
