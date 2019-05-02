# Generated by Django 2.1.1 on 2019-04-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190407_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='total_k12_hours',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='total_k12_students',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='total_other_community_members',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='total_uno_faculty',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='total_uno_hours',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='total_uno_students',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_k12_hours',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_k12_students',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_other_community_members',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_uno_faculty',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_uno_hours',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_uno_students',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]