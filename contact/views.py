from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        subject = request.POST["subject"]

        send_mail(
            firstname,
            subject,
            email,
            [sharushan0000@gmail.com],
        )


        return render (request , 'contact.html',{"fname":firstname + " We wiil contact you soon."} )

    else:
        return render (request , 'contact.html',{})