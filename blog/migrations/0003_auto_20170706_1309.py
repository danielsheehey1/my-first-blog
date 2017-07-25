# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.TextField()),
                ('model', models.TextField()),
                ('serial', models.TextField()),
                ('hours', models.TimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('desc', models.TextField()),
                ('allotted', models.TimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Customer')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('desc', models.TextField()),
                ('worder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Work_Order')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='assigned',
            field=models.ManyToManyField(to='blog.Work_Order_Item'),
        ),
    ]