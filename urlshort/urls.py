from django.contrib import admin
from django.conf.urls import url
from short.views import HomeView ,KirrCBVView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$',KirrCBVView.as_view(),name='scode'),  #to write class based view
    
]
