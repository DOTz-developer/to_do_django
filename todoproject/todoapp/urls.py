
from django.urls import path, include

from todoapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('lview/',views.lview.as_view(),name='lview'),
    path('dview/<int:pk>/',views.dview.as_view(),name='dview'),
    path('uview/<int:pk>/',views.uview.as_view(),name = 'uview '),
    path('delview/<int:pk>/',views.delview.as_view(),name='delview')

]
