from django.conf.urls import url
from . import views


app_name="mycollections"

urlpatterns = [
	url(r'^$',views.IndexView.as_view(),name="index"),
	url(r'^buycar/(?P<car_id>[0-9]+)/',views.BuyCar,name="buycar"),
	url(r'^car/detail/(?P<pk>[0-9]+)/$',views.DetailView_Car.as_view(),name="detailcar")
]