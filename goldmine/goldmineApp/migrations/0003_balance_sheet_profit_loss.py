# Generated by Django 4.0.5 on 2023-07-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldmineApp', '0002_ledger_d_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liabilities', models.CharField(max_length=100, null=True)),
                ('cr_amount', models.IntegerField()),
                ('asset', models.CharField(max_length=100, null=True)),
                ('dr_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'Balance_Sheet',
            },
        ),
        migrations.CreateModel(
            name='Profit_Loss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_perticular', models.CharField(max_length=100, null=True)),
                ('income_perticular_amount', models.IntegerField()),
                ('expense_perticular', models.CharField(max_length=100, null=True)),
                ('expense_perticular_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'Profit_Loss',
            },
        ),
    ]
