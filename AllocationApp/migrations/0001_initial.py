# Generated by Django 3.2.7 on 2021-09-20 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(default='', max_length=100)),
                ('Project_Description', models.CharField(default='', max_length=200)),
                ('Project_Department', models.CharField(default='', max_length=200)),
                ('StartDate_pro', models.DateField()),
                ('EndDate_pro', models.DateField()),
                ('Created_at', models.DateTimeField(auto_now=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ResourceName', models.CharField(max_length=100)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Created_at', models.DateTimeField(auto_now=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate_all', models.DateField()),
                ('EndDate_all', models.DateField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('points', models.CharField(max_length=4)),
                ('StartDay_all', models.IntegerField()),
                ('EndDay_all', models.IntegerField()),
                ('Created_at', models.DateTimeField(auto_now=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Deleted_at', models.DateTimeField(auto_now=True)),
                ('Project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AllocationApp.project')),
                ('Resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AllocationApp.resource')),
            ],
        ),
        migrations.CreateModel(
            name='DateSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.DateField()),
                ('DayValue', models.CharField(max_length=4)),
                ('day_week', models.CharField(default='', max_length=25)),
                ('Allocation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AllocationApp.resourceallocation')),
            ],
        ),
    ]