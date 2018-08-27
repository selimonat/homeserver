from django.shortcuts import render, render_to_response
from django.http import HttpResponse

import PoorMansSmartHome.PoorMansSmartHome as p
import time as t

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    h       = p.Home()
    df      = h.CurrentState_as_df(last_row=10)
    #last log entries
    states  = p.tuplekey_to_nested(df.to_dict())
    #add time info
    states.update({"time" : t.strftime("%H:%M",t.gmtime())})
    #add image path
    states.update({"file" : {"home_visual"   : "0.JPG",
                             "motion_energy" : "motion_energy.JPG"}})
    #get the imagematrix to visualize
    plt = figure(title="test")
    plt.rect(df)
    script, div = components(plt)     
    
    states.update({"script" : script,"div" : div})
    return render(request,'index.html',states)

def interface(request,source):
    #load source's  DF
    h       = p.Home()

    script,div = h.get_plot(source)
    return render(request,'source.html',
            {'script' : script , 'div' : div} )
def test(request):
    d = {tuple(("bla",)):12,"bla2":13}
    print(d)
    return render(request,'test.html',d)
