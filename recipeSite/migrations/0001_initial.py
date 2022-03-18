# Generated by Django 2.1.5 on 2022-03-17 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submissionDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeName', models.CharField(max_length=50, unique=True)),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('method', models.TextField(max_length=500)),
                ('cookTime', models.IntegerField(default=0)),
                ('difficulty', models.CharField(choices=[('EASY', 'Easy to Make'), ('MEDIUM', 'Moderately Difficult'), ('HARD', 'Hard to Make')], default='EASY', max_length=6)),
                ('servings', models.PositiveIntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='recipeImages')),
                ('slug', models.SlugField()),
                ('submissionDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookmarks', models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeSite.Recipe'),
        ),
        migrations.AddField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeSite.Recipe'),
        ),
    ]
