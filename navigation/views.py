from django.shortcuts import render
from navigation.models import *

# Create your views here.
def index(request):
    gonggao = notice.objects.all().order_by('-date')[0]
    fenlei = classify.objects.all().order_by('sort')
    return render(request, 'index.html', {'fenlei': fenlei, 'index': 'index', 'gongao': gonggao})
