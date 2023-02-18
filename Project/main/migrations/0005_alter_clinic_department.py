# Generated by Django 4.1.5 on 2023-02-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_appointment_is_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('Heart Center', 'Heart Center'), ('Neuroscience Center', 'Neuroscience Center'), ('Obesity Center', 'Obesity Center'), ('Eye Center', 'Eye Center'), ('Orthopedic Center', 'Orthopedic Center'), ('Pediatric Center', 'Pediatric Center')], max_length=300),
        ),
    ]