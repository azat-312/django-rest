
from django.contrib import admin
from django.urls import path
from afisha import views
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/',
         views.product_list_create_api_view),  # GET->list, POST->create
    path('api/v1/products/<int:id>/',
         views.product_detail_api_view),  # GET->item, PUT->update, DELETE->destroy
    path('api/v1/products/', include('products.urls')),
    path('api/v1/users/', include('users.urls'))
]