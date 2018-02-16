from django.conf.urls import url
from Portal import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view())
]