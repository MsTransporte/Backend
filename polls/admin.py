from django.contrib import admin
from .models import Admin , Transporter , Client , Intervention , Meuble , Produit , Paiement

admin.site.register(Admin)
admin.site.register(Transporter)
admin.site.register(Client)
admin.site.register(Intervention)
admin.site.register(Meuble)
admin.site.register(Produit)
admin.site.register(Paiement)
# Register your models here.
