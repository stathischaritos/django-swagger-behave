from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'lists', views.TodoListViewSet)
router.register(r'tasks', views.TodoTaskViewSet)
router.register(r'tags', views.TodoTagViewSet)

urlpatterns = [

    #REST routes provided by viewset.
    url(r'^', include(router.urls)),

    #Authentication route by rest framework.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Swagger documentation by rest framework.
    url(r'^docs/', include('rest_framework_swagger.urls')),

]