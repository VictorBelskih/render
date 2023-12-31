from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("success", views.index, name="success"),
    path("analyspojv", views.analyspojv, name="analyspojv"),
    path("analysudob", views.analysudob, name="analysudob"),
    path("analyswater", views.analyswater, name="analyswater"),
    path("analyskorm", views.analyskorm, name="analyskorm"),
    path("gis", views.gis, name="gis"),
    path("securityplant", views.securityplant, name="securityplant"),
    path("monitoring", views.monitoring, name="monitoring"),
    path("servicezone", views.servicezone, name="servicezone"),
    path("docs", views.docs, name="docs"),
    path("useudob", views.useudob, name="useudob"),
    path("ecomonitoring", views.ecomonitoring, name="ecomonitoring"),
    path("acredits", views.acredits, name="acredits"),
    path("isdania", views.isdania, name="isdania"),
    path("news", views.news, name="news"),
    path("media", views.media, name="media"),
    path("articles", views.articles, name="articles"),
    path('new/<int:id>/', views.new, name='new')
]

# Create your views here.