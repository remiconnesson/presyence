import importlib.resources as resources


def get_website_files():
    print(resources.contents("remi_portal_gun"))
    print(resources.contents("remi_portal_gun.dist"))
    print(resources.contents("remi_portal_gun.dist.assets"))



