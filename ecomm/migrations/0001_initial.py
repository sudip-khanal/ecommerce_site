# Generated by Django 4.2.1 on 2023-05-05 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('locations', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('Koshi', 'Koshi'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Madhesh', 'Madhesh'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('selling_price', models.FloatField()),
                ('discunted_prce', models.FloatField()),
                ('discription', models.TextField()),
                ('brand', models.CharField(max_length=30)),
                ('Category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('Top Wear', 'Top Wear'), ('Bottom Wear', 'Bottom Wear')], max_length=20)),
                ('product_image', models.ImageField(upload_to='Product_image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Koshi', 'Koshi'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Madhesh', 'Madhesh'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], default='Pending', max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
