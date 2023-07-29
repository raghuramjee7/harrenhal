from django.urls import path
from .views import BlogListView
from .views import BlogDetailView
from .views import BlogCreateView
from .views import BlogUpdateView
from .views import BlogDeleteView

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name = "post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name = "post_detail"),
    path("post/<int:pk>/update/", BlogUpdateView.as_view(), name = "post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name = "post_delete"),
    path("", BlogListView.as_view(), name = "home"),
]