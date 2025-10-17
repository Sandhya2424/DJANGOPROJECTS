from django.shortcuts import render,redirect

# Create your views here.


from django.shortcuts import render


from app1.forms import MovieForm
from app1.models import Moviedetail

def home(request):
    return render(request, 'home.html')

def addmovie(request):
    if (request.method == 'POST'):
        form_instance = MovieForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addmovie.html')
    if(request.method=="GET"):
        form_instance=MovieForm()
        context={'form':form_instance}
    return render(request, 'addmovie.html',context)

def movielist(request):
    movies=Moviedetail.objects.all()  # get first 6 movies
    context={'movies':movies}
    return render(request,'movielist.html',context)

def moviedetail(request, i):
    movie = Moviedetail.objects.get(id=i)
    return render(request, 'moviedetail.html', {'movie': movie})

def updatemovie(request, i):
    if request.method == 'POST':
        movie=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(request.POST, request.FILES, instance=movie)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('app1:movielist')
    if(request.method=="GET"):
        movie=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(instance=movie)
        context={'form':form_instance}
        return render(request, 'updatemovie.html',context)

def deletemovie(request, i):
    movie = Moviedetail.objects.get(id=i)
    movie.delete()
    return redirect('app1:movielist')
