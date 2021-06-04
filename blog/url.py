from django.urls import path
from . import views
from .views import( PostListView, PostDetailView, 
                PostCreateView, PostUpdateView, PostDeletelView)

urlpatterns = [
    # it will look for <app>/<model>_<viewtype>
    #                  blog/Post_list
    path('', PostListView.as_view(), name = 'Blog-Home'), #Post list view is a class we neeed to convert it to a view hence we add the .as_view fn
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/delete', PostDeletelView.as_view(), name = 'post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'), #will share the name with update form so, the name will be post_form
    path('about/', views.about, name = 'Blog-About'),
    
]