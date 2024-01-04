
from django.urls import path
from . import views

from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home,name='home'),
    path('product',views.product,name='product')
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 