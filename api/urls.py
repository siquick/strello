from django.conf import settings
from django.urls import path, include
from .views import *
if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('',HelloWorld.as_view(), name='hello-world'),
    path('boards/',ListBoards.as_view({'get':'list'}), name='list-boards'),
    path('board/<int:pk>',BoardsDetail.as_view(), name='list-board-details'),
    
    path('lists/',ListLists.as_view({'get':'list'}), name='list-lists'),
    path('list/<int:pk>',ListsDetails.as_view(), name='list-list-details'),
    
    path('cards/',ListCards.as_view({'get':'list'}), name='list-cards'),
]

urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
