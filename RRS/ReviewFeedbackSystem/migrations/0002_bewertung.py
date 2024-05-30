# Generated by Django 5.0.3 on 2024-05-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewFeedbackSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bewertung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bewertung', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('mit_wem', models.CharField(choices=[('geschäftsreise', 'Geschäftsreise'), ('als_paar', 'Als Paar'), ('familie', 'Familie'), ('mit_freunden', 'Mit Freunden'), ('alleine', 'Alleine')], max_length=20)),
                ('anlass', models.CharField(choices=[('frühstück', 'Frühstück'), ('brunch', 'Brunch'), ('mittagessen', 'Mittagessen'), ('abendessen', 'Abendessen'), ('dessert', 'Dessert'), ('kaffee_oder_tee', 'Kaffee oder Tee')], max_length=20)),
                ('kommentar', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
