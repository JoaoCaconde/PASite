from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
		name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
		name='token_refresh'),
    
    path('api/v1/', include('chamados.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
