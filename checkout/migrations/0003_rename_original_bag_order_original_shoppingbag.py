# Generated by Django 3.2.20 on 2023-07-20 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20230719_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_shoppingbag',
        ),
    ]
