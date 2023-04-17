from django.urls import path , include
from . import views

urlpatterns = [
    path('InsertAdmin', views.InsertAdmin.as_view()),
    path('InsertClient', views.InsertClient.as_view()),
    path('InsertTrnarsporter', views.InsertTrnarsporter.as_view()),
    path('InsertPositions', views.InsertPositions.as_view()),
    path('InsertMeuble', views.InsertMeuble.as_view()),
    path('InsertProduit', views.InsertProduit.as_view()),
    path('InsertPaiement', views.InsertPaiement.as_view()),
    path('InsertNotification', views.InsertNotification.as_view()),
    path('InsertIntervention', views.InsertIntervention.as_view()),
    path('InsertMeubles',views.InsertMeubles.as_view()),
    path('InsertPoduits',views.InsertPoduits.as_view()),
    path('AfficheTransporter',views.AfficheTransporter.as_view()),
    path('AfficheTransporter1',views.AfficheTransporter1.as_view()),
    path('Verification', views.Verification.as_view()),
    path('AfficheClient',views.AfficheClient.as_view()),
    path('AfficheIntervetionT', views.AfficheIntervetionT.as_view()),
    path('AfficheIntervetionC', views.AfficheIntervetionC.as_view()),
    path('AfficheIntervetion1', views.AfficheIntervetion1.as_view()),
    path('AfficheIntervetionAll', views.AfficheIntervetionAll.as_view()),
    path('AfficheNotificationC', views.AfficheNotificationC.as_view()),
    path('AfficheNotificationT', views.AfficheNotificationT.as_view()),
    path('AfficheMeuble', views.AfficheMeuble.as_view()),
    path('AfficheProduit', views.AfficheProduit.as_view()),
    path('AfficheListMeuble/get/',views.AfficheListMeuble.as_view()),
    path('AfficheLesProduit/get/',views.AfficheLesProduit.as_view()),
    path('ModifierClient', views.ModifierClient.as_view()),
    path('ModifierTransporter', views.ModifierTransporter.as_view()),
    path('ModifierTransporterPosition', views.ModifierTransporterPosition.as_view()),
    path('ModifierIntervention', views.ModifierIntervention.as_view()),
    path('ModifierMeuble', views.ModifierMeuble.as_view()),
    path('ModifierProduit', views.ModifierProduit.as_view()),
    path('ModifierMeubles',views.ModifierMeubles.as_view()),
    path('ModifierProduits',views.ModifierProduits.as_view()),
    path('DeleteClient', views.DeleteClient.as_view()),
    path('DeleteTranporter',views.DeleteTranporter.as_view()),
    path('DeleteIntervention', views.DeleteIntervention.as_view()),
    path('DeleteMeubles',views.DeleteMeubles.as_view()),
    path('DeletePrduits',views.DeletePrduits.as_view()),
    path('api-auth/', include('rest_framework.urls'))

]