from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='Article-detail'),
	path('search/', views.SearchResultsView.as_view(), name='search_results'),
	path('search-console/', views.search_console, name='search'),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),

]

