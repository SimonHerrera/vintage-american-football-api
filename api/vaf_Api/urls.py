from django.conf.urls import url, include
from vaf_Api import views
from rest_framework import routers


router = routers.DefaultRouter()
# do I need franchise url and view - doubt it becuase they are only shown on team
router.register(r'franchises', views.FranchiseList)
router.register(r'managers', views.ManagerList)
router.register(r'equipment', views.EquipmentList)
router.register(r'players', views.PlayerList)
router.register(r'locations', views.LocationList)
router.register(r'teams', views.TeamList)
router.register(r'games', views.GameList)

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')) #allows logout
]