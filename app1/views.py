from django.shortcuts import render

# Create your views here.
def datarender(request):
    data='This data is our assumption'
    d={'assumption':data}
    return render(request,'data_render1.html',context=d)