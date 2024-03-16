from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('', TemplateView.as_view(template_name = 'index.html'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
