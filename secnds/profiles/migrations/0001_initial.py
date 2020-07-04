# Generated by Django 3.0.7 on 2020-06-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('address_2', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('province_choices', models.CharField(choices=[('WP', 'Western'), ('CP', 'Central'), ('SP', 'Southern'), ('NW', 'North Western'), ('SG', 'Sabaragamuwa'), ('EP', 'Eastern'), ('NC', 'North Central'), ('UP', 'Uva'), ('NP', 'Northern')], max_length=2)),
                ('mobile_number', models.CharField(max_length=10)),
                ('profilemanager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
