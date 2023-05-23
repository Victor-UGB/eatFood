# Generated by Django 3.2 on 2023-05-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=50, unique=True)),
                ('category_tagline', models.CharField(max_length=300)),
                ('category_vendors', models.ManyToManyField(related_name='vendor_catergories', to='vendors.FoodVendor')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem_name', models.CharField(default='Food Item', max_length=50)),
                ('fooditem_description', models.CharField(default='Food Description', max_length=300)),
                ('fooditem_price', models.IntegerField(default=0)),
                ('fooditem_rating', models.FloatField(default=4.5)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ManyToManyField(related_name='category_food_items', to='api.FoodCategory')),
                ('fooditem_vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_items', to='vendors.foodvendor')),
            ],
        ),
    ]
