# Generated by Django 2.2.2 on 2019-06-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_p_tree_traversal', '0003_auto_20190604_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder_file',
            name='container',
        ),
    ]