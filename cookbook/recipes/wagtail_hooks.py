from django.urls import reverse

from wagtail import hooks
from wagtail.admin.menu import MenuItem

@hooks.register("register_admin_menu_item")
def register_site_menu_item():
    return MenuItem(
        ("Add recipe"), "/admin/pages/add/recipes/recipepage/10/", classnames="icon icon-doc-full-inverse", order=0,
    )