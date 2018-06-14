# Generated by Django 2.0.6 on 2018-06-14 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部活名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='club',
            field=models.ManyToManyField(to='employee.Club', verbose_name='部活'),
        ),
    ]
