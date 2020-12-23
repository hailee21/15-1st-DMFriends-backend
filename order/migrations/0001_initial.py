# Generated by Django 3.1.4 on 2020-12-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=45)),
                ('detail_address', models.CharField(max_length=45)),
                ('default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=45)),
                ('delivery_message', models.CharField(max_length=500)),
                ('order_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'orderstatuses',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_pay', models.CharField(max_length=45)),
                ('virtual_account', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'paymentstatuses',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'paymenttypes',
            },
        ),
    ]
