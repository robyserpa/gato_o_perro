# existing imports
from django.urls import path
from django.conf.urls import url
from apiSNN import views

urlpatterns = [
    path('imagenes/', views.ListImage.as_view()),
    path('libros/', views.ListLibro.as_view()),
    path('libros/<int:pk>/', views.DetailLibro.as_view()),
    path('personas/', views.ListPersona.as_view()),
    path('personas/<int:pk>/', views.DetailPersona.as_view()),
    url(r'^sobrevivencia/$',views.Clasificacion.determinarSobrevivencia),
    url(r'^predecir/',views.Clasificacion.predecir),
    url(r'^$',views.Autenticacion.singIn),
    url(r'^postsign/',views.Autenticacion.postsign),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)