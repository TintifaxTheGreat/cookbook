from taggit.models import Tag

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.edit_handlers import FieldPanel
from wagtail import hooks
from wagtail.admin.menu import MenuItem


@hooks.register("register_admin_menu_item")
def register_site_menu_item():
    return MenuItem(
        ("Add recipe"), "/admin/pages/add/recipes/recipepage/10/", classnames="icon icon-doc-full-inverse", order=0,
    )


class TagsModelAdmin(ModelAdmin):
    Tag.panels = [FieldPanel("name")]  # only show the name field
    model = Tag
    menu_label = "Tags"
    menu_icon = "tag"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ["name", "slug"]
    search_fields = ("name",)


modeladmin_register(TagsModelAdmin)
