# Generated by Django 4.0.4 on 2022-05-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_home_login2_home_login3_home_text_home_text2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
