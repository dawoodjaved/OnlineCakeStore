
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
