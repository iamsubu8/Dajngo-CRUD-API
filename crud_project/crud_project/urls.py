from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crud_app import views

from crud_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addProduct',AddProductView.as_view()),
    path('getAllProduct',GetAllProductView.as_view()),
    path('getProductByID',GetProductByIdView.as_view()),
    path('updateProductByID',UpdateproductView.as_view()),
    path('deleteProductByID',DeleteProductView.as_view()),
]
