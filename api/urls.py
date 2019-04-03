from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from .views import HelloWorld, ListBoards, BoardsDetail
from .views import ListLists, ListsDetails
from .views import ListCards, CardDetails
from .views import ListLabels, LabelDetails
from .views import ListUsers, UserDetails

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Strello API')

urlpatterns = [
    url(r'^$', schema_view),
    path('', HelloWorld.as_view(), name='hello-world'),
    path('boards/', ListBoards.as_view(), name='list-boards'),
    path('board/<int:pk>', BoardsDetail.as_view(), name='list-board-details'),

    path('lists/', ListLists.as_view(), name='list-lists'),
    path('list/<int:pk>', ListsDetails.as_view(), name='list-list-details'),

    path('cards/', ListCards.as_view(), name='list-cards'),
    path('card/<int:pk>', CardDetails.as_view(), name='list-card-details'),

    path('labels/', ListLabels.as_view(), name='list-labels'),
    path('label/<int:pk>', LabelDetails.as_view(), name='list-label-details'),

    path('members/', ListUsers.as_view(), name='list-users'),
    path('member/<int:pk>', UserDetails.as_view(), name='list-label-details'),
]
#
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls),
#                            name='django-debug-toolbar'),
#                   ] + urlpatterns
