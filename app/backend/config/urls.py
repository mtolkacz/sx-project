from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [

    # Zad1 app
    path(
        '',
        include(('sx.zad1.urls', 'zad1'), namespace='zad1')
    ),

    # Zad2 app
    path(
        '',
        include(('sx.zad2.urls', 'zad2'), namespace='zad2')
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


