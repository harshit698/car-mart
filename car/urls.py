from django.conf.urls import include,url
from django.contrib import admin
from mycollections import views

urlpatterns = [
	url(r'^$',views.IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^cars/',include('mycollections.urls')),
    url(r'^login/$',views.LoginView.as_view(),name="login"),
    url(r'^logout/$',views.end,name="logout"),
    url(r'^userprofile/(?P<user_id>[0-9]+)/$',views.ProfileView.as_view(),name="profile"),
    url(r'^createuser/$',views.CreateUser.as_view())
]
