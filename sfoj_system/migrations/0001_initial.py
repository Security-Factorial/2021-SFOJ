# Generated by Django 3.1.3 on 2021-09-05 12:14

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
            name='Code_History',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('UserID', models.CharField(max_length=15)),
                ('Board_idx', models.IntegerField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Judge_State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_idx', models.IntegerField()),
                ('UserID', models.CharField(max_length=15)),
                ('States', models.CharField(max_length=5)),
                ('Memory_use', models.IntegerField()),
                ('Time_Complex', models.IntegerField()),
                ('Submission_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('useremail', models.CharField(max_length=128)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.TextField()),
                ('Reg_date', models.DateTimeField(null=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
