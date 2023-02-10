from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('content.urls')),
                  path('admin/', admin.site.urls),
                  path('cars/', include('cars.urls')),
                  path('credit/', include('credit.urls')),
                  path('blog/', include('blog.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
