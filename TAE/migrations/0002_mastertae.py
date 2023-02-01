# Generated by Django 4.1.5 on 2023-01-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterTAE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Project', models.CharField(max_length=200)),
                ('Project_Task', models.CharField(max_length=200)),
                ('Activity', models.CharField(max_length=200)),
                ('Role', models.CharField(max_length=200)),
                ('Internal_Note', models.CharField(max_length=200)),
                ('Bill_Rate', models.CharField(max_length=200)),
                ('Bill_Hrs', models.CharField(max_length=200)),
                ('NB_Hrs', models.CharField(max_length=200)),
                ('Total_Hrs', models.CharField(max_length=200)),
                ('Revenue', models.CharField(max_length=200)),
                ('Reason', models.CharField(max_length=200)),
            ],
        ),
    ]