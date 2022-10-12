# Generated by Django 4.1.2 on 2022-10-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='')),
                ('summary', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
    ]
