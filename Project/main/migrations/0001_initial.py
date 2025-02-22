# Generated by Django 4.1.7 on 2023-02-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('feature_image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('department', models.CharField(choices=[('HC', 'Heart Center'), ('NC', 'Neuroscience Center'), ('OC', 'Obesity Center'), ('EC', 'Eye Center'), ('OC', 'Orthopedic Center'), ('PC', 'Pediatric Center')], max_length=300)),
                ('established_at', models.DateTimeField()),
            ],
        ),
    ]
