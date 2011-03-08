# Create your views here.
from gramy.models import Uczestnik, Granie
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import login, logout, forms as auth_form, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User

def lista(request):
    grania = Granie.objects.all()
    return render_to_response('gramy/lista.html', {'grania': grania,
                                                   })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = auth_form.AuthenticationForm()
        return render_to_response('gramy/login.html', {'form': form,
                                                       'next': request.GET['next'],
                                                       }, context_instance = RequestContext(request))
        
            
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def szczegoly(request, id):
    granie = Granie.objects.get(id = id)
    uczestnicy = Uczestnik.objects.all()

    if request.method == 'POST':
        uczestnik = Uczestnik(nick = request.user, granie = granie, chce = request.POST['chcesz'])
        print uczestnik.chce
        if uczestnik.chce == '1':
            print uczestnicy
            print uczestnik
            if Uczestnik.objects.filter(nick = uczestnik, granie = granie).exists():
                print 'juz takiego mamy'         
            else:
                print 'trzeba zapisac'
            

    return render_to_response('gramy/szczegoly.html', {'granie': granie,
                                                       'uczestnicy': uczestnicy,
                                                       'user': request.user,
                                                       }, context_instance = RequestContext(request))
