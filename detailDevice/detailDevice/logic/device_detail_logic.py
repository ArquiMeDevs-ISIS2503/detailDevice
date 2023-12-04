from ..models import Device



def get_device_by_name(name):
    try:
        device = Device.objects.get(name=name)
        return (device)
    except:
        device = None
        return (device)
