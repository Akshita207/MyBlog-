from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^sign_up/$',views.sign_up,name='sign-up'),
    url(r'^about/$',views.AboutView,name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
