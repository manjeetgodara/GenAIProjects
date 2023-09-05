from django.shortcuts import render, redirect

mydata={}

# Create your views here.

def create(request):
    if request.method=='POST':
        key=request.POST.get('key')
        value=request.POST.get('value')
        mydata[key]=value
        return redirect('/read')
    return render(request,'create.html')
    
def update(request):
    if request.method=='POST':
        key=request.POST.get('key')
        value=request.POST.get('value')
        mydata[key]=value
        return redirect('/read')
    return render(request,'update.html')    

def delete(request):
    if request.method == 'POST':
        keys_to_delete = request.POST.getlist('key')
        for key in keys_to_delete:
            if key in mydata:
                del mydata[key]
        return redirect('/read')
    return render(request, 'delete.html')


def read(request):
    return render(request,'read.html',{'data':mydata})
        

