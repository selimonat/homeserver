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
    states  = h.CurrentState()
    states.update({"time" : t.strftime("%H:%M",t.gmtime())})
    return render(request,'index.html',states)

def interface(request,source):
    #load source's  DF
    h       = p.Home()

    script,div = h.get_plot(source)
    return render(request,'source.html',
            {'script' : script , 'div' : div} )

def test(request):
    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title , 
        x_axis_label= 'X-Axis', 
        y_axis_label= 'Y-Axis')

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    #Store components 
    script, div = components(plot)

    #Feed them to the Django template.
    return render_to_response( 'test.html',
            {'script' : script , 'div' : div} )
