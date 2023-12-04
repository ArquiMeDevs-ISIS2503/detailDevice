from ..models import Site


def get_sites():
    queryset = Site.objects.all()
    return (queryset)


def create_site(form):
    measurement = form.save() # TODO: PORQUE NOS TOCA CREAR LA VARIABLE DESDE LA PAGINA DE MEDICIONES?
    measurement.save()
    return ()

def create_site_object(nombre):
    site = Site()
    site.name = nombre
    site.save()
    return (site)


def get_site_by_name(name):
    try:
        site = Site.objects.get(name=name)
        return (site)
    except:
        site = None
        return (site)
