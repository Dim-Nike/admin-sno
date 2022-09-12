from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', show_landing, name='landing'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)