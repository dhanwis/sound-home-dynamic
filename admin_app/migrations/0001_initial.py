# Generated by Django 5.0.1 on 2024-02-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='admin_app/products')),
                ('head', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='admin_app/projects')),
                ('head', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
