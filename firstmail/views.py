from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import *
# Create your views here.

def sendmail(request):
	html_content='enter the content'
	notification='check your mail'
	send_mail('send mail',html_content,settings.EMAIL_HOST_USER,['natakala.saimahitha@gmail.com'], fail_silently=False)
	return HttpResponse('check your mail')
