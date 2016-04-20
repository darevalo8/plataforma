from django.conf.urls import url
from apps.conquers import views
from .views import AddNota
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/(?P<pk>\d+)$', views.register, name="register"),
    url(r'^login$', views.user_login, name="login"),
    url(r'^logout$', views.user_logout, name="logout"),
    url(r'^actividad/envio$', views.envio_actividad, name="activity"),
    url(r'^actividad/ver$', views.consulta_activity, name="view"),
    url(r'^actividad/dowload/(?P<pk>\d+)$', views.descarga_documentos, name='download'),
    url(r'^logros/agregar$', AddNota.as_view(), name="nota"),
    url(r'^discusiones$', views.discusiones, name="discus"),
    url(r'^consulta$', views.tabla_puntuaciones, name="consulta")


]