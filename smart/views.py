from django.shortcuts import render
from django.http import HttpResponse

import PoorMansSmartHome.PoorMansSmartHome as p
import time as t
# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    h       = p.Home()
    states  = h.CurrentState()
    states.update({"time" : t.strftime("%H:%M",t.gmtime())})
    return render(request,'index.html',states)

def interface(request,source):
    return render(request,'source.html',{'interface':source,'versions':["today","week","month","all"]})
