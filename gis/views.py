from django.shortcuts import render
from django.db.models import Q
from .models import Farm
from django.http import JsonResponse
# Create your views here.
def index(request):
    farm = Farm.objects.all()

    context ={
       'farm' : farm
    }
    
    return render(request, "gis/index.html",context,)

def search(request, x, y):

    latitude = float(x)
    longitude = float(y)

    # 위도는 0.01이, 경도는 0.015가  약 1km에 해당
    
    condition = Q(latitude__range=(latitude - 0.01, latitude + 0.01)) & Q(
        longitude__range=(longitude - 0.015, longitude + 0.015)
    )

    farms = Farm.objects.filter(condition)

    farmJson = []
    for farm in farms:

        temp = {
            "farm_name": farm.farm_name,
            "lat": farm.lat,
            "long": farm.long,
            "result": farm.result,
        }

        farmJson.append(temp)

    data = {
        "farmJson": farmJson,
    }
    return JsonResponse(data)