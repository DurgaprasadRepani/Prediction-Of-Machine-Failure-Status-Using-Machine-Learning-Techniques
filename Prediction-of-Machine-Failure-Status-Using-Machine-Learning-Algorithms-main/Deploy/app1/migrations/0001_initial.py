# Generated by Django 4.0.3 on 2023-08-28 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Industries',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Machine_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Company_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.ImageField(blank=True, null=True, upload_to='profileimages')),
                ('licence_no', models.CharField(max_length=200)),
                ('operator_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('Industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Industries', to='app1.industry')),
                ('machine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Types', to='app1.machine_type')),
            ],
        ),
    ]
