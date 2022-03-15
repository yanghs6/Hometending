from .views import base_views, post_views, answer_views, comment_views, vote_views
from django.urls import path




app_name = 'boardapp'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:post_id>/', base_views.detail, name='detail'),

    # post_views.py
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', post_views.post_delete, name='post_delete'),
    path('post/photo/<int:post_id>/', post_views.post_photo, name='post_photo'),

    # answer_views.py
    path('answer/create/<int:post_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/post/<int:post_id>/', comment_views.comment_create_post, name='comment_create_post'),
    path('comment/modify/post/<int:comment_id>/', comment_views.comment_modify_post, name='comment_modify_post'),
    path('comment/delete/post/<int:comment_id>/', comment_views.comment_delete_post, name='comment_delete_post'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py
    path('vote/post/<int:post_id>/', vote_views.vote_post, name='vote_post'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),

]

