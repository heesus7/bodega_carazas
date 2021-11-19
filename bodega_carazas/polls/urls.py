from django.urls import path
from . import views
import polls

app_name= 'polls'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detalle'),
    path('<int:pk>/resultados/',views.ResultsView.as_view(),name='resultados'),
    path('<int:question_id>/votacion/',views.vote,name='votacion'),
    
]