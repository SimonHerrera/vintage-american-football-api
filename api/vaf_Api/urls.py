from django.conf.urls import url, include
from vaf_Api import views
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'playerteam', views.PlayerTeamList)
router.register(r'manager', views.ManagerList)
router.register(r'games', views.GameList)
router.register(r'players', views.PlayerList)
router.register(r'teams', views.TeamList)
router.register(r'equipment', views.EquipmentList)

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')) #allows logout
]