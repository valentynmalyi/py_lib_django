from django.urls import path, include

from apps.prime import urls as prime_urls

urlpatterns = [
    path('prime/', include(prime_urls))
]
