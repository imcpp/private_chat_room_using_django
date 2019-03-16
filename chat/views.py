from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from  django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe
import json
from googletrans import Translator
import enchant

@login_required
def index(request):
    users = User.objects.exclude(username=request.user)

    return render(request, 'chat/index.html', {
    'users': users,
    })

@login_required
def room(request, room_name):
    use1=room_name.split("-")
    use=use1[-1]
    print(use)
    users = User.objects.exclude(username=request.user)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(use1[0])),
        'username': mark_safe(json.dumps(request.user.username)),
        'users': users,
        'use':use,
    })


def home(request):
    return render(request,"home.html")
def login(request):
        username=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)

            return redirect('home')
        else:
            return render(request,'home.html',{'error':'username or password is incorrect'})

def logout(request):
    if request.method=='GET':
        auth.logout(request)
        return redirect('home')

def signup(request):
        if request.POST['password']==request.POST['cpassword'] :
                try:
                    user=User.objects.get(username=request.POST['name'])
                    return render(request,'home.html',{'error':'Username already exist !! Please choose a different one :'})
                except:
                    user=User.objects.create_user(username=request.POST['name'],password=request.POST['password'])
                    #auth.login(request,user)
                    #return HttpResponse('<h1>Home Page<h1>')
                    #return redirect('home')
                    return render(request,'home.html',{'error':'signup successful !!'})

        else:
            return render(request,'home.html',{'error':'password does not match'})


@login_required
def search(request):
    if request.method=='GET':
        lang=request.GET['lang']
        name=request.GET['name']
        print(lang)
        if lang=="hinglish":
            translator = Translator()
            #translator = Translator()
            name=name.strip()
            s=name.split(" ")
            n=s.pop()
            d=enchant.Dict("en_us")
            #s.append("haa ")
            #name=" ".join(s)
            if(d.check(n)):#or if(translator.detect(n)!='en')
                 n=n
            else:
                 n=translator.translate(n,dest='hi').text
                 #r=r.join(s)
                 s.append(n+" ")
                 name=" ".join(s)

            name=name+ " "
            return JsonResponse({'name':name})

        elif lang=="deafult":

            return JsonResponse({'name':name})

        else:
            translator = Translator()
            name=name.strip()
            s=name.split(" ")
            n=s.pop()

            n=translator.translate(n,dest=lang).text
            s.append(n+" ")
            name=" ".join(s)



            return JsonResponse({'name':name+" "})

@login_required
def profile(request):
    users = User.objects.exclude(username=request.user)
    return render(request,"profile.html",{"users":users})
