from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_alter_clothing_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="designer",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/designers"
            ),
        ),
    ]
