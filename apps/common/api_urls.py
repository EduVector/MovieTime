from django.urls import path

from .api.genre.GenreCreate.views import GenreCreateView
from .api.genre.GenreDestroy.views import GenreDestroyView
from .api.genre.GenreDetail.views import GenreRetrieveView
from .api.genre.GenreList.views import GenreListView
from .api.genre.GenreUpdate.views import GenreUpdateView


app_name = "common"

urlpatterns = [
    path('genrecreate/', GenreCreateView.as_view(), name='genre_create'),
    path('genredestroy/<str:name>/', GenreDestroyView.as_view(), name='genre_destroy'),
    path('genredetail/<str:name>/', GenreRetrieveView.as_view(), name='genre_detail'),
    path('genrelist/', GenreListView.as_view(), name='genre_list'),
    path('genreupdate/<str:name>/', GenreUpdateView.as_view(), name='genre_update'),
]
