from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    contacts = Contact.objects.order_by("-name")[:10]
    context = {"contacts": contacts}
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, "contacts/detail.html", {"contact": contact})


def create(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('phone_number') and request.POST.get('email'):
            contact = Contact()
            contact.name = contact.name.get(pk=request.POST['name'])
            contact.surname = contact.surname.get(pk=request.POST['surname'])
            contact.phone_number = contact.phone_number.get(pk=request.POST['phone_number'])
            contact.email = contact.email.get(pk=request.POST['email'])
            contact.save()

            return HttpResponseRedirect(reverse('create', args={contact, }))
    else:
        return render(request, 'contacts/create.html')
