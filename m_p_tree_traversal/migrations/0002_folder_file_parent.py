# Generated by Django 2.2.2 on 2019-06-04 18:38

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('m_p_tree_traversal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder_file',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='m_p_tree_traversal.folder_file'),
        ),
    ]
