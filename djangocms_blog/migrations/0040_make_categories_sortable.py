from django.db import migrations, models


def make_categories_sortable(apps, schema_editor):
    BlogCategory = apps.get_model("djangocms_blog", "BlogCategory")
    order_count = 0
    for category in BlogCategory.objects.all().order_by("-id"):
        category.order = order_count
        category.save()
        order_count += 1


def make_categories_sortable_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0039_auto_20200331_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'ordering': ['order'], 'verbose_name': 'blog category', 'verbose_name_plural': 'blog categories'},
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RunPython(make_categories_sortable, make_categories_sortable_reverse),
    ]
