# Generated by Django 5.0.6 on 2024-06-13 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(blank=True, default=0)),
                ('address', models.CharField(max_length=50)),
                ('coin', models.CharField(max_length=5)),
                ('chain_id', models.IntegerField()),
                ('transactions', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WalletContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('reserved', models.BooleanField()),
                ('chain_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.IntegerField(blank=True, default=0)),
                ('tx_hash', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=1000000)),
                ('to', models.CharField(max_length=50)),
                ('confirmations', models.IntegerField(blank=True, default=0)),
                ('status', models.IntegerField()),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_core.wallet')),
            ],
        ),
    ]