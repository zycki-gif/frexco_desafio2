from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='api:index')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls)
]
