from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from datetime import datetime
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.models import Admin ,Utlisateur , Client , Transporter , Intervention ,Notification , Meuble , Produit,Paiement , ListMeuble , LesProduit, Positions
from django.db import connections
from django.http import JsonResponse
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from polls.serializers import MeubleSerializer , ProduitSerializer , UtlisateurSerializer  ,InterventionSerializer , PaiementSerializer , NotificationSerializer ,TransportersSerializer , ClientSerializer , ListMeubleSerializer ,LesProduitSerializer
from django.core import serializers
import json
import logging
import threading

class InsertAdmin(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         nom1 = body.get('nom',None)
         prenom1 = body.get('prenom',None)
         email1 = body.get('email',None)
         Adresse1 = body.get('adresse',None)
         mot_de_passe1 =body.get('mot_de_passe',None)
         u= Utlisateur(nom=nom1 , prenom=prenom1 , email=email1 , adresse=Adresse1 , mot_de_passe=mot_de_passe1  )
         u.save()
         id_user1=Utlisateur.objects.filter(email=email1,mot_de_passe=mot_de_passe1).values('id_user')[0]['id_user']
         a=Admin(id_user=Utlisateur.objects.get(id_user=id_user1))
         a.save()
         if(a):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertClient(APIView):
   def post(self, request):
   #   try:
         body = json.loads(request.body.decode('utf-8'))
         nom1 = body.get('nom',None)
         prenom1 = body.get('prenom',None)
         email1 = body.get('email',None)
         # Adresse1 = body.get('adresse',None)
         mot_de_passe1 =body.get('mot_de_passe',None)
         telephone1 = body.get('telephone',None)
         u= Utlisateur(nom=nom1 , prenom=prenom1 , email=email1 , mot_de_passe=mot_de_passe1 )
         u.save()
         id_user1=Utlisateur.objects.filter(email=email1,mot_de_passe=mot_de_passe1).values('id_user')[0]['id_user']
         c=Client(id_user=Utlisateur.objects.get(id_user=id_user1),telephone=telephone1)
         c.save()
         id_cl1=Client.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).values('id_cl')[0]['id_cl']
         if(c):
            return  Response({'Reponse':id_cl1})
   #   except:
            # pass
            # return Response({'Reponse':'Faild'})

class InsertTrnarsporter(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         nom1 = body.get('nom',None)
         prenom1 = body.get('prenom',None)
         email1 = body.get('email',None)
         # Adresse1 = body.get('adresse',None)
         mot_de_passe1 =body.get('mot_de_passe',None)
         telephone1 = body.get('telephone',None)
         u= Utlisateur(nom=nom1 , prenom=prenom1 , email=email1  , mot_de_passe=mot_de_passe1 )
         u.save()
         id_user1=Utlisateur.objects.filter(email=email1,mot_de_passe=mot_de_passe1).values('id_user')[0]['id_user']
         a=Transporter(id_user=Utlisateur.objects.get(id_user=id_user1),telephone=telephone1)
         a.save()
         if(a):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})
class InsertPositions(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         latitude1 = body.get('latitude',None)
         longitude1 = body.get('longitude',None)
         id_tran1  = body.get('id_tran',None)
         P=Positions(latitude=latitude1 ,longitude=longitude1 , id_tr=Transporter.objects.get(id_tran=id_tran1))
         P.save()
         if(P):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertNotification(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         titre1= body.get('titre',None)
         sujet1 = body.get('sujet',None)
         today = date.today()
         d1 = today.strftime("%Y-%m-%d")
         Date1 = d1
         id_cl1  = body.get('id_cl',None)
         I= Notification(titre=titre1, sujet=sujet1,date=Date1 , id_cl=Client.objects.get(id_cl=id_cl1))
         I.save()
         if(I):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertPaiement(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         prix1 = body.get('prix',None)
         today = date.today()
         d1 = today.strftime("%Y-%m-%d")
         Date1 = d1
         id_cl1  = body.get('id_cl',None)
         id_in1  = body.get('id_in',None)
         P=Paiement(prix=prix1 ,date=Date1 , id_cl=Client.objects.get(id_cl=id_cl1), id_in=Intervention.objects.get(id_in=id_in1))
         P.save()
         if(P):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertIntervention(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         type_service1 = body.get('type_service',None)
         adresse_deb1 = body.get('adresse_deb',None)
         adresse_fin1 = body.get('adresse_fin',None)
         date_livraison1 = body.get('date_livraison',None)
         today = date.today()
         d1 = today.strftime("%Y-%m-%d")
         Date1 = d1
         id_cl1  = body.get('id_cl',None)
         I= Intervention(type_service=type_service1, adresse_deb=adresse_deb1, adresse_fin=adresse_fin1,date_livraison=date_livraison1,date_in=Date1, id_cl=Client.objects.get(id_cl=id_cl1) )
         I.save()
         id_in2=Intervention.objects.filter(id_cl=id_cl1,date_in=Date1).values('id_in')[0]['id_in']
         if(I):
            return  Response({'Reponse':id_in2})
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertMeuble(APIView):
   def post(self, request):
     try:
       serializer = MeubleSerializer(data=request.data , many=True)
       if serializer.is_valid():
          n=len(serializer.data)
          for i in range(n):
              meuble=serializer.data[i]
              m=Meuble(type=meuble['type'],dimension=meuble['dimension'],prix=meuble['prix'],id_in=Intervention.objects.get(id_in=meuble['id_in']))
              m.save()
          return Response("secc")
       else:
            return Response(serializer.errors, status=400)
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertProduit(APIView):
   def post(self, request):
     try:
       serializer = ProduitSerializer(data=request.data , many=True)
       if serializer.is_valid():
          n=len(serializer.data)
          for i in range(n):
              produit=serializer.data[i]
              p=Produit(poid=produit['poid'],dimension=produit['dimension'],prix=produit['prix'],id_in=Intervention.objects.get(id_in=produit['id_in']))
              p.save()
          return Response("secc")
       else:
            return Response(serializer.errors, status=400)
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertMeubles(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         catigorie1 = body.get('catigorie',None)
         type1 = body.get('type',None)
         prix1 = body.get('prix',None)
         lm= ListMeuble(catigorie=catigorie1 , type=type1 , prix=prix1 )
         lm.save()
         if(lm):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class InsertPoduits(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         prix1 = body.get('prix',None)
         lm= LesProduit(prix=prix1 )
         lm.save()
         if(lm):
            return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})
          
class AfficheUtilisateur(APIView):
   def get(self, request, id_user1, formt=None):
      utilisateur = Utlisateur.objects.filter(id_user=id_user1).first()
      utilisateur_Serializer = UtlisateurSerializer(utilisateur)
      return utilisateur_Serializer.data
class AfficheTransporter(APIView):
   def post(self, request, format=None):
    try:
         transporter1 = Transporter.objects.all()
         Transporters_Serializer= TransportersSerializer(transporter1, many=True)
         result = []
         for transporter in transporter1:
            id_user1 = transporter.id_user_id
            utilisateur_data = AfficheUtilisateur().get(request, id_user1)
            transporter_data = {
               'id_tran': transporter.id_tran,
               'nom': utilisateur_data['nom'],
               'prenom':utilisateur_data['prenom'],
               'adresse':utilisateur_data['adresse'],
               'email':utilisateur_data['email'],
               'telephone': transporter.telephone,
               'position': transporter.position
            }
            result.append(transporter_data)
         return JsonResponse(result, safe=False)
    except:
            pass
            return Response({'Reponse':'Faild'})
class AfficheTransporter1(APIView):
   def post(self, request, format=None):
    try:
         body = json.loads(request.body.decode('utf-8'))
         id_tran1 = body.get('id_tran',None)
         transporter1 = Transporter.objects.filter(id_tran=id_tran1)
         Transporters_Serializer= TransportersSerializer(transporter1, many=True)
         result = []
         for transporter in transporter1:
            id_user1 = transporter.id_user_id
            utilisateur_data = AfficheUtilisateur().get(request, id_user1)
            transporter_data = {
               'id_tran': transporter.id_tran,
               'nom': utilisateur_data['nom'],
               'prenom':utilisateur_data['prenom'],
               'adresse':utilisateur_data['adresse'],
               'email':utilisateur_data['email'],
               'telephone': transporter.telephone,
               'position': transporter.position
            }
            result.append(transporter_data)
         return JsonResponse(result[0], safe=False)
    except:
            pass
            return Response({'Reponse':'Faild'})
class AfficheClient(APIView):
   def post(self, request, format=None):
     try:
         client1 = Client.objects.all()
         Client_Serializer= ClientSerializer(client1, many=True)
         result = []
         for client in client1:
            id_user1 = client.id_user_id
            utilisateur_data = AfficheUtilisateur().get(request, id_user1)
            client_data = {
               'id_cl': client.id_cl,
               'nom': utilisateur_data['nom'],
               'prenom':utilisateur_data['prenom'],
               'adresse':utilisateur_data['adresse'],
               'email':utilisateur_data['email'],
               'telephone': client.telephone,
            }
            result.append(client_data)
         return JsonResponse(result, safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheIntervetionC(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_cl1  = body.get('id_cl',None)
         intervention1= Intervention.objects.filter(id_cl=id_cl1)
         Intervention_Serializer1 = InterventionSerializer(intervention1, many=True)
         return JsonResponse(Intervention_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheIntervetionT(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_tr1  = body.get('id_tr',None)
         intervention1= Intervention.objects.filter(id_tr=id_tr1)
         Intervention_Serializer1 = InterventionSerializer(intervention1, many=True)
         return JsonResponse(Intervention_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheIntervetionAll(APIView):
   def post(self, request):
     try:
         intervention1= Intervention.objects.all()
         Intervention_Serializer1 = InterventionSerializer(intervention1, many=True)
         return JsonResponse(Intervention_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})
class AfficheIntervetion1(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_in1  = 98
         # body.get('id_in',None)
         intervention1= Intervention.objects.filter(id_in=id_in1)
         Intervention_Serializer1 = InterventionSerializer(intervention1, many=True)
         return JsonResponse(Intervention_Serializer1.data[0] , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})
class AffichePaiment(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_cl1  = body.get('id_cl',None)
         paiement1= Paiement.objects.filter(id_cl=id_cl1)
         Paiement_Serializer1 = PaiementSerializer(paiement1, many=True)
         return JsonResponse(Paiement_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheNotificationC(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_cl1  = body.get('id_cl',None)
         notification1= Notification.objects.filter(id_cl=id_cl1)
         Notification_Serializer1 = NotificationSerializer(notification1, many=True)
         return JsonResponse(Notification_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheNotificationT(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_tran1  = body.get('id_tran',None)
         notification1= Notification.objects.filter(id_tran=id_tran1)
         Notification_Serializer1 = NotificationSerializer(notification1, many=True)
         return JsonResponse(Notification_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheMeuble(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_in1  = body.get('id_in',None)
         meuble1= Meuble.objects.filter(id_in=id_in1)
         Meuble_Serializer1 = MeubleSerializer(meuble1, many=True)
         return JsonResponse(Meuble_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheProduit(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_in1  = body.get('id_in',None)
         produit1= Produit.objects.filter(id_in=id_in1)
         Produit_Serializer1 = ProduitSerializer(produit1, many=True)
         return JsonResponse(Produit_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficheListMeuble(APIView):
   def get(self, request, format=None):
     try:
         # body = json.loads(request.body.decode('utf-8'))
         # type1  = body.get('type',None)
         type1= request.GET.get('type', None)
         listmeuble1= ListMeuble.objects.filter(type=type1)
         ListMeuble_Serializer1 = ListMeubleSerializer(listmeuble1 , many=True)
         return JsonResponse(ListMeuble_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'faild'})

class AfficheLesProduit(APIView):
   def get(self, request,format=None):
     try:
         # body = json.loads(request.body.decode('utf-8'))
         lesproduit1= LesProduit.objects.all()
         LesProduit_Serializer1 = LesProduitSerializer(lesproduit1 , many=True)
         return JsonResponse(LesProduit_Serializer1.data , safe=False)
     except:
            pass
            return Response({'Reponse':'Faild'})
          
class ModifierClient(APIView):
   def post(self,request):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id_user1  = body.get('id_user',None)
         nom1 = body.get('nom',None)
         prenom1 = body.get('prenom',None)
         adresse1 = body.get('adresse',None)
         email1 = body.get('email',None)
         mot_de_passe1 = body.get('mot_de_passe',None)
         telephone1 = body.get('telephone',None)
         user= Utlisateur.objects.get(id_user=id_user1)
         user.nom=nom1
         user.prenom=prenom1
         user.adresse=adresse1
         user.email=email1
         user.mot_de_passe=mot_de_passe1
         user.save()
         client=Client.objects.get(id_user=Utlisateur.objects.get(id_user=id_user1)) 
         client.telephone=telephone1
         client.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})

class ModifierTransporter(APIView):
   def post(self,request ):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id_tran1  = body.get('id_tran',None)
         nom1 = body.get('nom',None)
         prenom1 = body.get('prenom',None)
         # adresse1 = body.get('adresse',None)
         email1 = body.get('email',None)
         # mot_de_passe1 = body.get('mot_de_passe',None)
         telephone1 = body.get('telephone',None)
         id_user1=Transporter.objects.filter(id_tran=id_tran1).values('id_user')[0]['id_user']
         user= Utlisateur.objects.get(id_user=id_user1)
         user.nom=nom1
         user.prenom=prenom1
         # user.adresse=adresse1
         user.email=email1
         # user.mot_de_passe=mot_de_passe1
         user.save()
         transporter=Transporter.objects.get(id_user=Utlisateur.objects.get(id_user=id_user1)) 
         transporter.telephone=telephone1
         transporter.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})

class ModifierTransporterPosition(APIView):
   def post(self,request ):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id_tran1  = body.get('id_tran',None)
         position1 = body.get('position',None)
         transporter= Transporter.objects.get(id_tran=id_tran1)
         transporter.position=position1
         transporter.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})

class ModifierIntervention(APIView):
   def post(self,request ):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id_cl1  = body.get('id_cl',None)
         adresse_deb1 = body.get('adresse_deb',None)
         adresse_fin1 = body.get('adresse_fin',None)
         today = date.today()
         d1 = today.strftime("%Y-%m-%d")
         Date1 = d1
         date_livraison1 = body.get('date_livraison',None)
         id_tr1= body.get('id_tr',None)
         intervention= Intervention.objects.get(id_cl=Client.objects.get(id_cl=id_cl1))
         intervention.adresse_deb=adresse_deb1
         intervention.adresse_fin=adresse_fin1
         intervention.date_livraison=date_livraison1
         intervention.date_in=Date1
         intervention.id_tr=Transporter.objects.get(id_tran=id_tr1)
         intervention.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})

class ModifierMeuble(APIView):
   def post(self,request ):
      try:
         body = json.loads(request.body.decode('utf-8'))
         type1 = body.get('type',None)
         dimension1 = body.get('dimension',None)
         prix1 = body.get('prix',None)
         id_me1= body.get('id_me',None)
         meuble= Meuble.objects.get(id_me=id_me1)
         meuble.type=type1
         meuble.dimension=dimension1
         meuble.prix=prix1
         meuble.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})

class ModifierProduit(APIView):
   def post(self,request , format=None):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id_pr1=body.get('id_pr',None)
         poid1 = body.get('poid',None)
         dimension1 = body.get('dimension',None)
         prix1 = body.get('prix',None)
         produit= Produit.objects.get(id_pr=id_pr1)
         produit.poid=poid1
         produit.dimension=dimension1
         produit.prix=prix1
         produit.save()
         return Response('secc')
      except:
            pass
            return Response({'Reponse':'Faild'})
      
class ModifierMeubles(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_lm1= body.get('id_lm',None)
         catigorie1 = body.get('catigorie',None)
         type1 = body.get('type',None)
         prix1 = body.get('prix',None)
         lm= ListMeuble.objects.get(id_lm=id_lm1)
         lm.catigorie=catigorie1
         lm.type=type1
         lm.prix=prix1
         lm.save()
         return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})
     
class ModifierProduits(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_lp1= body.get('id_lp',None)
         prix1 = body.get('prix',None)
         produit= LesProduit.objects.get(id_lp=id_lp1)
         produit.prix=prix1
         produit.save()
         return  HttpResponse("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})
          
class Verification(APIView):
    def post(self,request ):
     try:
        body = json.loads(request.body.decode('utf-8'))
        email1 = body.get('email',None)
        mot_de_passe1 = body.get('mot_de_passe',None)
        user = Utlisateur.objects.filter(email=email1,mot_de_passe=mot_de_passe1)
        User_Serializer =UtlisateurSerializer(user,many=True)
        if(user.count()==1):
            id_user1=User_Serializer.data[0]['id_user']
            
            admin= Admin.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).count()
            client= Client.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).count()
            transporter= Transporter.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).count()
            if(admin==1):
             return  HttpResponse("admin")
            elif client==1:
                  id_cl1=Client.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).values('id_cl')[0]['id_cl']
                  return  Response({"Reponse":id_cl1});
            elif transporter==1:
             id_tran1=Transporter.objects.filter(id_user=Utlisateur.objects.get(id_user=id_user1)).values('id_tran')[0]['id_tran']
             return  Response({"Reponse":id_tran1})
        else:
             return Response({"resultat":"field"})
     except:
            pass
            return Response({'Reponse':'Faild'})

class DeleteClient(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_cl1 = body.get('id_cl',None)
         id_user1=Client.objects.filter(id_cl=id_cl1).values('id_user')[0]['id_user']
         utlisateur1=Utlisateur.objects.get(id_user=id_user1)
         utlisateur1.delete()
         return Response("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class DeleteTranporter(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_tran1 = body.get('id_tran',None)
         id_user1=Transporter.objects.filter(id_tran=id_tran1).values('id_user')[0]['id_user']
         utlisateur1=Utlisateur.objects.get(id_user=id_user1)
         utlisateur1.delete()
         return Response("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class DeleteIntervention(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_in1 = body.get('id_in',None)
         intervation1=Intervention.objects.get(id_in=id_in1)
         intervation1.delete()
         return Response("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})

class DeleteMeubles(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_lm1 = body.get('id_lm',None)
         Meubles1=ListMeuble.objects.get(id_lm=id_lm1)
         Meubles1.delete()
         return Response("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})
     
class DeletePrduits(APIView):
   def post(self, request):
     try:
         body = json.loads(request.body.decode('utf-8'))
         id_lp1 = body.get('id_lp',None)
         Produit1=LesProduit.objects.get(id_lp=id_lp1)
         Produit1.delete()
         return Response("secc")
     except:
            pass
            return Response({'Reponse':'Faild'})


   
