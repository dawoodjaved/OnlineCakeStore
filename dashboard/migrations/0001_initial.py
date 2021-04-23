
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Butter Cake', 'Butter Cake'), ('Pound Cake', 'Pound Cake'), ('Sponge Cake', 'Sponge Cake')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
    ]
