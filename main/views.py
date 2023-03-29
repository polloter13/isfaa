from django.shortcuts import render
from .forms import MessageForm
from django.core.mail import send_mail
from .models import Plants, Plant, Texnika, Model, Tool, Gübre, Watering, Watering_tool
from django.http import Http404
import datetime


alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'ə', 'f', 'g', 'ğ', 'h', 'x', 'ı', 'i', 'j',
            'k', 'q', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']


def index(request):
    if 'q' not in request.GET:
        link = 'home'
        context = {
            'link': link
        }
        return render(request, 'main/index.html', context)
    q = request.GET.get('q')
    fertilizers = Gübre.objects.filter(name__contains=q)
    plants = Plants.objects.filter(name__contains=q)
    plant = Plant.objects.filter(name__contains=q)
    watering = Watering.objects.filter(name__contains=q)
    tools = Tool.objects.filter(name__contains=q)
    texnikas = Texnika.objects.filter(ad__contains=q)
    context = {
        'plant': plant,
        'plants': plants,
        'fertilizers': fertilizers,
        'watering': watering,
        'tools': tools,
        'texnikas': texnikas,
    }

    return render(request, 'main/search.html', context)


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            print(email)
            content = request.POST.get('content')
            months = {
                1: 'Yanvar',
                2: 'Fevral',
                3: 'Mart',
                4: 'Aprel',
                5: 'May',
                6: 'Iyun',
                7: 'Iyul',
                8: 'Avqust',
                9: 'Sentyabr',
                10: 'Oktyabr',
                11: 'Noyabr',
                12: 'Dekabr',

            }
            send_mail(subject='Websitenizden Yeni Mesajınız var', from_email='mehemmed05.aliyev@gmail.com', message='''
                    Ad: {}
                    E-Poçt: {}
                    Mesaj: {}
                    ---
                    Date: {}
                    Time: {}
                    '''.format(name, email, content, months[datetime.datetime.now().month], datetime.datetime.now().strftime("%H:%M")),
                      recipient_list=['info@isfa.az'])
            form.save()
    link = 'contact'
    form = MessageForm()
    context = {
        'form': form,
        'link': link,
    }
    return render(request, 'main/contact.html', context)


def gallery(request):
    link = 'gallery'
    context = {
        'link': link
    }
    return render(request, 'main/gallery.html', context)


def about(request):
    link = 'about'
    context = {
        'link': link
    }
    return render(request, 'main/about.html', context)


def plants(request):
    plants = Plants.objects.all()
    numbered_list = {}
    for x in plants:
        numbered_list[x] = ''.join(x.name.strip().lower().split(' '))

    link = 'plants'
    context = {
        'link': link,
        'plants': numbered_list,
    }
    return render(request, 'main/plants.html', context)


def plant_type(request, id):
    try:
        plant = Plants.objects.get(id=id)
    except:
        raise Http404

    plant_type = Plant.objects.filter(parent=plant)
    link = 'plants'
    context = {
        'parent': plant,
        'plant': plant_type,
        'link': link,
    }
    return render(request, 'main/plant.html', context)


def type(request, id):
    try:
        type = Plant.objects.get(id=id)
    except:
        raise Http404
    parent = Plants.objects.get(id=type.parent.id)
    other_types = list(filter(lambda x: x.id != type.id,
                       Plant.objects.filter(parent=parent)))[0:5]
    link = 'plants'

    context = {
        'parent': parent,
        'type': type,
        'other_types': other_types,
        'link': link,
    }
    return render(request, 'main/type.html', context)


def techniques(request):
    link = 'village'
    context = {
        'link': link,
    }
    return render(request, 'main/techniques.html', context)


def texnika(request):
    texnika = Texnika.objects.all()
    link = 'village'
    context = {
        'texnika': texnika,
        'link': link,
    }
    return render(request, 'main/texnika.html', context)


def texnika_tool(request, id):
    try:
        texnika = Texnika.objects.get(id=id)
    except:
        raise Http404
    model = Model.objects.filter(texnika=texnika)
    count = model.count()
    link = 'village'
    context = {
        'texnika': texnika,
        'model': model,
        'link': link,
        'count': count,
    }
    return render(request, 'main/texnika_model.html', context)


def tools(request):
    link = 'village'
    tools = Tool.objects.all()
    context = {
        'link': link,
        'tools': tools,
    }
    return render(request, 'main/tools.html', context)


def news(request):
    link = 'news'
    context = {
        'link': link,
    }
    return render(request, 'main/news.html', context)


def fertilizers(request):
    data = Gübre.objects.all()
    link = 'fertilizer'
    context = {
        'data': data,
        'link': link,
    }
    return render(request, 'main/fertilizers.html', context)


def fertilizer_item(request, id):
    try:
        item = Gübre.objects.get(pk=id)
    except:
        raise Http404
    link = 'fertilizer'
    context = {
        'link': link,
        'item': item,
    }

    return render(request, 'main/fertilizer_item.html', context)


def watering(request):
    link = 'watering'
    data = Watering.objects.all()
    context = {
        'link': link,
        'data': data,
    }

    return render(request, 'main/watering.html', context)


def watering_item(request, id):
    try:
        item = Watering.objects.get(pk=id)
    except:
        raise Http404
    link = 'watering'
    context = {
        'item': item,
        'link': link,
    }
    return render(request, 'main/watering_item.html', context)
