from taggit.models import Tag

from wagtail.admin.panels import FieldPanel
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register


@hooks.register("register_admin_menu_item")
def register_site_menu_item():
    try:
        return MenuItem(
            ("Add recipe"),
            "/admin/pages/add/recipes/recipepage/10/",
            classnames="icon icon-doc-full-inverse",
            order=0,
        )
    except Exception:
        return None


class TagsModelAdmin(ModelAdmin):
    Tag.panels = [FieldPanel("name")]
    model = Tag
    menu_label = "Tags"
    menu_icon = "tag"
    menu_order = 200
    list_display = ["name", "slug"]
    search_fields = ("name",)


modeladmin_register(TagsModelAdmin)
