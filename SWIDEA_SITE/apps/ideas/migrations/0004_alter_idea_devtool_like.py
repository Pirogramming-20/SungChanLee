# Generated by Django 5.0.1 on 2024-01-17 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtools', '0001_initial'),
        ('ideas', '0003_idea_devtool_alter_idea_image_alter_idea_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtools.devtool', verbose_name='개발툴'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.idea')),
            ],
        ),
    ]
