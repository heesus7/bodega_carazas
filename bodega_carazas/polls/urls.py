from django.urls import path
from . import views
import polls

app_name= 'polls'

urlpatterns=[
    path('',views.index,name='index'),
    path('especificaciones/<int:question_id>/',views.detail,name='detalle'),
    path('<int:question_id>/resultados/',views.results,name='resultados'),
    path('<int:question_id>/votacion/',views.vote,name='votacion'),
    
]