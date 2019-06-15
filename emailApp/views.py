from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def sendingMail(request):
    print (request.data)
    rec_mail=request.data['email']
    user=request.data['username']
    html_content = render_to_string('secondPage.html',{
                  'user':user
              })
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives('PEHACHAIN Initial Registration', text_content, 'testgtpl4@gmail.com', [rec_mail])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return Response("Success")