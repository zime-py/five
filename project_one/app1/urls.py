from django.urls import path
from.import views

urlpatterns = [
    path('anisul/',views.one,name='anisul'),
    path('naim/',views.two,name='naim'),
    path('w3school/',views.three,name='w3school'),
]
