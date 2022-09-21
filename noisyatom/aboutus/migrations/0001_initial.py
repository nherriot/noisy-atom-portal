# Generated by Django 2.0 on 2022-07-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.TextField()),
                ('position', models.CharField(max_length=200)),
                ('card_description', models.CharField(max_length=200)),
                ('project_date', models.DateTimeField(verbose_name='date published')),
                ('picture', models.ImageField(default='RP2040_Pico.png', upload_to='profile/')),
            ],
        ),
    ]
