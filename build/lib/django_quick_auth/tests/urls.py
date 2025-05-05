from django.urls import path, include

urlpatterns = [
    path('auth/', include('django_quick_auth.urls', namespace='django_quick_auth')),
]