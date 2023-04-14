from django.shortcuts import render
from .models import Series
def series(request):
    seriess = Series.objects.all()
    return render(request,'series.html',{'seriess':seriess})
