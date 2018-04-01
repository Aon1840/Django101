from django.http import HttpResponse
from django.template import loader
from testMySQL.models import Blog

# Create your views here.
def index(request):
    b1 = Blog.objects.filter()
    std = b1[0]
    header_str = "Hello, Python variable"
    template = loader.get_template('index.html')
    context = {
        'var1' : header_str,
        'std' : std

    }
    return HttpResponse(template.render(context, request))