# Generated by Django 4.2.11 on 2024-06-18 12:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('base', '0001_initial'),
        ('horilla_audit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeKeyResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_result', models.CharField(blank=True, max_length=60, null=True)),
                ('key_result_description', models.TextField(blank=True, max_length=255, null=True)),
                ('progress_type', models.CharField(blank=True, choices=[('%', 'Percentage'), ('#', 'Number'), ('Currency', (('$', 'USD$'), ('₹', 'INR'), ('€', 'EUR')))], max_length=60, null=True)),
                ('status', models.CharField(blank=True, choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=20, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('start_value', models.IntegerField(blank=True, default=0, null=True)),
                ('current_value', models.IntegerField(blank=True, default=0, null=True)),
                ('target_value', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('progress_percentage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('objective', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('objective_description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=20)),
                ('progress_percentage', models.IntegerField(default=0)),
                ('archive', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_objective', to='employee.employee', verbose_name='Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('review_cycle', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=50)),
                ('archive', models.BooleanField(blank=True, default=False, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('cyclic_feedback', models.BooleanField(default=False)),
                ('cyclic_feedback_days_count', models.IntegerField(blank=True, null=True)),
                ('cyclic_feedback_period', models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months'), ('years', 'Years')], max_length=50, null=True)),
                ('cyclic_next_start_date', models.DateField(blank=True, null=True)),
                ('cyclic_next_end_date', models.DateField(blank=True, null=True)),
                ('colleague_id', models.ManyToManyField(blank=True, related_name='feedback_colleague', to='employee.employee')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='feedback_employee', to='employee.employee')),
                ('employee_key_results_id', models.ManyToManyField(blank=True, to='pms.employeekeyresult')),
                ('manager_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='feedback_manager', to='employee.employee')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='KeyResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('title', models.CharField(max_length=60, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('progress_type', models.CharField(choices=[('%', 'Percentage'), ('#', 'Number'), ('Currency', (('$', 'USD$'), ('₹', 'INR'), ('€', 'EUR')))], default='%', max_length=60)),
                ('target_value', models.IntegerField(blank=True, default=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('show_response', models.BooleanField(default=False)),
                ('answer_employees', models.ManyToManyField(blank=True, related_name='meeting_answer_employees', to='employee.employee', verbose_name='Answerable Employees')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('employee_id', models.ManyToManyField(related_name='meeting_employee', to='employee.employee', verbose_name='Employee')),
                ('manager', models.ManyToManyField(related_name='meeting_manager', to='employee.employee')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'Meetings',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('question', models.CharField(max_length=250)),
                ('question_type', models.CharField(blank=True, choices=[('1', 'Text'), ('2', 'Rating'), ('3', 'Boolean'), ('4', 'Multi-choices'), ('5', 'Likert')], max_length=100, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('question_template', models.CharField(max_length=100, unique=True)),
                ('company_id', models.ManyToManyField(blank=True, to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('option_a', models.CharField(blank=True, max_length=250, null=True)),
                ('option_b', models.CharField(blank=True, max_length=250, null=True)),
                ('option_c', models.CharField(blank=True, max_length=250, null=True)),
                ('option_d', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('question_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='question_options', to='pms.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='template_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='pms.questiontemplate'),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('period_name', models.CharField(max_length=150, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company_id', models.ManyToManyField(blank=True, to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('duration_unit', models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months'), ('years', 'Years')], default='days', max_length=20, null=True, verbose_name='Duration Unit')),
                ('duration', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('add_assignees', models.BooleanField(default=False)),
                ('archive', models.BooleanField(blank=True, default=False, null=True)),
                ('assignees', models.ManyToManyField(blank=True, related_name='assignees_objective', to='employee.employee', verbose_name='Assignees')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('key_result_id', models.ManyToManyField(blank=True, related_name='objective', to='pms.keyresult', verbose_name='Default Key results')),
                ('managers', models.ManyToManyField(blank=True, related_name='objective', to='employee.employee', verbose_name='Managers')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MeetingsAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(blank=True, max_length=200, null=True)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_meeting_answer', to='employee.employee', verbose_name='Employee')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='meeting_answer', to='pms.meetings')),
                ('question_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeting_answer_question_id', to='pms.question')),
            ],
        ),
        migrations.AddField(
            model_name='meetings',
            name='question_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pms.questiontemplate'),
        ),
        migrations.CreateModel(
            name='KeyResultFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(blank=True, max_length=200, null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_key_result', to='employee.employee')),
                ('feedback_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='feedback_key_result', to='pms.feedback')),
                ('key_result_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='key_result_feedback', to='pms.employeekeyresult')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalObjective',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('history_title', models.CharField(blank=True, max_length=20, null=True)),
                ('history_description', models.TextField(null=True)),
                ('history_highlight', models.BooleanField(default=False, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('duration_unit', models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months'), ('years', 'Years')], default='days', max_length=20, null=True, verbose_name='Duration Unit')),
                ('duration', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('add_assignees', models.BooleanField(default=False)),
                ('archive', models.BooleanField(blank=True, default=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('history_tags', models.ManyToManyField(to='horilla_audit.audittag')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'historical objective',
                'verbose_name_plural': 'historical objectives',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalKeyResult',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('history_title', models.CharField(blank=True, max_length=20, null=True)),
                ('history_description', models.TextField(null=True)),
                ('history_highlight', models.BooleanField(default=False, null=True)),
                ('title', models.CharField(max_length=60, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('progress_type', models.CharField(choices=[('%', 'Percentage'), ('#', 'Number'), ('Currency', (('$', 'USD$'), ('₹', 'INR'), ('€', 'EUR')))], default='%', max_length=60)),
                ('target_value', models.IntegerField(blank=True, default=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('history_tags', models.ManyToManyField(to='horilla_audit.audittag')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'historical key result',
                'verbose_name_plural': 'historical key results',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEmployeeObjective',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('history_title', models.CharField(blank=True, max_length=20, null=True)),
                ('history_description', models.TextField(null=True)),
                ('history_highlight', models.BooleanField(default=False, null=True)),
                ('objective', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('objective_description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('created_at', models.DateField(blank=True, editable=False)),
                ('updated_at', models.DateField(blank=True, editable=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=20)),
                ('progress_percentage', models.IntegerField(default=0)),
                ('archive', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('employee_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee', verbose_name='Employee')),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_set', to='pms.employeeobjective')),
                ('history_tags', models.ManyToManyField(to='horilla_audit.audittag')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('objective_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pms.objective', verbose_name='Objective')),
            ],
            options={
                'verbose_name': 'historical employee objective',
                'verbose_name_plural': 'historical employee objectives',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEmployeeKeyResult',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_title', models.CharField(blank=True, max_length=20, null=True)),
                ('history_description', models.TextField(null=True)),
                ('history_highlight', models.BooleanField(default=False, null=True)),
                ('key_result', models.CharField(blank=True, max_length=60, null=True)),
                ('key_result_description', models.TextField(blank=True, max_length=255, null=True)),
                ('progress_type', models.CharField(blank=True, choices=[('%', 'Percentage'), ('#', 'Number'), ('Currency', (('$', 'USD$'), ('₹', 'INR'), ('€', 'EUR')))], max_length=60, null=True)),
                ('status', models.CharField(blank=True, choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=20, null=True)),
                ('created_at', models.DateField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateField(blank=True, editable=False, null=True)),
                ('start_value', models.IntegerField(blank=True, default=0, null=True)),
                ('current_value', models.IntegerField(blank=True, default=0, null=True)),
                ('target_value', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('progress_percentage', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('employee_objective_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pms.employeeobjective')),
                ('history_tags', models.ManyToManyField(to='horilla_audit.audittag')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('key_result_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pms.keyresult', verbose_name='Key result')),
            ],
            options={
                'verbose_name': 'historical employee key result',
                'verbose_name_plural': 'historical employee key results',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalComment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_title', models.CharField(blank=True, max_length=20, null=True)),
                ('history_description', models.TextField(null=True)),
                ('history_highlight', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('employee_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.employee')),
                ('employee_objective_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pms.employeeobjective')),
                ('history_tags', models.ManyToManyField(to='horilla_audit.audittag')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical comment',
                'verbose_name_plural': 'historical comments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='feedback',
            name='question_template_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='feedback_question_template', to='pms.questiontemplate'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='subordinate_id',
            field=models.ManyToManyField(blank=True, related_name='feedback_subordinate', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='employeeobjective',
            name='key_result_id',
            field=models.ManyToManyField(blank=True, related_name='employee_objective', to='pms.keyresult', verbose_name='Key results'),
        ),
        migrations.AddField(
            model_name='employeeobjective',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='employeeobjective',
            name='objective_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_objective', to='pms.objective', verbose_name='Objective'),
        ),
        migrations.AddField(
            model_name='employeekeyresult',
            name='employee_objective_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_key_result', to='pms.employeeobjective'),
        ),
        migrations.AddField(
            model_name='employeekeyresult',
            name='key_result_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_key_result', to='pms.keyresult', verbose_name='Key result'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment', to='employee.employee')),
                ('employee_objective_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_objective', to='pms.employeeobjective')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(blank=True, max_length=200, null=True)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_answer', to='employee.employee')),
                ('feedback_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feedback_answer', to='pms.feedback')),
                ('question_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_question_id', to='pms.question')),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_subject', models.CharField(max_length=100)),
                ('based_on', models.CharField(choices=[('general', 'General'), ('employee', 'Employee'), ('department', 'Department'), ('job_position', 'Job Position')], default='general', max_length=50)),
                ('status', models.CharField(choices=[('On Track', 'On Track'), ('Behind', 'Behind'), ('Closed', 'Closed'), ('At Risk', 'At Risk'), ('Not Started', 'Not Started')], default='Not Started', max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('archive', models.BooleanField(blank=True, default=False, null=True)),
                ('anonymous_feedback_id', models.CharField(editable=False, max_length=10, null=True)),
                ('feedback_description', models.TextField(blank=True, max_length=255, null=True)),
                ('department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.department', verbose_name='Department')),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee')),
                ('job_position_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.jobposition', verbose_name='Job Position')),
            ],
        ),
    ]
