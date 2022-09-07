from django.urls import path

from post import views

# post/
urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:post_id>', views.PostView.as_view()),
]
