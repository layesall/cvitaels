from django.urls import path
from base.views import IndexView, WorksView, NewsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('works/', WorksView.as_view(), name='works'),
    path('news/', NewsView.as_view(), name='news'),
]
