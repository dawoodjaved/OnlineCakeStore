
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210320_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Genoise Cake', 'Genoise Cake'), ('Angel Food Cake', 'Angel Food Cake'), ('Biscuit Cake', 'Biscuit Cake')], max_length=50, null=True),
        ),
    ]
