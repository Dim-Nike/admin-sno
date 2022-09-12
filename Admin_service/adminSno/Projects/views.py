from django.shortcuts import render
from django.contrib.auth import logout
from django.core.mail import send_mail
import qrcode
from django.shortcuts import render, redirect
from xhtml2pdf import pisa
from .models import *
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseNotFound, Http404, FileResponse


def show_landing(req):
    data = {
        'title_page': 'Меню'
    }

    return render(req, 'Projects/landing.html', data)


def show_people(req):
    data = {
        'title_page': 'Меню'
    }

    return render(req, 'Projects/people_page.html', data)


def show_projects(req):
    data = {
        'title_page': 'Меню'
    }

    return render(req, 'Projects/projects_page.html', data)