# Generated by Django 5.0.3 on 2024-06-01 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewFeedbackSystem', '0003_bewertung_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='bewertung',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bewertungen', to='ReviewFeedbackSystem.user'),
        ),
        migrations.AlterField(
            model_name='bewertung',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bewertungen', to='ReviewFeedbackSystem.restaurant'),
        ),
    ]