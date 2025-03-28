# Generated by Django 5.1.7 on 2025-03-12 01:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_director_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='Movie',
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
            preserve_default=False,
        ),
    ]
