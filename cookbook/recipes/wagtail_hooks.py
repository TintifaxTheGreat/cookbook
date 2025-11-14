from taggit.models import Tag

from wagtail.admin.panels import FieldPanel
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register


# Conditionally register the menu item only if we can create it safely
def _try_register_add_recipe_menu():
    from recipes.models import RecipeIndexPage

    @hooks.register("register_admin_menu_item")
    def register_add_recipe_menu_item():
        recipe_index = RecipeIndexPage.objects.first()
        return MenuItem(
            "Add recipe",
            f"/admin/pages/add/recipes/recipepage/{recipe_index.pk}/",
            icon_name="doc-full-inverse",
            order=0,
        )


try:
    from recipes.models import RecipeIndexPage

    # Only register if we have a RecipeIndexPage
    if RecipeIndexPage.objects.exists():
        _try_register_add_recipe_menu()
except Exception:
    # If there's any error, just don't register the menu item
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
