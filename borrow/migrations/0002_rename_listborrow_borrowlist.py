# Generated by Django 4.2.11 on 2024-03-17 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListBorrow',
            new_name='BorrowList',
        ),
    ]
