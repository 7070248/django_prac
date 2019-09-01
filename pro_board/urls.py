from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('create', views.create_post, name='create_post'),
    path('delete/<int:post_id>', views.delete_post, name='delete_post'),
    path('update/<int:post_id>', views.update_post, name ='update_post'),
    path('comment/<int:post_id>', views.create_comment, name='create_comment'),
]
