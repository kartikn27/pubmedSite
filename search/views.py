from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is Search homepage</h1>")

def documentDetail(request, document_id):
    return HttpResponse("<h2>Details for document id: " + str(document_id) + "</h2>")
