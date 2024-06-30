# Generated by Django 4.2.11 on 2024-06-18 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('attendance', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
        ('horilla_audit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktyperequestcomment',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='worktyperequestcomment',
            name='files',
            field=models.ManyToManyField(blank=True, to='base.baserequestfile'),
        ),
        migrations.AddField(
            model_name='worktyperequestcomment',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='worktyperequestcomment',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.worktyperequest'),
        ),
        migrations.AddField(
            model_name='worktyperequest',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='worktyperequest',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='work_type_request', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='worktyperequest',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='worktyperequest',
            name='previous_work_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previous_work_type', to='base.worktype', verbose_name='Previous Work Type'),
        ),
        migrations.AddField(
            model_name='worktyperequest',
            name='work_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_work_type', to='base.worktype', verbose_name='Requesting Work Type'),
        ),
        migrations.AddField(
            model_name='worktype',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='worktype',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='worktype',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='tags',
            name='company_id',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.company'),
        ),
        migrations.AddField(
            model_name='tags',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='tags',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='shiftrequestcomment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='shiftrequestcomment',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='shiftrequestcomment',
            name='files',
            field=models.ManyToManyField(blank=True, to='base.baserequestfile'),
        ),
        migrations.AddField(
            model_name='shiftrequestcomment',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='shiftrequestcomment',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.shiftrequest'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shift_request', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='previous_shift_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previous_shift', to='base.employeeshift', verbose_name='Previous Shift'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='reallocate_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reallocate_shift_request', to='employee.employee', verbose_name='Reallocate Employee'),
        ),
        migrations.AddField(
            model_name='shiftrequest',
            name='shift_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_shift', to='base.employeeshift', verbose_name='Requesting Shift'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='current_work_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_work_type', to='base.worktype', verbose_name='Current Work Type'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='next_work_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_work_type', to='base.worktype', verbose_name='Next Work Type'),
        ),
        migrations.AddField(
            model_name='rotatingworktypeassign',
            name='rotating_work_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.rotatingworktype', verbose_name='Rotating Work Type'),
        ),
        migrations.AddField(
            model_name='rotatingworktype',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='rotatingworktype',
            name='employee_id',
            field=models.ManyToManyField(through='base.RotatingWorkTypeAssign', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='rotatingworktype',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='rotatingworktype',
            name='work_type1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='work_type1', to='base.worktype', verbose_name='Work Type 1'),
        ),
        migrations.AddField(
            model_name='rotatingworktype',
            name='work_type2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='work_type2', to='base.worktype', verbose_name='Work Type 2'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='current_shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_shift', to='base.employeeshift', verbose_name='Current Shift'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='next_shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_shift', to='base.employeeshift', verbose_name='Next Shift'),
        ),
        migrations.AddField(
            model_name='rotatingshiftassign',
            name='rotating_shift_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.rotatingshift', verbose_name='Rotating Shift'),
        ),
        migrations.AddField(
            model_name='rotatingshift',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='rotatingshift',
            name='employee_id',
            field=models.ManyToManyField(through='base.RotatingShiftAssign', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='rotatingshift',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='rotatingshift',
            name='shift1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shift1', to='base.employeeshift', verbose_name='Shift 1'),
        ),
        migrations.AddField(
            model_name='rotatingshift',
            name='shift2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shift2', to='base.employeeshift', verbose_name='Shift 2'),
        ),
        migrations.AddField(
            model_name='multipleapprovalmanagers',
            name='condition_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.multipleapprovalcondition'),
        ),
        migrations.AddField(
            model_name='multipleapprovalcondition',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='multipleapprovalcondition',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.department'),
        ),
        migrations.AddField(
            model_name='multipleapprovalcondition',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='job_position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.jobposition', verbose_name='Job Position'),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_position', to='base.department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='employee_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_set', to='base.worktyperequest'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='history_tags',
            field=models.ManyToManyField(to='horilla_audit.audittag'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='modified_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='previous_work_type_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.worktype', verbose_name='Previous Work Type'),
        ),
        migrations.AddField(
            model_name='historicalworktyperequest',
            name='work_type_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.worktype', verbose_name='Requesting Work Type'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='employee_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_set', to='base.shiftrequest'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='history_tags',
            field=models.ManyToManyField(to='horilla_audit.audittag'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='modified_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='previous_shift_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.employeeshift', verbose_name='Previous Shift'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='reallocate_to',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Reallocate Employee'),
        ),
        migrations.AddField(
            model_name='historicalshiftrequest',
            name='shift_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.employeeshift', verbose_name='Requesting Shift'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='current_work_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.worktype', verbose_name='Current Work Type'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='employee_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_set', to='base.rotatingworktypeassign'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='history_tags',
            field=models.ManyToManyField(to='horilla_audit.audittag'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='modified_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='next_work_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.worktype', verbose_name='Next Work Type'),
        ),
        migrations.AddField(
            model_name='historicalrotatingworktypeassign',
            name='rotating_work_type_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.rotatingworktype', verbose_name='Rotating Work Type'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='current_shift',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.employeeshift', verbose_name='Current Shift'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='employee_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_set', to='base.rotatingshiftassign'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='history_tags',
            field=models.ManyToManyField(to='horilla_audit.audittag'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='modified_by',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='next_shift',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.employeeshift', verbose_name='Next Shift'),
        ),
        migrations.AddField(
            model_name='historicalrotatingshiftassign',
            name='rotating_shift_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.rotatingshift', verbose_name='Rotating Shift'),
        ),
        migrations.AddField(
            model_name='employeetype',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='employeetype',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='employeetype',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='employeeshiftschedule',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='employeeshiftschedule',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='employeeshiftschedule',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='day_schedule', to='base.employeeshiftday'),
        ),
        migrations.AddField(
            model_name='employeeshiftschedule',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='employeeshiftschedule',
            name='shift_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.employeeshift', verbose_name='Shift'),
        ),
        migrations.AddField(
            model_name='employeeshiftday',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='days',
            field=models.ManyToManyField(through='base.EmployeeShiftSchedule', to='base.employeeshiftday'),
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='grace_time_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_shift', to='attendance.gracetime', verbose_name='Grace Time'),
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='emaillog',
            name='company_id',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
        migrations.AddField(
            model_name='dynamicpagination',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_pagination', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='dynamicemailconfiguration',
            name='company_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
        migrations.AddField(
            model_name='dynamicemailconfiguration',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='dynamicemailconfiguration',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='driverviewed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='company_id',
            field=models.ManyToManyField(blank=True, to='base.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='department',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='dashboardemployeecharts',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='dashboardemployeecharts',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='dashboardemployeecharts',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='company',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='biometricattendance',
            name='company_id',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='biometric_enabled_company', to='base.company'),
        ),
        migrations.AddField(
            model_name='announcementview',
            name='announcement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.announcement'),
        ),
        migrations.AddField(
            model_name='announcementview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='announcementcomment',
            name='announcement_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.announcement'),
        ),
        migrations.AddField(
            model_name='announcementcomment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='announcementcomment',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='announcementcomment',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='attachments',
            field=models.ManyToManyField(blank=True, related_name='announcement_attachments', to='base.attachment'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='department',
            field=models.ManyToManyField(blank=True, to='base.department'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='announcement_employees', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='job_position',
            field=models.ManyToManyField(blank=True, to='base.jobposition'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AlterUniqueTogether(
            name='jobrole',
            unique_together={('job_position_id', 'job_role')},
        ),
        migrations.AlterUniqueTogether(
            name='employeeshiftschedule',
            unique_together={('shift_id', 'day')},
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('company', 'address')},
        ),
    ]
