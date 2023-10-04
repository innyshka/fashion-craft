from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_rename_materials_material"),
    ]

    operations = [
        migrations.AddField(
            model_name="size",
            name="description",
            field=models.CharField(default=60, max_length=255),
            preserve_default=False,
        ),
    ]
