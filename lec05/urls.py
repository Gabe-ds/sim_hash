from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = "lec05"

urlpatterns = [
    path('upload_list/<int:pk>/detail/', views.DetailView.as_view(), name="detail"),
    path('ahash_list/', views.AHashListView.as_view(), name="ahash_list"),
    path('do_ahash/', views.DoAHashView.as_view(), name="do_ahash"),
    path('ahash_list/<int:pk>/delete/', views.DeleteView.as_view(), name="delete"),
]