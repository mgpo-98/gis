import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt.settings")
django.setup()
from gis.models import Farm

f = open("gis_1.csv", "r", encoding="cp949")
rdr = csv.reader(f)
cnt = 0
for line in rdr:
    if line[5]:
        
        _farm_num = line[0]
        _farm_name = line[1]
        _lat = line[2]
        if line[4]:
            _distance = line[4]
        
            _long = line[3]
        _result = line[5]
        
        farm = Farm(
            farm_num=_farm_num,
            farm_name=_farm_name,
            lat=_lat,
            long=_long,
            distance=_distance,
            result=_result,
            
        )
        if cnt > 0 :
            farm.save()
        cnt += 1

    print(_farm_name)
   
f.close()
