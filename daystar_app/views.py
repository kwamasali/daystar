from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'daystar-app/home.html')


def display(request):
    return render(request, 'daystar-app/displays.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'daystar-app/signup.html'

@login_required
def babies(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
       
        if form.is_valid():
            new_name = form.save(commit=False)
            new_name.save()
            return redirect('/')
        
    else:
        form = BabyForm()
        return render(request, 'daystar-app/babies.html', {'form':form})
    
def babydisplay(request):
    baby = Babies.objects.all()
    return render(request, 'daystar-app/all-babies.html', {'baby':baby})

@login_required    
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
       
        if form.is_valid():
            new_payee = form.save(commit=False)
            new_payee.save()
            return redirect('/')
        
    else:
        form = PaymentForm()
        return render(request, 'daystar-app/payment.html', {'form':form})
    
def paymentdisplay(request):
    payments = Payment.objects.all()
    return render(request, 'daystar-app/all-payments.html', {'payments':payments})

@login_required   
def sitter(request):
    if request.method == 'POST':
        form = SittersForm(request.POST)
       
        if form.is_valid():
            new_sitter = form.save(commit=False)
            new_sitter.save()
            return redirect('/')
        
    else:
        form = SittersForm()
        return render(request, 'daystar-app/sitters.html', {'form':form})
    
def sitterdisplay(request):
    sitters = Sitter.objects.all()
    return render(request, 'daystar-app/all-sitters.html', {'sitters':sitters})
        
@login_required
def dollshop(request):
    if request.method == 'POST':
        form = DollsForm(request.POST)
       
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            return redirect('/')
        
    else:
        form = DollsForm()
        return render(request, 'daystar-app/dolls-shop.html', {'form':form})
    
def inventorydisplay(request):
    inventory = DollsShop.objects.all()
    return render(request, 'daystar-app/all-inventory.html', {'inventory':inventory})
    
def logoutview(request):
    logout(request)
    return render(request, 'daystar-app/home.html')
    
@login_required
def checkin(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
       
        if form.is_valid():
            new_baby = form.save(commit=False)
            new_baby.save()
            return redirect('/')
        
    else:
        form = CheckinForm()
        return render(request, 'daystar-app/checkin.html', {'form':form}) 
    
def checkindisplay(request):
    checkins = CheckIn.objects.all()
    return render(request, 'daystar-app/all-checkins.html', {'checkins':checkins})



