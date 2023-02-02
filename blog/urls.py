from django.urls import path, include
from .views import *

urlpatterns = [
#    path('api/', include('blog.urls')),
    path('posts', PostListView.as_view(), name='post_list')
]