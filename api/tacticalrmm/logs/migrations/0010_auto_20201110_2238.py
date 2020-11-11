# Generated by Django 3.1.2 on 2020-11-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0009_auto_20201110_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='action',
            field=models.CharField(choices=[('login', 'User Login'), ('failed_login', 'Failed User Login'), ('delete', 'Delete Object'), ('modify', 'Modify Object'), ('add', 'Add Object'), ('view', 'View Object'), ('check_run', 'Check Run'), ('task_run', 'Task Run'), ('agent_install', 'Agent Install'), ('remote_session', 'Remote Session'), ('execute_script', 'Execute Script'), ('execute_command', 'Execute Command'), ('bulk_action', 'Bulk Action')], max_length=100),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='object_type',
            field=models.CharField(choices=[('user', 'User'), ('script', 'Script'), ('agent', 'Agent'), ('policy', 'Policy'), ('winupdatepolicy', 'Patch Policy'), ('client', 'Client'), ('site', 'Site'), ('check', 'Check'), ('automatedtask', 'Automated Task'), ('coresettings', 'Core Settings'), ('bulk', 'Bulk')], max_length=100),
        ),
    ]
