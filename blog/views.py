# -*- coding: utf-8 -*-
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
# from blog.models import Book
from django.shortcuts import render
from django.template import loader
from django.db import connection

def student(request):
    t = loader.get_template('student.html')
    # 此处有改进,直接dict装上就行
    c = {
        'title': 'student score list',
        'student':['jimmy','tom','bob','rose'],
        'score': [58, 100, 70, 50],
    }
    return HttpResponse(t.render(c))

def copyright(request):
    t = loader.get_template('copyright.html')
    return HttpResponse(t.render())

def base(request):
    t = loader.get_template('base.html')
    return HttpResponse(t.render())

def home(request):
    t = loader.get_template('home.html')
    return HttpResponse(t.render())

def index(request):

    t = loader.get_template('index.html')
    list1 = [3,5,9,12,143,14154,1413,231]
    c = {'list':list1,'word':'hello','str':'word'}
    return HttpResponse(t.render(c))

def insert(request):
    cursor = connection.cursor()
    cursor.execute("Insert into JavaWebUI.dbo.blog_user(manager,name,ms,type,stop,addDate) values(123123,'zyq','saf',1,0,'2019-03-19')")
    return render(request,'insert.html')

from blog.models import Book
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)