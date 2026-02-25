from django.shortcuts import render
from .models import Sample

def index(request):
    """
    Template test sayfası. 
    Veritabanındaki Sample nesnelerini resim testi için gönderir.
    """
    samples = Sample.objects.all()
    return render(request, 'index.html', {'sample_list': samples})