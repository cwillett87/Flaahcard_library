from django.urls import path
from . import views


urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
    path('collections/<str:title>/', views.CollectionDetail.as_view()),
    path('collections-flashcard/', views.FlashcardList.as_view()),
    path('collections-flashcard/<int:collection>/', views.FlashcardDetail.as_view()),
    path('collections-flashcard/<int:pk>/<str:word>/', views.FlashcardNumber.as_view()),
    path('collections-flashcard/update/<int:pk>/', views.FlashcardEdit.as_view()),
]
