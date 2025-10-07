from django import forms
from .models import Devotee, Deposit
import hashlib

class IntakeForm(forms.Form):
    name = forms.CharField(max_length=120, label='Devotee Name')
    phone = forms.CharField(max_length=10, label='Phone (10 digits)')
    aadhaar = forms.CharField(max_length=12, label='Aadhaar (12 digits)')
    address = forms.CharField(widget=forms.Textarea, required=False, label='Address')
    email = forms.EmailField(required=False, label='Email') 
    amount = forms.DecimalField(min_value=1, max_digits=10, decimal_places=2, label='Amount (₹)')
    diwali_year = forms.IntegerField(help_text='Diwali cycle year, e.g. 2025')
    comment_choice = forms.ChoiceField(
        choices=[
            ('₹1 (New)', '₹1 (New)'),
            ('₹1 (Old)', '₹1 (Old)'),
            ('₹2 (New)', '₹2 (New)'),
            ('₹2 (Old)', '₹2 (Old)'),
            ('₹5 (New)', '₹5 (New)'),
            ('₹5 (Old)', '₹5 (Old)'),
            ('₹10 (New)', '₹10 (New)'),
            ('₹10 (Old)', '₹10 (Old)'),
            ('₹20 (New)', '₹20 (New)'),
            ('₹20 (Old)', '₹20 (Old)'),
            ('₹50 (New)', '₹50 (New)'),
            ('₹50 (Old)', '₹50 (Old)'),
            ('₹100 (New)', '₹100 (New)'),
            ('₹100 (Old)', '₹100 (Old)'),
            ('₹200 (New)', '₹200 (New)'),
            ('₹200 (Old)', '₹200 (Old)'),
            ('₹500 (New)', '₹500 (New)'),
            ('₹500 (Old)', '₹500 (Old)'),
            
            
        ],
        required=False,
        label='Comment'
    )
    form_filler_name = forms.CharField(max_length=120, required=False, label='Form Filler Name')
    quantity = forms.IntegerField(min_value=1, initial=1)

    def clean_phone(self):
        p = self.cleaned_data['phone']
        if not p.isdigit() or len(p) != 10:
            raise forms.ValidationError('Enter 10 digit phone number')
        return p

    def clean_aadhaar(self):
        a = self.cleaned_data['aadhaar']
        if not a.isdigit() or len(a) != 12:
            raise forms.ValidationError('Enter 12 digit Aadhaar')
        return a

    def save(self):
        name = self.cleaned_data['name'].strip()
        phone = self.cleaned_data['phone']
        aadhaar = self.cleaned_data['aadhaar']
        address = self.cleaned_data['address']
        email = self.cleaned_data.get('email') 
        amount = self.cleaned_data['amount']
        diwali_year = self.cleaned_data['diwali_year']
        comment_choice=self.cleaned_data['comment_choice'],
        form_filler_name=self.cleaned_data.get('form_filler_name', '')
        quantity = self.cleaned_data['quantity']
        

    # Derive devotee (dedupe by aadhaar hash or phone if needed)
        aadhaar_hash = hashlib.sha256(aadhaar.encode()).hexdigest()
        devotee, _ = Devotee.objects.get_or_create(
            aadhaar_hash=aadhaar_hash,
            defaults={
                'name': name,
                'phone': phone,
                'aadhaar_last4': aadhaar[-4:],
                'address': address,
                'email': email,
                
            }
        )

    # If exists, update basic fields
        devotee.name = name
        devotee.phone = phone
        devotee.aadhaar_last4 = aadhaar[-4:]
        if address:
            devotee.address = address
        if email:
            devotee.email = email
        devotee.save()

    # Generate token: RAT-<year>-XXXX
        from .utils import next_token
        token = next_token(diwali_year)

        deposit = Deposit.objects.create(
            devotee=devotee,
            amount=amount,
            token=token,
            diwali_year=diwali_year,
            comment_choice=comment_choice,       # ✅ NEW FIELD
            form_filler_name=form_filler_name,
            quantity=quantity,
        )
        return deposit
        
# class OTPForm(forms.Form):
#     phone = forms.CharField(max_length=10)
#     otp = forms.CharField(max_length=6, required=False)