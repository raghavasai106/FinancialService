from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('customer/create/', views.customer_new, name='customer_new'),

    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),

    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    re_path(r'^customers_json/', views.CustomerList.as_view()),
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_email_sent.html"),
         name='reset_email_sent'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_confirm.html"),
         name='reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_complete.html"),
         name='reset_complete'),

    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_changed.html"),
         name='password_changed'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('customers_json/', views.CustomerList.as_view()),
    path('signup/', views.AdvisorSignUp, name='signup'),
    path('signup/signup_successful', views.signup_successful, name='signup_successful'),

    re_path(r'^mutualfund/$', views.mutualfund_list, name='mutualfund_list'),
    re_path(r'^mutualfund/(?P<pk>\d+)/delete/$', views.mutualfund_delete, name='mutualfund_delete'),
    re_path(r'^mutualfund/(?P<pk>\d+)/edit/$', views.mutualfund_edit, name='mutualfund_edit'),
    re_path(r'^mutualfund/create/$', views.mutualfund_new, name='mutualfund_new'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
