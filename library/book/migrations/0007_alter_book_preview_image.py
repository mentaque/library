# Generated by Django 4.1.7 on 2023-03-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_preview_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='preview_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
