from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_alter_size_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothing",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/clothing"
            ),
        ),
    ]
