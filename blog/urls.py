# importing django routing libraries
from . import views
from django.urls import path, include
from .views import *
from .feeds import blogFeed
from django.contrib.sitemaps.views import sitemap
from .sitemaps import blogSitemap

blogsitemap = {
"blog": blogSitemap, }

urlpatterns = [
	# home page
	path('', views.postslist.as_view(), name='posts'),
    path('', views.postslist.as_view(), name='home'),
	# route for posts
	path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
     # RSS route  
    path("posts / feed", blogFeed(), name ="feed"),
       # urls handling site maps
    path("sitemap.xml", sitemap, {"sitemaps": blogsitemap}, name ="sitemap"),
    
]
