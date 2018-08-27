from django.shortcuts import render, render_to_response
from django.http import HttpResponse

import PoorMansSmartHome.PoorMansSmartHome as p
import time as t

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components 
from bokeh.models import LinearColorMapper

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
    df.columns= ['_'.join(col).rstrip('_') for col in df.columns.values]
    df = df.filter(like='state').reset_index()
    x=[];y=[];state=[]                                                           
    for coli,col in enumerate(df.columns):
        for ind in df.index:
            y.append(ind) 
            x.append(coli)
            state.append(df.iloc[ind,coli])
    import pandas as pd
    D = pd.DataFrame.from_dict({"x":x,"y":y,"state":state}) 
    
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors, 
                               low=0, 
                               high=1)

    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
    plt   = figure(title="test",
                   tools=TOOLS,
                   toolbar_location='below',
                   tooltips=[('date', '@x @y'),('state', '@state%')])

    plt.rect(x="x", y="y", width=1, height=1, source=D, fill_color={'field':'state', 'transform': mapper})
    plt.grid.grid_line_color = None
    plt.axis.axis_line_color = None
    plt.axis.major_tick_line_color = None
    plt.axis.major_label_text_font_size = "5pt"
    plt.axis.major_label_standoff = 0
    plt.xaxis.major_label_orientation = 3.14 / 3
    
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
