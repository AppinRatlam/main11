from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator

class Devotee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    aadhaar_hash = models.CharField(max_length=64, unique=True)   # ✅ SHA256 hash
    aadhaar_last4 = models.CharField(max_length=4, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)   # ✅ added timestamp

    def __str__(self):
        return f"{self.name} ({self.phone})"

# class Devotee(models.Model):
#     name = models.CharField(max_length=120)
#     phone = models.CharField(
#         max_length=10,
#         validators=[RegexValidator(r'^\d{10}$', 'Enter 10 digit mobile number')],
#     )
#     aadhaar_last4 = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{4}$')])
#     aadhaar_hash = models.CharField(max_length=64, help_text='SHA256 of full Aadhaar for de-duplication')
#     address = models.TextField(blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.phone})"

class Deposit(models.Model):
    STATUS_CHOICES = [
        ('HELD','Held in Temple'),
        ('RETURNED','Returned to Devotee'),
        ('CANCELLED','Cancelled'),
    ]

    devotee = models.ForeignKey(Devotee, on_delete=models.PROTECT, related_name='deposits')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    token = models.CharField(max_length=20, unique=True, db_index=True)
    diwali_year = models.IntegerField(help_text='Diwali cycle year (e.g., 2025)')
    received_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='HELD')
    returned_at = models.DateTimeField(null=True, blank=True)
    remarks = models.CharField(max_length=200, blank=True)
    comment_choice = models.CharField(max_length=50, blank=True, null=True)
    form_filler_name = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.token} - {self.devotee.name} - ₹{self.amount}"
