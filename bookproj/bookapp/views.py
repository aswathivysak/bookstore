from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import  Book
from . form import BookForm
# Create your views here.
def index(request):
    book=Book.objects.all()
    context={
        'book':book,
    }
    return render(request,'index.html',context)

def detail(request,bookid):
    book=Book.objects.get(id=bookid)
    return render(request,'detail.html',{'book':book})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        img = request.FILES['img']
        book=Book(name=name,desc=desc,price=price,img=img)
        book.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'book':book,'form':form})

def delete(request,id):
    if request.method=='POST':
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')