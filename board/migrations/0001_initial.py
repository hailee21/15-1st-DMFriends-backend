# Generated by Django 3.1.4 on 2020-12-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=150)),
                ('theme', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'boards',
            },
        ),
        migrations.CreateModel(
            name='BoardImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'boardimages',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.board')),
                ('self_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.comment')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
