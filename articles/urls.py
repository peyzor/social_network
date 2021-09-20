from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:article_id>/',
         views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('<int:article_id>/comments/',
         views.ArticleCommentListView.as_view(),
         name='comment_list'),
    path('<int:article_id>/comments/<int:comment_id>/',
         views.ArticleCommentDetailView.as_view(),
         name='comment_detail'),
    path('<int:article_id>/images/',
         views.ArticleImageListView.as_view(),
         name='image_list'),
    path('<int:article_id>/images/<int:image_id>/',
         views.ArticleImageDetailView.as_view(),
         name='image_detail'),
]
