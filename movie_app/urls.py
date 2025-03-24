from django.urls import path
from afisha import views
 
urlpatterns = [
     path('', views.directors_list_create_api_view),
     path('<int:id>/', views.director_details_api_view)
 ]