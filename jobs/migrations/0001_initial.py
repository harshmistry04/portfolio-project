# Generated by Django 2.1.4 on 2018-12-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='impages/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
