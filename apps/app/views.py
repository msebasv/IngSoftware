from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from .forms import eventForm
from django.http import HttpResponse

# Create your views here.
class Dashboard(TemplateView):
    template_name = 'dashboard.html'

def index(request):
    return render(request, 'html/jinja2/index.j2')

def send_email(request):
    form_contact = eventForm()
    if request.method == 'POST':
        form_contact = eventForm(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content =request.POST.get('content')
            email = EmailMessage( "Mensaje de app Django","El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".format(name,email,content),"",[email], reply_to=['appsieun@gmail.com'])
            try:
                email.send()
                return redirect('sent_email')
            except:
                return HttpResponse('<h1>Hubo un error</h1>')
    return render(request,'html/jinja2/emailForm.j2',{
        'form':form_contact
    })