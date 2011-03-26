# Create your views here.
from gramy.models import Uczestnik, Granie
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import login, logout, forms as auth_form, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from gramy_utils import *

def lista(request):
    grania = Granie.objects.all()
    return render_to_response('gramy/lista.html', {'grania': grania,
                                                   },context_instance = RequestContext(request))

def login_view(request):
    redirect_to = request.GET.get('next', '/')
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
                                                       'next': redirect_to,
                                                       }, context_instance = RequestContext(request))
  
            
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def szczegoly(request, id):
    granie = Granie.objects.get(id = id)
    uczestnicy = Uczestnik.objects.filter(granie = granie)

    if request.method == 'POST':        
        uczestnik = Uczestnik(nick = request.user, granie = granie, chce = request.POST.get('chce', 2))
        if uczestnik.chce == '1':
            if not Uczestnik.objects.filter(nick = uczestnik.nick, granie = uczestnik.granie).exists():
                uczestnik.save()
               
        if uczestnik.chce == '0':
            if Uczestnik.objects.filter(nick = uczestnik.nick, granie = uczestnik.granie).exists():
                Uczestnik.objects.filter(nick = uczestnik.nick, granie = uczestnik.granie).delete()


        if granie.uczestnik_set.all().count() >= 2:
            if granie.decision == 0:
                granie.decision = 1
                granie.save()
                recipients = ['tofikowy01@gmail.com']

                send_mail4play(granie.decision, recipients) # COMMENT WHEN RUN ON LOCALHOST / UNCOMMENT FOR UPLOAD


#            send_im_chat(message, 'tofikowy01@gmail.com')
#            send_mail('gramy', 'jest granie','korba@autograf.pl', ['tofikowy01@gmail.com']) # django.core
#            mail.send_mail('tomek.filipczuk@gmail.com', ['tofikowy01@gmail.com'], 'gramy', 'jest granie') # google.appengine.api
        if granie.uczestnik_set.all().count() == 1:
            if granie.decision == 1:
                granie.decision = 0
                granie.save()
                recipients = ['tofikowy01@gmail.com']

                send_mail4play(granie.decision, recipients) # COMMENT WHEN RUN ON LOCALHOST / UNCOMMENT FOR UPLOAD

#            send_im_chat(message, 'tofikowy01@gmail.com')
#            send_mail('nie gramy', 'nie ma grania','korba@autograf.pl', ['tofikowy01@gmail.com']) # django.core
#            mail.send_mail('tomek.filipczuk@gmail.com', ['tofikowy01@gmail.com'], 'nie gramy', 'nie ma grania') # google.appengine.api

    return render_to_response('gramy/szczegoly.html', {'granie': granie,
                                                       'uczestnicy': uczestnicy,
                                                       'user': request.user,
                                                       },
                              context_instance = RequestContext(request)
                              )
    
