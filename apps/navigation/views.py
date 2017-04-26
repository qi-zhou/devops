from django.shortcuts import render

from .models import Notice, Classify


# Create your views here.
def index(request):
    gonggao = Notice.objects.all()[0]
    fenlei = Classify.objects.all()

    return render(request, 'index.html', {"gonggao": gonggao, "fenlei": fenlei})

# def lte(request):
#
#     return render(request, 'lte.html')
