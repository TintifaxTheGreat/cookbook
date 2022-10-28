from taggit.models import Tag

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.edit_handlers import FieldPanel
from wagtail import hooks
from wagtail.admin.menu import MenuItem


@hooks.register("register_admin_menu_item")
def register_site_menu_item():
    # TODO improve this
    try:
        return MenuItem(
            ("Add recipe"), "/admin/pages/add/recipes/recipepage/10/", classnames="icon icon-doc-full-inverse", order=0,
        )
    except Exception:
        pass


class TagsModelAdmin(ModelAdmin):
    Tag.panels = [FieldPanel("name")]
    model = Tag
    menu_label = "Tags"
    menu_icon = "tag"
    menu_order = 200
    list_display = ["name", "slug"]
    search_fields = ("name",)


modeladmin_register(TagsModelAdmin)
