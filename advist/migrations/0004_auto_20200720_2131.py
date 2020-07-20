# Generated by Django 3.0.8 on 2020-07-20 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advist', '0003_auto_20200720_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='advistments',
            options={'ordering': ['-published'], 'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.AlterField(
            model_name='advistments',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='advistments',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='advistments',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='advist.Rubric', verbose_name='Рубрика'),
        ),
    ]
