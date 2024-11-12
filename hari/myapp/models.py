from django.db import models
from django.contrib import admin
class BankLoanDB(models.Model):
     name=models.CharField(max_length=20)
     loanID=models.IntegerField(primary_key="True")
     accNo=models.IntegerField()
     occupation=models.CharField(max_length=20)
     collateral=models.CharField(max_length=30)


class BankLoanDBAdmin(admin.ModelAdmin):
     list_display=('name','loanID','accNo','occupation','collateral')
