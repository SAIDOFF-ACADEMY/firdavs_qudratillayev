from django.urls import path

from user import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:id>/', views.UserDetail.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('users/login/', views.UserLoginView.as_view()),
    path('users/logout/', views.UserLogOutView.as_view()),
    path('user_contacts/', views.UserContactView.as_view()),
    path('user_contact/<int:id>/', views.UserContactDetail.as_view()),
]
