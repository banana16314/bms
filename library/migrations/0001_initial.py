# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('college', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('isbn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to='library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to='library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='editor',
            name='press',
            field=models.ForeignKey(to='library.Press'),
        ),
        migrations.AddField(
            model_name='book',
            name='bookstore',
            field=models.ForeignKey(to='library.Bookstore'),
        ),
        migrations.AddField(
            model_name='book',
            name='editor',
            field=models.ForeignKey(to='library.Editor'),
        ),
        migrations.AddField(
            model_name='book',
            name='press',
            field=models.ForeignKey(to='library.Press'),
        ),
    ]
