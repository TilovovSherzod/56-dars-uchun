# Generated by Django 4.2.3 on 2023-07-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.subject'),
        ),
    ]
