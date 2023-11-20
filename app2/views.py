from django.shortcuts import render

# Create your views here.
def submit(request):
    data='This data is our assumption'
    d={'key':data}
    return render(request,'data_render2.html',context=d)