import json
from .models import Site
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SiteForm
from .logic.site_logic import get_sites, create_site
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def get_site_by_name(request, name):
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
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_site_name(data_json):
            site = Site()
            site.name = data_json['name']
            site.save()
            return HttpResponse("Site created successfully")
        else:
            return HttpResponse("Site name already exists")

def check_site_name(data):
    if 'name' in data:
        name = data['name']
        sites = get_sites()
        for site in sites:
            if site.name == name:
                return False
        return True
    return False

@csrf_exempt
def site_delete_by_id(request, id):
    if request.method == 'DELETE':
        sites = get_sites()
        for site in sites:
            if site.id == id:
                site.delete()
                return HttpResponse("Successfully deleted site")
        return HttpResponse("Site not found")
    return HttpResponse("Invalid request")