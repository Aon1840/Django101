from django.http import HttpResponse
from django.template import loader
from testMySQL.models import Blog
import json

# Create your views here.
def index(request):
    b1 = Blog.objects.filter()
    std = b1[0]
    header_str = "Hello, Python variable"
    template = loader.get_template('index.html')
    bls = []
    for b in b1 :
        bls.append({
            "name" : b.name,
            "tagline" : b.tagline
        })

    context = {
        'var1' : header_str,
        'std' : bls

    }
    return HttpResponse(json.dumps(context),content_type="application/json")
# def testJson(request):
    # b1 = Blog.o