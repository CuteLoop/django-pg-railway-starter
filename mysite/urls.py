from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your home app:
    path('', include('home.urls')),
    # allauth URLs for account management (login, signup, etc.)
    path('accounts/', include('allauth.urls')),
]
