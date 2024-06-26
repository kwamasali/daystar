# Generated by Django 5.0.3 on 2024-05-20 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
                ('parent', models.CharField(blank=True, max_length=50, null=True)),
                ('student_number', models.CharField(blank=True, max_length=40, null=True)),
                ('gaurdian', models.CharField(blank=True, max_length=10, null=True)),
                ('baby_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DollsShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=70)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('num_available', models.IntegerField(blank=True, null=True)),
                ('payer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=10, null=True)),
                ('sitter_number', models.CharField(blank=True, max_length=40, null=True)),
                ('level_of_education', models.CharField(blank=True, max_length=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=70)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('payment_to_sitter', models.IntegerField(blank=True, null=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.babies')),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.sitter')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('payer', models.CharField(max_length=50)),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.babies')),
                ('typestay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.type_stay')),
            ],
        ),
        migrations.AddField(
            model_name='babies',
            name='typestay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar_app.type_stay'),
        ),
    ]
