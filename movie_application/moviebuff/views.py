from django.shortcuts import render,HttpResponse
from .forms import MovieForms
from .models import CreateMovie

# Create your views here.
def Create(request):
    if request.POST:
        frm=MovieForms(request.POST)
        frm.save()
        return List(request)
        
    frm=MovieForms()
    return render(request,'create.html',{'frm':frm})



def List(request):
    movie_lists = CreateMovie.objects.all()

    return render(request,'list.html',{'movie_list':movie_lists})



def edit(request,pk):
    instance_edit = CreateMovie.objects.get(pk=pk)
    if request.POST:
        edited_data=MovieForms(request.POST,instance=instance_edit)
        if edited_data.is_valid():
            edited_data.save()
            return List(request)
       
    else:
        
        frm=MovieForms(instance=instance_edit)
        return render(request,'create.html',{'frm':frm})

        

    



def delete(request,pk):
    instance=CreateMovie.objects.get(pk=pk)
    instance.delete()
    return List(request)
   
 
