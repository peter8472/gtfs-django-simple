# Create your views here.
from django.http import HttpResponse
from django.template import Context,loader
from bus.models import Routes,Stops,Calendar,StopTimes,Trips,Shapes
from pdb import set_trace
from datetime import datetime


def index(request):
    tmp  = Routes.objects.all().values()
    all_routes_list = [i for i in tmp]

    t =loader.get_template("bus/routes.html")
    c = Context( {
	   'all_routes_list':all_routes_list } )

    return HttpResponse(t.render(c))

def calendar(request):
    object_list = Calendar.objects.filter(
		start_date__lte=datetime.now()).filter(
		saturday="1").filter(end_date__gte=datetime.now())
    object_list = Calendar.nowmanager.all()

    t =loader.get_template("bus/calendar.html")
    c = Context( {
 	   'request': request,
	   'object_list':object_list } )

    return HttpResponse(t.render(c))

def mytrip(request):
    object_list = Calendar.nowmanager.all()
    mytrip = object_list[0].getService()
    mytrip_id = Trips.objects.filter(route_id = '45'	)
    stop_times = StopTimes.objects.filter(trip_id = mytrip_id[0].trip_id)
#    stop_times = StopTimes.objects.filter(trip_id = 45)
    t = loader.get_template("bus/mytrip.html")
    c = Context({	 'stop_times':stop_times     })
    return HttpResponse(t.render(c))


def map(request):
    object_list = Shapes.objects.filter(shape_id = 18675)
    t = loader.get_template("bus/map.html")
    c = Context({   'shape':object_list } )
    return HttpResponse(t.render(c))
