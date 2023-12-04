from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .logic.device_detail_logic import get_device_by_name


def device_detail(request):
    device_detail = get_device_by_name('device1')
    context = {
        'device_detail': device_detail
    }
    return render(request, 'deviceDetail/deviceDetail.html', context)

