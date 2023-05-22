# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    id_user = models.OneToOneField('Utlisateur', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Avis(models.Model):
    id_a = models.AutoField(primary_key=True)
    id_cl = models.ForeignKey('Client', models.DO_NOTHING, db_column='id_cl')
    descriptions = models.TextField()

    class Meta:
        managed = False
        db_table = 'avis'


class Client(models.Model):
    id_cl = models.AutoField(primary_key=True)
    telephone = models.IntegerField()
    id_user = models.OneToOneField('Utlisateur', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'client'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Intervention(models.Model):
    id_in = models.AutoField(primary_key=True)
    type_service = models.CharField(max_length=20)
    adresse_deb = models.CharField(max_length=255)
    adresse_fin = models.CharField(max_length=255)
    date_livraison = models.DateTimeField()
    date_in = models.DateTimeField()
    id_cl = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_cl', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intervention'


class LesProduit(models.Model):
    id_lp = models.AutoField(primary_key=True)
    prix = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'les_produit'


class ListMeuble(models.Model):
    id_lm = models.AutoField(primary_key=True)
    catigorie = models.CharField(max_length=100)
    type = models.CharField(max_length=255)
    prix = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'list_meuble'


class Meuble(models.Model):
    id_me = models.AutoField(primary_key=True)
    type = models.CharField(max_length=40)
    dimension = models.FloatField()
    prix = models.FloatField()
    id_in = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='id_in', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meuble'


class Notification(models.Model):
    id_n = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=40)
    sujet = models.CharField(max_length=50)
    date = models.DateTimeField()
    id_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    id_tran = models.ForeignKey('Transporter', models.DO_NOTHING, db_column='id_tran', blank=True, null=True)
    id_cl = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_cl', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'


class Paiement(models.Model):
    prix = models.IntegerField()
    date = models.DateTimeField()
    id_cl = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_cl')
    id_in = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='id_in')

    class Meta:
        managed = False
        db_table = 'paiement'


class Positions(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    id_tr = models.ForeignKey('Transporter', models.DO_NOTHING, db_column='id_tr')

    class Meta:
        managed = False
        db_table = 'positions'


class Produit(models.Model):
    id_pr = models.AutoField(primary_key=True)
    poid = models.FloatField()
    dimension = models.FloatField()
    prix = models.FloatField()
    id_in = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='id_in', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produit'


class Tache(models.Model):
    id_tache = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    id_in = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='id_in')
    etat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tache'


class TacheTransporter(models.Model):
    id_tt = models.AutoField(primary_key=True)
    id_tran = models.ForeignKey('Transporter', models.DO_NOTHING, db_column='id_tran')
    id_tache = models.ForeignKey(Tache, models.DO_NOTHING, db_column='id_tache')

    class Meta:
        managed = False
        db_table = 'tache_transporter'


class Transporter(models.Model):
    id_tran = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=12)
    id_user = models.OneToOneField('Utlisateur', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'transporter'


class Utlisateur(models.Model):
    id_user = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'utlisateur'
