from django.shortcuts import render
from django.http.response import HttpResponse


def comment(request):
    return HttpResponse("comment")
