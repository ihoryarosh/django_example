from django.shortcuts import render
from .models import Job
from django.http import HttpResponse

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'page_denis_vorko/index.html', context={'jobs':jobs})


def about(request):
    job = Job.objects.get(title=request.path.split('/')[-1])
    return render(request, 'page_denis_vorko/about.html', context={'job':job})

    
