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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(choices=[('VEH', 'VEHICLES'), ('ELE', 'ELECTRONICS'), ('FUR', 'FURNITURE'), ('OTH', 'OTHER')], max_length=3)),
                ('ad_title', models.CharField(max_length=50)),
                ('image_1', models.ImageField(upload_to='ad_img')),
                ('image_2', models.ImageField(upload_to='ad_img')),
                ('image_3', models.ImageField(upload_to='ad_img')),
                ('image_4', models.ImageField(upload_to='ad_img')),
                ('image_5', models.ImageField(upload_to='ad_img')),
                ('item_brand', models.CharField(max_length=25)),
                ('item_model', models.CharField(max_length=25)),
                ('item_condition', models.CharField(choices=[('BN', 'BRAND NEW'), ('N', 'NEW'), ('U', 'USED'), ('NW', 'NOT WORKING')], max_length=2)),
                ('item_description', models.TextField(max_length=5000)),
                ('price', models.PositiveIntegerField()),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('itemmanager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]