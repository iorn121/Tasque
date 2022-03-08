# Generated by Django 4.0.2 on 2022-03-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
        migrations.AddField(
            model_name='task',
            name='detail',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='詳細'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タスク名'),
        ),
    ]