from __future__ import print_function
import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from twilio.rest import Client
import http.client
from django.core.mail import send_mail
from django.conf import settings
'''from telesign.messaging import MessagingClient'''
from django.core.files.storage import FileSystemStorage
from registerapp.models import App
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
import random
import urllib.request
import urllib.parse
import random
import string
import dropbox
import json
from django_dropbox_storage.storage import DropboxStorage

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def indexView(request):
    return render(request,'index.html')   
def aboutView(request):
    return render(request,'about.html')   


def faqView(request):
    return render(request,'faq.html')  
def change(changed):
        global otp2
        otp2=changed  
@csrf_exempt
def regView(request):
    for instance in App.objects.all():
        if instance.verified==False:
            pk=instance.pk
            pku=App.objects.get(id=pk).owner.pk
            User.objects.get(id=pku).delete()
            App.objects.get(id=pk).delete()
    
    
    if request.method == 'POST' :
        try:
            for_otp = request.POST["for_otp"]
            phone = request.POST["phone"]
            countryCode=request.POST["countryCode"]
            changed=random.randint(1001, 9999)
            change(changed)
            print(str(otp2))
            messagess=str(otp2)
            payload=""
            conn = http.client.HTTPConnection("2factor.in")

            

            headers = { 'content-type': "application/x-www-form-urlencoded" }

            conn.request("GET", "/API/V1/f46fa927-fe61-11e9-9fa5-0200cd936042/SMS/"+str('+')+str(countryCode)+str(phone)+"/"+messagess+"/Upload", payload, headers)
            res = conn.getresponse()
            data = res.read()
            

            print(data.decode("utf-8"))
            print(messagess)
 
        except KeyError as e:
            print(0)
            print(0)
            print(otp2)
            otp=request.POST["otp"]
            print(otp)
            response_data = {
                'message': "failure",
            }
            if str(otp) == str(otp2) :
                print(str(otp))
                print(str(otp2))
                name = request.POST["name"]
                today = datetime.datetime.now()
                password= randomStringDigits(8)
                username=name[0]+name[1]+name[2]
                for x in range(1000):
                    if(not User.objects.filter(username=str(username)+'@'+str(today.month)+'.'+str(today.year)+'_'+str(x))):
                        num=x;
                        break;
                uname=request.POST["uname"]
                email=request.POST["email"]
                phone=request.POST["phone"]
                shortdesc=request.POST["shortdesc"]
                
                user = User.objects.create_user(username=username+'@'+str(today.month)+'.'+str(today.year)+'_'+str(num),first_name=uname,last_name=phone,email=email,password=password)
                user.save()
                images = request.FILES['images']
                
                apk = request.FILES['apk']
                method=request.POST["method"]
                print(method)
                try:
                    appbuilder=request.POST["app-builder"]
                except:
                    appbuilder="NA"

                try:
                    apppub=request.POST["apppub"]
                except:
                    apppub="NA"
                print(apppub)
                print(appbuilder)
                published=request.POST["published"]
                print(published)
                code=request.POST["countryCode"]
                print(code)
                how=request.POST["how"]
                print(how)
                addnl=request.POST["addnl"]
                print(addnl)
                longdesc=request.POST["longdesc"]
                privpolicy=request.POST["privpolicy"]
                promovideo=request.POST["promovideo"]
                username2=username+'@'+str(today.month)+'.'+str(today.year)+'_'+str(num)
                App.objects.create(name=name,images=images,apkfile=apk,countryCode=code,addnl=addnl,published=published,appbuilder=appbuilder,apppub=apppub,method=method,phone=phone,verified=True,owner=user,shortdesc=shortdesc,longdesc=longdesc,privpolicy=privpolicy,promovideo=promovideo)
                subject = 'EntWik login credentials'
                message = 'Username: '+username2+"\n"+'Password: '+password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from, recipient_list )
                print(username2)
                print(password)
                
                
                
                response_data['message'] = 1
                return JsonResponse(response_data)
            else :
                return JsonResponse(response_data)
    return render(request,'form.html')


    




@csrf_exempt
def loginView(request):
    response_data = {
        'message': "failure",
    }
    if request.method == 'POST' :
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        try:
            loginit = authenticate(username=username, password=password)
            login(request, loginit)
            response_data['message'] = 1      
            return JsonResponse(response_data)      
        except:
            return JsonResponse(response_data)

    return render(request,'login.html')


@csrf_exempt
def dashboardView(request):
    response_data = {
        'message': "failure",
    }
    user=request.user
    instance=App.objects.get(owner=user)
    if request.method == 'POST' :
        
        privpolicy = request.POST["privpolicy"]
        promovideo = request.POST["promovideo"]
        email = request.POST["email"]
        shortdesc = request.POST["shortdesc"]
        longdesc = request.POST["longdesc"]
        try:
            newimg=request.FILES["newimg"]
            instance.images=newimg
            instance.save()
        except:
            pass
        user = request.user
        user.email=email
        user.save()
        instance = App.objects.get(owner=user)
        instance.shortdesc=shortdesc
        instance.longdesc=longdesc
        instance.promovideo=promovideo
        instance.privpolicy=privpolicy
        
        instance.save()
        response_data['message'] = 1      
        return JsonResponse(response_data)
    context = {
        'shortdesc':str(instance.shortdesc),
        'longdesc':str(instance.longdesc),
        'privpolicy':str(instance.privpolicy),
        'promovideo':str(instance.promovideo),
        'name':str(instance.name),
        'phone':str(instance.phone),
        'email':str(user.email),
        'images':str(instance.images),
        'pk':str(instance.pk),
        
        
    }
    return render(request,'Dashboard.html',context)
          
@csrf_exempt
def logoutView(request):
    logout(request)
    subject = 'EntWik login credentials'
    message = 'Test \n Data'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ronitraj.tg@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse('Logged Out')






 
 