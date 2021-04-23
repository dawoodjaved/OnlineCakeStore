from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food')], max_length=50, null=True),
        ),
    ]
