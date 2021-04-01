from django.urls import path
from .apiv1 import views as apiv1_views

urlpatterns = [
    path(
        route='zadanie1/',
        view=apiv1_views.JsonShaDataListAPI.as_view(),
        name='api',
    ),
]
