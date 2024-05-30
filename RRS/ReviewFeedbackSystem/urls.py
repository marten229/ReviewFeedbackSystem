from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, create_reservation, bewertung_abgeben, danke, bewertungen_anzeigen, bewertung_loeschen

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reservation/', create_reservation, name='create-reservation'),
    path('restaurants/<int:pk>/bewertung/', bewertung_abgeben, name='create-bewertung'),
    path('restaurants/<int:pk>/danke/', danke, name='danke'),
    path('bewertungen/', bewertungen_anzeigen, name='bewertungen_anzeigen'),
    path('bewertungen/<int:bewertung_id>/loeschen/', bewertung_loeschen, name='bewertung-loeschen'),
]