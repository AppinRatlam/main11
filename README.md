# Mahalakshmi Temple Deposit App (Django)

A simple, secure-by-default Django app to manage the Diwali deposit ritual at Mahalakshmi Temple, Ratlam (M.P.).
- Register deposit with devotee details
- Auto-generate unique token (e.g., `RAT-2025-0001`)
- Print a receipt
- Search by token/name/phone
- Mark as returned after Diwali Puja
- Reports + CSV export
- Stores only Aadhaar last 4 + SHA256 hash (no full Aadhaar in DB)

## Quick Start

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Notes on Privacy
- We store `aadhaar_last4` and `aadhaar_hash` (SHA256) only.
- Receipt shows last 4 digits only.
- Avoid sharing database backups publicly.
- For production: set `DEBUG=False`, set a strong `SECRET_KEY`, use Postgres, HTTPS, and staff-only access.

## Future Enhancements
- SMS/WhatsApp token (using a gateway)
- PDF receipts (WeasyPrint/xhtml2pdf)
- Multi-branch support (prefix by branch)
- QR on receipt linking to token page
