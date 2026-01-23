from django.shortcuts import render
from .models import Sample  # Sample modelini import ediyoruz

def index(request):
    # Veritabanındaki tüm Sample objelerini çekiyoruz
    samples = Sample.objects.all()
    
    # context sözlüğü ile verileri template'e gönderiyoruz
    context = {
        'sample_list': samples
    }
    return render(request, 'index.html', context)