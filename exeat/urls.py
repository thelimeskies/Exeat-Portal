"""exeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView
from django.urls import path
from django.views.generic import TemplateView

from portal import views
from portal.views import HomeExeatView, DayExeatView, BankExeatView, StatusView, AdHomeExeatView, AdDayExeatView, \
    AdAllExeatView, StudentDashboard, AdminDashboard, AdChooseExeat, TmDashboard, TmChooseExeat, TmBankExeatView, \
    TmDayExeatView, TmAllExeatView, TmHomeExeatView, approve_exeat, DepartingList, ReturningList, ScDashboard, \
    StudentSelect, AdExtensionView, ExtendView, AdDefaultersView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Login Control
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login_success/', views.login_success, name='login_success'),
    path('reset_password/', PasswordResetView.as_view(template_name="reset_password.html"), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete'),
    path('change_password/', PasswordChangeView.as_view(template_name="change_password.html"), name="change_password"),

    # Student/ URLs
    path('Student/', StudentDashboard.as_view(), name='student'),
    path('Student/choose_exeat', StudentSelect.as_view(), name='student_select'),
    path('Student/home_exeat/', HomeExeatView.as_view(), name='home_exeat'),
    path('Student/bank_exeat/', BankExeatView.as_view(), name='bank_exeat'),
    path('Student/day_exeat/', DayExeatView.as_view(), name='day_exeat'),
    path('Student/status/', StatusView.as_view(), name='status'),
    path('Student/extend/', ExtendView.as_view(), name='extend'),

    # Admin URLs
    path('Admin/', AdminDashboard.as_view(), name='admin'),
    path('Admin/choose_exeat', AdChooseExeat.as_view(), name='choose_exeat'),
    path('Admin/home_exeat/', AdHomeExeatView.as_view(), name='admin_home_exeat'),
    path('Admin/day_exeat/', AdDayExeatView.as_view(), name='admin_day_exeat'),
    path('Admin/all_exeat/', AdAllExeatView.as_view(), name='admin_all_exeat'),
    path('Admin/extension/', AdExtensionView.as_view(), name='ad_extension'),
    path('Admin/defaulters/', AdDefaultersView.as_view(), name='ad_defaulters'),

    # ExeatTeam URLs
    path('Team/', TmDashboard.as_view(), name='exeat_team'),
    path('Team/choose_exeat', TmChooseExeat.as_view(), name='exeat_choose_exeat'),
    path('Team/home_exeat/', TmHomeExeatView.as_view(), name='exeat_home_exeat'),
    path('Team/bank_exeat/', TmBankExeatView.as_view(), name='exeat_bank_exeat'),
    path('Team/day_exeat/', TmDayExeatView.as_view(), name='exeat_day_exeat'),
    path('Team/all_exeat/', TmAllExeatView.as_view(), name='exeat_all_exeat'),

    # SecurityUrls
    path('Security/depart', DepartingList.as_view(), name='departing_list'),
    path('Security/return', ReturningList.as_view(), name='returning_list'),
    path('Security/dashboard', ScDashboard.as_view(), name='security'),

    # Functions
    path('ajax/approve/', approve_exeat, name='approve'),
    path('ajax/accept/', views.accept_exeat, name='accept'),
    path('ajax/extend/', views.extend_exeat, name='extend_btn'),
    path('ajax/clock_in', views.clock_in, name='clock_in'),
    path('ajax/clock_out', views.clock_out, name='clock_out'),
    path('ajax/disapprove', views.disapprove, name='disapprove'),

    # Debugging
    path('testing/', views.temp, name='testing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'portal.views.error_404'
