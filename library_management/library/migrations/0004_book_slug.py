# Generated by Django 5.0.7 on 2024-07-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]