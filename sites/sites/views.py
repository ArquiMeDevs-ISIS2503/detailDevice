from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SiteForm
from .logic.site_logic import get_sites, create_site
from django.http import JsonResponse


def site_list(request, name):
    sites = get_sites()
    context = {}
    
    for site in sites:
        if site.name == name:
            context['site'] = {'id': site.id, 'name': site.name}
            
    # Si no se encuentra la sede, devuelve una respuesta vacía
    return JsonResponse(context, safe=False)

def site_list(request):
    sites = get_sites()
    context = {'sites': list(sites.values('id', 'name'))}

    # Si no se encuentra la sede, devuelve una respuesta vacía
    return JsonResponse(context, safe=False)
    

def site_create(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            create_site(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created site')
            return HttpResponseRedirect(reverse('sites:siteCreate'))
        else:
            print(form.errors)
    else:
        form = SiteForm()

    context = {
        'form': form,
    }
    return render(request, 'Site/siteCreate.html', context)