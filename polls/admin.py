from django.contrib import admin
from .models import Admin , Transporter , Client , Intervention , Meuble , Produit , Paiement , Positions , Tache , TacheTransporter

admin.site.register(Admin)
admin.site.register(Transporter)
admin.site.register(Client)
admin.site.register(Intervention)
admin.site.register(Meuble)
admin.site.register(Produit)
admin.site.register(Paiement)
admin.site.register(Positions)
admin.site.register(Tache)
admin.site.register(TacheTransporter)
# Register your models here.
