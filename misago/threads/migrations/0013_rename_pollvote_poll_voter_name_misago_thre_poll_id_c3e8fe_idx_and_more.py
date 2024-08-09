# Generated by Django 4.2.7 on 2023-11-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misago_acl", "0004_cache_version"),
        ("misago_threads", "0012_set_dj_partial_indexes"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="pollvote",
            new_name="misago_thre_poll_id_c3e8fe_idx",
            old_fields=("poll", "voter_name"),
        ),
        migrations.RenameIndex(
            model_name="post",
            new_name="misago_thre_thread__4e5114_idx",
            old_fields=("thread", "id"),
        ),
        migrations.RenameIndex(
            model_name="post",
            new_name="misago_thre_poster__eefeb2_idx",
            old_fields=("poster", "posted_on"),
        ),
        migrations.RenameIndex(
            model_name="post",
            new_name="misago_thre_is_even_d29c90_idx",
            old_fields=("is_event", "is_hidden"),
        ),
        migrations.RenameIndex(
            model_name="subscription",
            new_name="misago_thre_send_em_da8b99_idx",
            old_fields=("send_email", "last_read_on"),
        ),
        migrations.RenameIndex(
            model_name="thread",
            new_name="misago_thre_categor_6cb52c_idx",
            old_fields=("category", "id"),
        ),
        migrations.RenameIndex(
            model_name="thread",
            new_name="misago_thre_categor_7ec8b0_idx",
            old_fields=("category", "last_post_on"),
        ),
        migrations.RenameIndex(
            model_name="thread",
            new_name="misago_thre_categor_c5eaf1_idx",
            old_fields=("category", "replies"),
        ),
        migrations.AlterField(
            model_name="attachmenttype",
            name="limit_downloads_to",
            field=models.ManyToManyField(
                blank=True, related_name="+", to="misago_acl.role"
            ),
        ),
        migrations.AlterField(
            model_name="attachmenttype",
            name="limit_uploads_to",
            field=models.ManyToManyField(
                blank=True, related_name="+", to="misago_acl.role"
            ),
        ),
    ]