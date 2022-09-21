# Generated by Django 2.0 on 2022-07-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0004_auto_20220729_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('card_description', models.TextField()),
                ('linkedIn', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('google', models.CharField(max_length=300)),
                ('picture', models.ImageField(default='RP2040_Pico.png', upload_to='profile/')),
                ('project_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='card_description',
        ),
        migrations.RemoveField(
            model_name='about',
            name='card_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='google',
        ),
        migrations.RemoveField(
            model_name='about',
            name='linkedIn',
        ),
        migrations.RemoveField(
            model_name='about',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='about',
            name='position',
        ),
        migrations.RemoveField(
            model_name='about',
            name='project_date',
        ),
        migrations.RemoveField(
            model_name='about',
            name='twitter',
        ),
    ]
