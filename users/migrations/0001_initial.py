# Generated by Django 3.0.8 on 2020-08-09 13:31

from django.conf import settings
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('validated', models.BooleanField(default=False, help_text='True means user has a validated otp correctly in second API')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('password1', models.CharField(blank=True, max_length=20, null=True)),
                ('password2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=15, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.SmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('is_worker', models.BooleanField(default=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('current_role', models.CharField(blank=True, choices=[('CS', 'customer'), ('WR', 'worker')], default='CS', max_length=25)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_moder', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_online', models.DateTimeField(null=True)),
                ('avatar', models.ImageField(default='default/default.png', upload_to=users.models.user_photos_dir)),
                ('about', models.TextField(blank=True, null=True)),
                ('dislike', models.ManyToManyField(blank=True, related_name='_user_dislike_+', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('like', models.ManyToManyField(blank=True, related_name='_user_like_+', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
