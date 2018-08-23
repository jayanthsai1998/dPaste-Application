from django.contrib import admin
from django.urls import path
from dpasteapp.views import *


urlpatterns = [

    path('', HomeRedirectView.as_view()),

    path('signup/', SignUpController.as_view(), name = 'signup'),
    path('login/', LoginController.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout'),

    path('dpastelists/', dPasteListView.as_view(), name = 'dpastelists'),
    path('dpastelists/add/', dPasteListCreateView.as_view(), name = 'add_dpastelist'),

    path('dpastelists/<int:pk>/edit/', dPasteListUpdateView.as_view(), name = 'edit_dpastelist'),
    path('dpastelists/<int:pk>/delete/', dPasteListDeleteView.as_view(), name = 'delete_dpastelist'),

    path('dpastelists/<int:dpastelist_id>/', dPasteItemListView.as_view(), name = 'dpastelistitem_list'),
    path('dpastelists/<int:dpastelist_id>/add/', dPasteListItemCreateView.as_view(), name = 'add_dpastelistitem'),
    path('dpastelists/<int:dpastelist_id>/items/<int:pk>/edit/', dPasteListItemUpdateView.as_view(), name = 'edit_dpastelistitem'),
    path('dpastelists/<int:dpastelist_id>/items/<int:pk>/delete/', dPasteListItemDeleteView.as_view(), name = 'delete_dpastelistitem'),

    #path('')

    path( 'about/', aboutView.as_view(), name = 'about' ),
    path( 'features/', featuresView.as_view(), name = 'features' ),
]