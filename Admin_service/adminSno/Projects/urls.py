from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', show_landing, name='landing'),
    path('projects', show_projects, name='projects'),
    path('people', show_people, name='people'),
    path('project__', show_project, name='profile_project'),
    path('child__', show_child, name='profile_child'),
    path('estimate', show_estimate, name='estimate')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)