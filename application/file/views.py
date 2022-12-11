from django.shortcuts import render

from django.http.response import HttpResponse


def file(request):
    return HttpResponse("file")
