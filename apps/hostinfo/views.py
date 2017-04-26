from django.shortcuts import render

# Create your views here.
from .models import Host


# Createyourviewshere.
def hostinfo(request):
    hosts = Host.objects.all()

    # if request.method == 'POST':
    #     hostname = request.POST.get('hostname')
    #     ip = request.POST.get('ip')
    #     osversion = request.POST.get('osversion')
    #     memory = request.POST.get('memory')
    #     disk = request.POST.get('disk')
    #     cpu_core = request.POST.get('cpu_core')
    #
    #     host = Host()
    #     host.hostname = hostname
    #     host.ip = ip
    #     host.osversion = osversion
    #     host.memory = memory
    #     host.disk = disk
    #     host.cpu_core = cpu_core
    #     host.save()
    #
    # else:
    #     return render(request, "host.html", {})
    # print host.hostname
    return render(request, 'host.html', {"hostsinfo": hosts})
