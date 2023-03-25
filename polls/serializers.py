from rest_framework import serializers
from polls.models import Admin , Client , Transporter , Meuble , Produit , Intervention , Notification , Paiement , Utlisateur , Paiement , LesProduit , ListMeuble

class MeubleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meuble
        fields = ( 'type',
                 'dimension',
                 'prix' ,
                 'id_in',
        )
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ( 'poid',
                  'dimension',
                  'prix' ,
                  'id_in',
        )
class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Intervention
        fields = (
                    'id_in',
                    'type_service',
                    'adresse_deb',
                    'adresse_fin',
                    'date_livraison',
                    'date_in',
                    'id_cl',
                    'id_tr',
                )
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ( 'id_cl',
                  'telephone',
                  'id_user' ,
        )

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields=(
                    'id_p',
                    'prix',
                    'date',
                    'id_cl',
                    'id_in',
        )
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields=(
            'id_n',
            'titre',
            'sujet',
            'date',
            'id_admin',
            'id_tran',
            'id_cl',
        )
class UtlisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utlisateur
        fields = ( 'id_user',
                  'nom',
                  'prenom' ,
                  'adresse',
                  'email',
                  'mot_de_passe',
        )
class TransportersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporter
        fields = ('id_tran',
                    'telephone',
                    'position',
                    'id_user',)
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id_cl',
                    'telephone',
                    'id_user',)
class ListMeubleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListMeuble
        fields = ( 'catigorie',
                 'type',
                 'prix' ,
        )
class LesProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LesProduit
        fields = ( 
                 'prix' ,
        )