from . import views
from django.urls import path
app_name='bookapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:bookid>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]