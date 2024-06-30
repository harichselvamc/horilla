# Generated by Django 4.2.11 on 2024-06-18 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        ('employee', '0001_initial'),
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='assetrequest',
            name='requested_employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_employee', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='assetreport',
            name='asset_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_report', to='asset.asset'),
        ),
        migrations.AddField(
            model_name='assetreport',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetreport',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='assetlot',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='assetlot',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetlot',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='assetdocuments',
            name='asset_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='asset.assetreport'),
        ),
        migrations.AddField(
            model_name='assetdocuments',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetdocuments',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='assetcategory',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='assetcategory',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetcategory',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='asset_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.asset', verbose_name='asset'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='assign_images',
            field=models.ManyToManyField(blank=True, related_name='assign_images', to='asset.returnimages'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='assigned_by_employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_by', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='assigned_to_employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='allocated_employeee', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='assetassignment',
            name='return_images',
            field=models.ManyToManyField(blank=True, related_name='return_images', to='asset.returnimages'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asset.assetcategory'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_lot_number_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='asset.assetlot'),
        ),
        migrations.AddField(
            model_name='asset',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='asset',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.employee'),
        ),
    ]
