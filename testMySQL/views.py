from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from testMySQL.models import Blog
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    b1 = Blog.objects.filter()
    # header_str = "Hello, Python variable"
    # template = loader.get_template('index.html')
    bls = []
    for b in b1 :
        bls.append({
            "name" : b.name,
            "tagline" : b.tagline
        })

    context = {
        # 'var1' : header_str,
        'std' : bls

    }
    return HttpResponse(json.dumps(context),content_type="application/json")

@csrf_exempt
def sendData(request):
    if(request.method == "POST"):
        data = request.POST
        paramsName = data["name"]
        paramsTagline = data["tagline"]
        newData = Blog(name=paramsName,tagline=paramsTagline)
        newData.save()
        response_data = {
            "result":"ok",
            "method":request.method
        }
    else:
        response_data = {
            "result" : "fail",
            "method" : request.method
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
