from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0007_designer_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="designer",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
