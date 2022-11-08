from rest_framework import routers

from management import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoriesViewSet)

urlpatterns = router.urls
