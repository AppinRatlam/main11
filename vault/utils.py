# from .models import Deposit
# from django.db.models import Max
# from twilio.rest import Client
# from django.conf import settings
# import random


# def next_token(year: int) -> str:
#     prefix = f"RAT-{year}-"
#     last = Deposit.objects.filter(diwali_year=year, token__startswith=prefix).aggregate(Max('token'))['token__max']
#     if last:
#         try:
#             seq = int(last.split('-')[-1])
#         except Exception:
#             seq = 0
#     else:
#         seq = 0
#     seq += 1
#     return f"{prefix}{seq:04d}"

# # vault/utils.py


# try:
#     from twilio.rest import Client
#     TWILIO_AVAILABLE = True
# except Exception:
#     TWILIO_AVAILABLE = False

# from twilio.rest import Client
# from django.conf import settings

# import requests
# from django.conf import settings


# def generate_otp():
#     return "{:06d}".format(random.randint(0, 999999))

# def send_otp_whatsapp(phone, otp):
#     """
#     Send OTP via Fast2SMS WhatsApp API
#     """
#     url = "https://www.fast2sms.com/dev/bulkV2"  # Replace with Fast2SMS WhatsApp endpoint
#     payload = {
#         "route": "whatsapp",
#         "numbers": phone,  # in format 91XXXXXXXXXX
#         "message": f"Your OTP is {otp}",
#         "language": "english",
#         "flash": 0
#     }
#     headers = {
#         "authorization": settings.FAST2SMS_API_KEY,
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     result = response.json()
#     if result.get("return") == True:
#         return True
#     else:
#         print(f"[ERROR] Failed to send OTP: {result}")
#         return False
        
# def store_otp(request, phone, otp):
#     request.session[f"otp_{phone}"] = otp

# def verify_otp(request, phone, otp):
#     stored_otp = request.session.get(f"otp_{phone}")
#     if stored_otp and stored_otp == otp:
#         # OTP correct, remove from session
#         del request.session[f"otp_{phone}"]
#         return True
#     return False



# # def send_otp_whatsapp(phone: str, request=None):
# #     """
# #     Send OTP via WhatsApp using Twilio.
# #     Fallback to session storage for local testing.
# #     """
# #     phone_e = f"+91{phone}" if not phone.startswith("+") else phone
# #     code = "{:06d}".format(random.randint(0, 999999))

# #     if TWILIO_AVAILABLE and getattr(settings, "TWILIO_ACCOUNT_SID", None) and getattr(settings, "TWILIO_AUTH_TOKEN", None):
# #         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
# #         twilio_whatsapp_number = getattr(settings, "TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886")
# #         message = client.messages.create(
# #             from_=twilio_whatsapp_number,
# #             to=f"whatsapp:{phone_e}",
# #             body=f"Your Temple Deposit OTP is {code}"
# #         )
# #         return True
# #     else:
# #         # fallback for testing
# #         if request is not None:
# #             request.session["pending_otp_code"] = code
# #         print(f"[DEBUG] WhatsApp OTP for {phone_e}: {code}")
# #         return code


# # def verify_otp_whatsapp(phone: str, code: str, request=None) -> bool:
# #     if request is None:
# #         return False
# #     expected = request.session.get("pending_otp_code")
# #     return expected is not None and expected == code


from .models import Deposit
from django.db.models import Max

# ---------- Token Generation ----------
def next_token(year: int) -> str:
    """
    Generate next sequential token for the given year.
    Format: RAT-YYYY-0001
    """
    prefix = f"RAT-{year}-"
    last = Deposit.objects.filter(diwali_year=year, token__startswith=prefix).aggregate(Max('token'))['token__max']
    
    if last:
        try:
            seq = int(last.split('-')[-1])
        except Exception:
            seq = 0
    else:
        seq = 0

    seq += 1
    return f"{prefix}{seq:04d}"
