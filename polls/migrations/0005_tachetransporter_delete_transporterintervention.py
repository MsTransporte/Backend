# Generated by Django 4.1.1 on 2023-05-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_tache_transporterintervention'),
    ]

    operations = [
        migrations.CreateModel(
            name='TacheTransporter',
            fields=[
                ('id_tt', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tache_transporter',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TransporterIntervention',
        ),
    ]