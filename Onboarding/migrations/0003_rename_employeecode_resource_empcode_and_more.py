# Generated by Django 4.1.5 on 2023-02-01 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Onboarding', '0002_rename_empbilled_resource_billed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='EmployeeCode',
            new_name='EmpCode',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='Designation',
            new_name='EmpName',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='EmployeeName',
            new_name='Role',
        ),
    ]
