# Generated by Django 5.1.1 on 2024-09-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0004_remove_tag_image_remove_tag_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]