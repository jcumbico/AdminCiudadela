"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from collections import OrderedDict
from django.template import RequestContext
from datetime import datetime
from app.models import Directiva, Proyecto, Evento, Actividad, rptRendicionDeCuentas
from app.fusioncharts import FusionCharts

def inicio(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request = request,
        template_name = 'app/index.html',
        context=
        {
            'title':'Acerca de Nosotros',
            'message':'Se listan los integrantes de las directivas de la ciudadela.',
        }
    )

def nosotros(request):
    """Renders the about page."""
    conjunto = Directiva.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request = request,
        template_name = 'app/nosotros.html',
        context=
        {
            'title':'Acerca de Nosotros',
            'message':'Se listan los integrantes de las directivas de la ciudadela.',
            'conjunto' : conjunto,
        }
    )

def proyectos(request):
    """Renders the home page."""
    conjunto = Proyecto.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/proyectos.html',
        {
            'title':'Proyectos',
            'message':'Lista de los proyectos propuestos y ejecutados en la ciudadela',
            'conjunto':conjunto,
        }
    )

def eventos(request):
    """Renders the home page."""
    conjunto = Evento.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/eventos.html',
        {
            'title':'Eventos',
            'message':'Lista de los eventos realizados y a realizarce en la ciudadela',
            'conjunto':conjunto,
        }
    )

def actividades(request):
    """Renders the home page."""
    conjunto = Actividad.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/actividades.html',
        {
            'title':'Actividades',
            'message':'Lista de las actividades realizadas en la ciudadela',
            'conjunto':conjunto,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Cantáctenos',
            'message':'Datos para que pongan en contacto con nosotros',
            'year':datetime.now().year,
        }
    )

def cuentas(request):
    """Obtener todos los ingresos agrupados por año, tipo de registro, titulo de registro"""
    conjunto = rptRendicionDeCuentas.objects.all().order_by('Orden')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cuentas.html',
        {
            'title':'Rendición de Cuentas',
            'message':'Detalle de los Ingresos e Egresos de la Ciudadela por año',
            'conjunto':conjunto,
        }
    )

def estadisticas(request):
    """Obtener todos los ingresos agrupados por año, tipo de registro, titulo de registro"""
    conjunto = rptRendicionDeCuentas.objects.all().order_by('Orden')

    #Load dial indicator values from simple string array# e.g.dialValues = ["52", "10", "81", "95"]
    dataSource = OrderedDict()

    # The `widgetConfig` dict contains key-value pairs of data for widget attribute
    dialValues = ["49"]

    # widget data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    widgetConfig = OrderedDict()
    widgetConfig["caption"] = "Puntuación de satisfacción de moradores de Las Tejas para 2018"
    widgetConfig["subCaption"] = "250 hogares encuestados (90% del total -300-)"
    widgetConfig["lowerLimit"] = "0"
    widgetConfig["upperLimit"] = "100"
    widgetConfig["showValue"] = "1"
    widgetConfig["numberSuffix"] = "%"
    widgetConfig["theme"] = "fusion"
    widgetConfig["showToolTip"] = "0"
    widgetConfig["exportEnabled"] =  "1"

    # The `colorData` dict contains key-value pairs of data for ColorRange of dial
    colorRangeData = OrderedDict()
    colorRangeData["color"] = [
        {
            "minValue": "0",
            "maxValue": "25",
            "code": "#FF0000"
        },
        {
            "minValue": "25",
            "maxValue": "50",
            "code": "#FFFF00"
        },
        {
            "minValue": "50",
            "maxValue": "75",
            "code": "#32CD32"
        },
        {
            "minValue": "75",
            "maxValue": "100",
            "code": "#0000FF"
        }
    ]

     # Convert the data in the `dialData` array into a format that can be consumed by FusionCharts.
    dialData = OrderedDict()
    dialData["dial"] = []

    dataSource["chart"] = widgetConfig
    dataSource["colorRange"] = colorRangeData
    dataSource["dials"] = dialData

    # Iterate through the data in `dialValues` and insert into the `dialData["dial"]` list.
    # The data for the `dial`should be in an array wherein each element of the 
    # array is a JSON object# having the `value` as keys.
    for i in range(len(dialValues)):
        dialData["dial"].append({
        "value": dialValues[i]
    })

    # Create an object for the angular-gauge using the FusionCharts class constructor
    # The widget data is passed to the `dataSource` parameter.
    grafico01 = FusionCharts("angulargauge", "angulargauge01", "500", "400", "espacio01", "json", dataSource)

    #-----------------------------------

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource2 = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig2 = OrderedDict()
    chartConfig2["caption"] = "Distribución de Egresos durante Octubre 2018"
    chartConfig2["subCaption"] = ""
    chartConfig2["numberSuffix"] = ""
    chartConfig2["theme"] = "fusion"
    chartConfig2["exportEnabled"] =  "1"
    chartConfig2["showValues"]=  "1"
    chartConfig2["enablemultislicing"]= "1"

    # The `chartData` dict contains key-value pairs of data
    chartData2 = OrderedDict()
    chartData2["Sueldos Porteros"] = 2000
    chartData2["Sueldos Jardineros"] = 400
    chartData2["Sueldo Administrador"] = 400
    chartData2["Honorario Contador"] = 200
    chartData2["Mantenimiento de parque"] = 200

    dataSource2["chart"] = chartConfig2
    dataSource2["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData2.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource2["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D2 = FusionCharts("pie3d", "myFirstChart2", "500", "400", "chartContainer2", "json", dataSource2)

    #-----------------------------------

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource3 = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig3 = OrderedDict()
    chartConfig3["caption"] = "Distribución de Ingresos durante Octubre 2018"
    chartConfig3["subCaption"] = ""
    chartConfig3["numberSuffix"] = ""
    chartConfig3["theme"] = "fusion"
    chartConfig3["exportEnabled"] =  "1"
    chartConfig3["showValues"]=  "1"
    chartConfig3["enablemultislicing"]= "1"

    # The `chartData` dict contains key-value pairs of data
    chartData3 = OrderedDict()
    chartData3["Alícuotas"] = 4900
    chartData3["Cuidado de carros"] = 300

    dataSource3["chart"] = chartConfig3
    dataSource3["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData3.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource3["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D3 = FusionCharts("pie3d", "myFirstChart3", "500", "400", "chartContainer3", "json", dataSource3)

    #-----------------------------------

    ##Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource4 = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig4 = OrderedDict()
    chartConfig4["caption"] = "Variación de ingreso durante 2018"
    chartConfig4["subCaption"] = ""
    chartConfig4["xAxisName"] = "Mes"
    chartConfig4["yAxisName"] = "Dinero"
    chartConfig4["numberSuffix"] = ""
    chartConfig4["theme"] = "fusion"
    chartConfig4["exportEnabled"] =  "1"
    chartConfig4["showValues"]=  "1"

    # The `chartData` dict contains key-value pairs of data
    chartData4 = OrderedDict()
    chartData4["Abr"] = 3900
    chartData4["May"] = 3800
    chartData4["Jun"] = 3800
    chartData4["Jul"] = 3800
    chartData4["Ago"] = 3800
    chartData4["Sep"] = 4800

    dataSource4["chart"] = chartConfig4
    dataSource4["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData4.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource4["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D4 = FusionCharts("line", "myFirstChart4", "500", "400", "chartContainer4", "json", dataSource4)

    ##-----------------------------------


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/estadisticas.html',
        {
            'title':'Estadísticas para la toma de decisiones',
            'message':'Cuadros de mando',
            'output' : grafico01.render(),
            'output2' : column2D2.render(),
            'output3' : column2D3.render(),
            'output4' : column2D4.render(),
            #'output5' : column2D5.render(),
            #'output6' : column2D6.render(),
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/nosotros.html',
        {
            'title':'Acerca de Nosotros',
            'message':'',
            'year':datetime.now().year,
        }
    )
