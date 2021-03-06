# Generated by Django 3.0.7 on 2020-06-25 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20200625_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author', verbose_name='ФИО автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.IntegerField(default=1, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='borrowed_books', to='p_library.Friend', verbose_name='Имя друга'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_borrowed',
            field=models.BooleanField(default=False, verbose_name='Одолжена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Publisher', verbose_name='Издательство'),
        ),
    ]
