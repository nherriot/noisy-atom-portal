# Generated by Django 2.2.27 on 2022-02-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, height_field=250, max_length=50, upload_to='', width_field=250)),
                ('is_active', models.BooleanField(default=True)),
                ('trigger', models.DateTimeField()),
                ('primary_url', models.URLField()),
                ('secondary_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'QRCode',
                'db_table': 'QRCodes',
                'ordering': ['-created_at'],
            },
        ),
    ]