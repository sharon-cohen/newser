from django.shortcuts import render
from .models import Job
import time
from pywand import Wand, wm_msg, WandPowerStates, WandStates

def index(request):
    jobs = Job.objects.all()
    
   
    return render(request, 'job/home.html', {'jobs': jobs})
def start(request):
    jobs = Job.objects.all()
    try:
        wand = Wand("192.168.1.100")
        while True:
            time.sleep(2)
            print(wand.get_state()[0])
            if wand.get_state()[0] == WandStates.WS_STANDBY:

                break
    except:
        print("fail")
    print("start")
    return render(request, 'job/home.html', {'jobs': jobs})
