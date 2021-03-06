# Generated by Django 2.2.2 on 2019-06-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_p_tree_traversal', '0002_folder_file_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder_file',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder_file',
            name='container',
            field=models.FileField(default='./', upload_to='mptt_directory/'),
        ),
    ]
