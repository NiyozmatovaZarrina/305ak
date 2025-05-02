from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
     path('', include('book.urls')), 
    path('admin/', admin.site.urls),
]

if (settings.DEBUG):
    from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
                                                                                                   
    urlpatterns += [        
        path('api/schema/', SpectacularAPIView.as_view(),    name='schema'),
        # Optional UI:
        path('api/swagger-ui/', SpectacularSwaggerView. as_view(url_name='schema'),name='swagger-ui'),
        path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    
