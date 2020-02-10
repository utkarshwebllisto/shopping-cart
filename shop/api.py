from rest_framework import routers
from rental import views
from myshop import views 
router = routers.DefaultRouter()
#router.register(r'friends', views.FriendViewset)
#router.register(r'belongings', views.BelongingViewset)
#router.register(r'borrowings', views.BorrowedViewset)
router.register(r'user', views.UserViewSet)