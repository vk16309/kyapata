# Generated by Django 2.2 on 2020-03-15 06:14

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
            name='Upvoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoter', models.CharField(default='None', max_length=40, verbose_name='Upvoter')),
                ('upvoted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('class_type', models.CharField(choices=[('t', 'Home Tution'), ('c', 'Coaching'), ('b', 'both')], max_length=20)),
                ('name', models.CharField(max_length=120, verbose_name='Your Name')),
                ('institute_name', models.CharField(max_length=50, null=True, verbose_name='Institute Name')),
                ('email', models.CharField(max_length=120, verbose_name='Enter Your Email')),
                ('contact', models.IntegerField(verbose_name='Mobile Number')),
                ('locality', models.CharField(default='optional', max_length=50)),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('state', models.CharField(max_length=20, verbose_name='State')),
                ('votes_total', models.IntegerField(default=1)),
                ('acheivements', models.TextField(help_text='Description about your Acheivements and Awards', max_length=1000)),
                ('experience', models.IntegerField(verbose_name='Years')),
                ('videolinks', models.CharField(max_length=120, verbose_name='Notes Or Video Links')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('premium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', 'other')], max_length=10)),
                ('subject', models.CharField(max_length=40, verbose_name='Subject')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
