from django.conf import settings
from django.urls import path, include
from .views import HelloWorld, ListBoards, BoardsDetail
from .views import ListLists, ListsDetails, ListCards, CardDetails
from .views import ListLabels, LabelDetails

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello-world'),
    path('boards/', ListBoards.as_view(), name='list-boards'),
    path('board/<int:pk>', BoardsDetail.as_view(), name='list-board-details'),

    path('lists/', ListLists.as_view(), name='list-lists'),
    path('list/<int:pk>', ListsDetails.as_view(), name='list-list-details'),

    path('cards/', ListCards.as_view(), name='list-cards'),
    path('card/<int:pk>', CardDetails.as_view(), name='list-card-details'),

    path('labels/', ListLabels.as_view(), name='list-labels'),
    path('label/<int:pk>', LabelDetails.as_view(), name='list-label-details'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
