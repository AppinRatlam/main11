# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('intake/', views.intake, name='intake'),
#     # path('intake/verify/', views.intake_verify, name='intake_verify'),
#     path('receipt/<str:token>/', views.receipt, name='receipt'),
#     path('search/', views.search, name='search'),
#     path('return/<str:token>/', views.mark_returned, name='mark_returned'),
#     path('report/', views.report, name='report'),
#     path('export.csv', views.export_csv, name='export_csv'),
#     path('otp/', views.otp, name='otp'),
#     path('otp-verify/', views.otp_verify, name='otp_verify'),
#     # path('return/send-otp/<int:deposit_id>/', views.return_send_otp, name='return_send_otp'),
#     path('return/verify-otp/<int:deposit_id>/', views.return_verify_otp, name='return_verify_otp'),

#     # path("deposit/send-otp/", views.deposit_send_otp, name="deposit_send_otp"),
#     # path("deposit/verify-otp/", views.deposit_verify_otp, name="deposit_verify_otp"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('intake/', views.intake, name='intake'),
    path('receipt/<str:token>/', views.receipt, name='receipt'),
    path('search/', views.search, name='search'),
    path('return/verify-otp/<int:deposit_id>/', views.return_verify_otp, name='return_verify_otp'),
    path('report/', views.report, name='report'),
    path('export.csv', views.export_csv, name='export_csv'),
    path('otp/', views.otp, name='otp'),
    path('otp-verify/', views.otp_verify, name='otp_verify'),
    path('return/<str:token>/', views.mark_returned, name='mark_returned'),
]
