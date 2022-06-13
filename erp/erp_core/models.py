from enum import Enum
from django.db import models


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]
    
class Company(models.Model):
    """Create company profile and their attributes"""
    class Meta:
        verbose_name_plural = "Companies"
    
    class Industry(ChoiceEnum):
        """Create industry choices"""
        ENERGY = 'Energy'
        RETAIL = 'Retail'
        TECH = 'Tech'
        OTHER = 'Other'
         
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    industry = models.CharField(max_length=15, choices=Industry.choices(), default=Industry.TECH)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zip_code =  models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name.upper()
    
class Invoice(models.Model):
    """Create invoice and their attributes"""
    class Kind(ChoiceEnum):
        """Create industry choices"""
        ACTIVE = 'Active'
        PASSIVE = 'Passive'
        CREDIT = 'Credit Note'
    
    class Status(ChoiceEnum):
        PAID = "Paid"
        UNPAID = "Unpaid"
        
    sender = models.ForeignKey(Company, related_name="invoice_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Company, related_name="invoice_receiver", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    number = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=10, choices=Kind.choices())
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices(), default=Status.UNPAID)
    notes = models.TextField(blank=True, null=True)
