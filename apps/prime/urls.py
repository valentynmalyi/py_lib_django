from django.urls import path, include

from apps.prime import views

urlpatterns = [
    path('<int:n>', views.PrimeNumber.as_view())
]
