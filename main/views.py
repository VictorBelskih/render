from django.shortcuts import render
from .models import News, Slides,Articles
from django.core.mail import send_mail
from .forms import FeedbackForm
from django.conf import settings


def index(request):
    news = News.objects.order_by('-id')[:6]
    slide = Slides.objects.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Обратная связь',
                f'Имя: {name}\nEmail: {email}\nСообщение: {message}',
                settings.EMAIL_HOST_USER,
                ['belskih15@gmail.com'],  # Замените на адрес получателя
            )
            return render(request, 'AgroChemical/success.html')
    else:
        form = FeedbackForm()
    context = {'news': news, 'slide': slide, 'form': form}
    return render(request, 'AgroChemical/index.html', context)


def about(request):
    article = Articles.objects.filter(category='1')
    return render(request, 'AgroChemical/about.html', {'article': article})

def analyspojv(request):
    article = Articles.objects.filter(category='2')
    return render(request, 'AgroChemical/analyspojv.html', {'article': article})

def analyswater(request):
    article = Articles.objects.filter(category='3')
    return render(request, 'AgroChemical/analyswater.html', {'article': article})

def analysudob(request):
    article = Articles.objects.filter(category='4')
    return render(request, 'AgroChemical/analysudob.html', {'article': article})

def analyskorm(request):
    article = Articles.objects.filter(category='5')
    return render(request, 'AgroChemical/analyskorm.html', {'article': article})

def gis(request):
    article = Articles.objects.filter(category='6')
    return render(request, 'AgroChemical/gis.html', {'article': article})

def securityplant(request):
    article = Articles.objects.filter(category='7')
    return render(request, 'AgroChemical/securityplant.html',{'article': article})
def monitoring(request):
    article = Articles.objects.filter(category='8')
    return render(request, 'AgroChemical/monitoring.html',{'article': article})
