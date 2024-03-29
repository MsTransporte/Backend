# Generated by Django 4.1.1 on 2023-04-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id_a', models.AutoField(primary_key=True, serialize=False)),
                ('descriptions', models.TextField()),
            ],
            options={
                'db_table': 'avis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_cl', models.AutoField(primary_key=True, serialize=False)),
                ('telephone', models.IntegerField()),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id_in', models.AutoField(primary_key=True, serialize=False)),
                ('type_service', models.CharField(max_length=20)),
                ('adresse_deb', models.CharField(max_length=255)),
                ('adresse_fin', models.CharField(max_length=255)),
                ('date_livraison', models.DateTimeField()),
                ('date_in', models.DateTimeField()),
            ],
            options={
                'db_table': 'intervention',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LesProduit',
            fields=[
                ('id_lp', models.AutoField(primary_key=True, serialize=False)),
                ('prix', models.IntegerField()),
            ],
            options={
                'db_table': 'les_produit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListMeuble',
            fields=[
                ('id_lm', models.AutoField(primary_key=True, serialize=False)),
                ('catigorie', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=255)),
                ('prix', models.IntegerField()),
            ],
            options={
                'db_table': 'list_meuble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meuble',
            fields=[
                ('id_me', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=40)),
                ('dimension', models.FloatField()),
                ('prix', models.FloatField()),
            ],
            options={
                'db_table': 'meuble',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id_n', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=40)),
                ('sujet', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id_p', models.AutoField(primary_key=True, serialize=False)),
                ('prix', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'paiement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id_tr', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
            options={
                'db_table': 'les_produit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id_pr', models.AutoField(primary_key=True, serialize=False)),
                ('poid', models.FloatField()),
                ('dimension', models.FloatField()),
                ('prix', models.FloatField()),
            ],
            options={
                'db_table': 'produit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id_tran', models.AutoField(primary_key=True, serialize=False)),
                ('telephone', models.CharField(max_length=12)),
                ('position', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'transporter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utlisateur',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'utlisateur',
                'managed': False,
            },
        ),
    ]
