from django.urls import path
from api.views import home,add_std,delete_std,update_std,do_update_std
urlpatterns = [
    path('', home,name='home'),
    path('home/', home,name='home'),
    path('add-std/',add_std,name='add-std'),
    path('delete-std/<int:id>',delete_std,name='delete-std'),
    path('update-std/<int:id>',update_std,name='update-std'),
    path('do-update-std/<int:id>',do_update_std,name='do-update-std'),
]
