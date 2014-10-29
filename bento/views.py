from django.shortcuts import render,render_to_response,redirect,RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import request
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from rest_framework.mixins import *
from rest_framework.permissions import IsAuthenticated
#from django.db.models import Sum
import pdb
from thali.settings import *
import math
#from django.db.models import Sum,Count
from datetime import datetime, timedelta
from django.core.mail import send_mail
from rest_framework.decorators import *
#from registration.backends.simple.views import RegistrationView
#from forms import TakeawayProfileRegistrationForm
#from notifications.models import Notification
# Create your views here.

@api_view(['POST','GET'])
@permission_classes(())
def send_email_thali(request):


    from_email = request.POST.get('from_email', None)
    to_email = request.POST.get('to_email',None)
    order_info = request.POST.get('order_info',None)
    chef_info = request.POST.get('chef_info',None)
    result = 'SUCCESS'
    recipients = ['ravi.dutta@gmail.com','suresh.atluri@gmail.com','f2003484@gmail.com','varrekeerthi@gmail.com']
    recipients.append(to_email)
    subject = 'HOMETHALI CUSTOMER ORDER'

    if from_email :   
    	subject = subject + ' IS GOOD'    	
    	
    else :
    	result = 'SUCCESS'
    	subject = subject + ' HAS GONE BAD. NO FROM_EMAIL FOUND.'

    	
    body = 'You have got an order from ' + str(from_email) + '\n' + str(order_info)  + '\n' + 'CHEF INFO :' + '\n' + str(chef_info)
    #send_mail(subject, email , 'support@mbatakeaways.com', recipients)

    return Response({"result": body })