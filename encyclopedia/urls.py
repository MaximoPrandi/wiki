from django.urls import path

from .views import index_view, search_view, entry_view, new_view, edit_view

app_name = "encyclopedia"
urlpatterns = [
    path("", index_view, name="index"),
    path("search", search_view, name="search"),
    path("new", new_view, name="new"),
    path("edit/<str:entry>", edit_view, name="edit"),
    path("<str:entry>", entry_view, name="entry")
]
