# Generated by Django 4.2 on 2023-05-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='media/blog')),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_issued', models.DateField()),
                ('issuer', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='media/certificate')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificate',
            },
        ),
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='media/testimonies')),
                ('content', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Testimonies',
                'verbose_name_plural': 'Testimonies',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('facebook', models.CharField(blank=True, max_length=2000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=2000, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=2000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=2000, null=True)),
                ('image_field', models.ImageField(upload_to='media/personal')),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfile',
            },
        ),
    ]