from django.shortcuts import render
from .models import Contact

# Create your views here.



def contact(request):
    if request.method =='POST':
        
        v_name = request.POST.get('name')
        v_email = request.POST.get('email')
        v_message = request.POST.get('message')

        v_contact = Contact (name = v_name , email = v_email , message = v_message)
        v_contact.save() 
        return render (request, 'contact/thank.html' ) 


    else: 
        return render (request,'contact/contact.html')

