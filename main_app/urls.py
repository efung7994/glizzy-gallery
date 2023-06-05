from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('glizzys/', views.glizzy_index, name='glizzy-index'),
  path('glizzys/<int:glizzy_id>/', views.glizzy_detail, name='glizzy-detail'),
  path('glizzys/create/', views.GlizzyCreate.as_view(), name='glizzy-create'),
]