from ..logic.site_logic import get_site_by_name, create_site, create_site_object

# this function return site id. If the site does not exist, then it is created


def get_site(name):
    site = get_site_by_name(name)
    if site != None:
        return (site)
    else:
        site = create_site_object(name)
        return (site)
