# Generated by Django 4.2.3 on 2024-06-30 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_product_content_ru_remove_product_content_uz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freeproduct',
            options={'verbose_name': 'Free Product', 'verbose_name_plural': 'Free Products'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='count_ru',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='count_uz',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='free_products_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='free_products_uz',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='product_ru',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='freeproduct',
            name='product_uz',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
