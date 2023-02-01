# Generated by Django 4.1.5 on 2023-02-01 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Onboarding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='EmpBilled',
            new_name='Billed',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpLocation',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpCode',
            new_name='EmployeeCode',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpName',
            new_name='EmployeeName',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpGrade',
            new_name='Grade',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpRole',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmpStatus',
            new_name='Status',
        ),
    ]
