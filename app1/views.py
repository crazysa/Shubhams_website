from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Hi , Shubham Here 🙋‍♂️🙋‍♂️")

def createdate(request):
    return HttpResponse("I started creating the page on 10th sept 2021")

def aboutme(request):
    Text = "As of sept 2021 I am working at arcesium india pvt ltd as a Software Engineer.Here I am working using python and mysql and mostly deal with internal framework , automation , infra and testing of Glo tao app which is an accounts reconcilation service used by hedge funds(ya the Big guys!!)"
    return HttpResponse(Text)