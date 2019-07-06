# Generated by Django 2.2.1 on 2019-07-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, max_length=140)),
                ('price', models.IntegerField()),
                ('menu_img', models.ImageField(default='avatars/default.png', upload_to='menu/')),
            ],
        ),
    ]
