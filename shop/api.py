from rest_framework import routers
from rental import views
from myshop import views as v1
router = routers.DefaultRouter()
router.register(r'friends', views.FriendViewset)
router.register(r'belongings', views.BelongingViewset)
router.register(r'borrowings', views.BorrowedViewset)
router.register(r'Data', v1.data)