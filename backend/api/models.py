from django.db import models

class Contact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50)  # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    credit_rating = models.IntegerField(db_column='CREDIT_RATING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'


class LandingRate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    rate = models.DecimalField(db_column='RATE', max_digits=8, decimal_places=2)  # Field name made lowercase.
    loan_intent = models.CharField(db_column='LOAN_INTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'landing_rate'


class CrmDeal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loan_amount = models.BigIntegerField(db_column='LOAN_AMOUNT')  # Field name made lowercase.
    loan_duration = models.IntegerField(db_column='LOAN_DURATION', blank=True, null=True)  # Field name made lowercase.
    responsible = models.ForeignKey('User', db_column='RESPONSIBLE_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    contact = models.ForeignKey(Contact, db_column='CONTANT_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    company = models.ForeignKey('Company', db_column='COMPANY_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    landing_rate = models.ForeignKey(LandingRate, db_column='LANDING_RATE_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    date_create = models.DateTimeField(db_column='DATE_CREATE', auto_now_add=True)  # Field name made lowercase.
    date_closed = models.DateTimeField(db_column='DATE_CLOSED', blank=True, null=True)  # Field name made lowercase.
    stage = models.CharField(db_column='STAGE', max_length=255)  # Field name made lowercase.
    annual_income = models.DecimalField(db_column='ANNUAL_INCOME', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    monthly_salary = models.DecimalField(db_column='MONTHLY_SALARY', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    loan_type = models.CharField(db_column='LOAN_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scoring_result = models.CharField(db_column='SCORING_RESULT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deal_result = models.CharField(db_column='DEAL_RESULT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status_credit = models.CharField(db_column='STATUS_CREDIT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_deal'


class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    ful_name = models.CharField(db_column='FUL_NAME', max_length=255)  # Field name made lowercase.
    representative_name = models.CharField(db_column='REPRESENTATIVE_NAME', max_length=255)  # Field name made lowercase.
    representative_last_name = models.CharField(db_column='REPRESENTATIVE_LAST_NAME', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255)  # Field name made lowercase.
    inn = models.BigIntegerField(db_column='INN')  # Field name made lowercase.
    kpp = models.BigIntegerField(db_column='KPP')  # Field name made lowercase.
    industry = models.CharField(db_column='INDUSTRY', max_length=255)  # Field name made lowercase.
    phone = models.BigIntegerField(db_column='PHONE')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.
    revenue = models.BigIntegerField(db_column='REVENUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Statement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_by = models.ForeignKey(User, db_column='CREATED_BY')  # Field name made lowercase.
    count_month = models.IntegerField(db_column='COUNT_MONTH')  # Field name made lowercase.
    count_contact = models.IntegerField(db_column='COUNT_CONTACT')  # Field name made lowercase.
    count_company = models.IntegerField(db_column='COUNT_COMPANY')  # Field name made lowercase.
    money_turnover = models.BigIntegerField(db_column='MONEY_TURNOVER')  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statement'