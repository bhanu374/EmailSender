from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
def greetings(request):
        return render(request,'index.html')
def contact(request):
       if request.method == "POST":
                Subject_mail = request.POST['subject']
                Message_mail = request.POST['message']
                Email_mail = request.POST['email']
                settings.EMAIL_HOST_USER= request.POST['From']
                settings.EMAIL_HOST_PASSWORD=request.POST['Password']

                send_mail(
                Subject_mail,
                Message_mail,
                settings.EMAIL_HOST_USER,
                [Email_mail],
                fail_silently=False,
                )  
                return HttpResponse("YOUR MAIL SENT SUCCESFULLY!")
                 

