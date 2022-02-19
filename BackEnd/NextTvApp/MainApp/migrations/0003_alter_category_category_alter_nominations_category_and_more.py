# Generated by Django 4.0.2 on 2022-02-19 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_alter_nominations_category_alter_votes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nominations',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.category'),
        ),
        migrations.AlterField(
            model_name='votes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='MainApp.nominations'),
        ),
    ]
