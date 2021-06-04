import datetime
from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView
from django.db.models import F

from .decorators import student_required, security_required, exeat_team_required, admin_required
from .forms import ExeatForm, ExtensionForm
from .models import Exeat, Security, ExeatExtension


@login_required
def login_success(request):
    if request.user.is_student:
        return redirect("student")
    elif request.user.is_admin:
        return redirect("admin")
    elif request.user.is_security:
        return redirect("security")
    elif request.user.is_exeat_team:
        return redirect("exeat_team")


# Student Views
@method_decorator([login_required, student_required], name='dispatch')
class StudentDashboard(TemplateView):
    template_name = 'student/index.html'


@method_decorator([login_required, student_required], name='dispatch')
class StudentSelect(TemplateView):
    template_name = 'student/choose_exeat.html'


"""def student_dashboard(request, *args, **kwargs):
    return render(request, 'student/index.html')"""


@method_decorator([login_required, student_required], name='dispatch')
class HomeExeatView(CreateView):
    form_class = ExeatForm
    template_name = 'student/home_exeat.html'
    success_url = '/Student/status/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(HomeExeatView, self).form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class DayExeatView(CreateView):
    form_class = ExeatForm
    template_name = 'student/day_exeat.html'
    success_url = '/Student/status/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(DayExeatView, self).form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class BankExeatView(CreateView):
    form_class = ExeatForm
    template_name = 'student/bank_exeat.html'
    success_url = '/Student/status'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(BankExeatView, self).form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class ExtendView(CreateView):
    form_class = ExtensionForm
    template_name = 'student/extend.html'
    success_url = '/Student/status'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ExtendView, self).form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class StatusView(ListView):
    model = Exeat
    template_name = 'student/status.html'
    ordering = ['-date_created']

    def get_queryset(self):
        return self.model.objects.filter(user__username=self.request.user)


# Admin Views
@method_decorator([login_required, admin_required], name='dispatch')
class AdminDashboard(TemplateView):
    template_name = 'portal_admin/admin_portal.html'


"""def admin_dashboard(request, *args, **kwargs):
    return render(request, 'portal_admin/admin_portal.html')"""


@method_decorator([login_required, admin_required], name='dispatch')
class AdChooseExeat(TemplateView):
    template_name = 'portal_admin/admin_choose_exeat.html'


"""def admin_choose_exeat(request, *args, **kwargs):
    return render(request, 'portal_admin/admin_choose_exeat.html')"""


@method_decorator([login_required, admin_required], name='dispatch')
class AdHomeExeatView(ListView):
    model = Exeat
    template_name = 'portal_admin/admin_home_exeat.html'

    def get_queryset(self):
        return self.model.objects.filter(status="P", exeat_type="HE")


@method_decorator([login_required, admin_required], name='dispatch')
class AdExtensionView(ListView):
    model = ExeatExtension
    template_name = 'portal_admin/admin_exeat_extension.html'

    def get_queryset(self):
        return self.model.objects.filter(approval="P")


@method_decorator([login_required, admin_required], name='dispatch')
class AdDayExeatView(ListView):
    model = Exeat
    template_name = 'portal_admin/admin_day_exeat.html'

    def get_queryset(self):
        return self.model.objects.filter(status="P", exeat_type="DE")


@method_decorator([login_required, admin_required], name='dispatch')
class AdAllExeatView(ListView):
    model = Exeat
    template_name = 'portal_admin/admin_all_exeats.html'

    def get_queryset(self):
        return self.model.objects.all()


@method_decorator([login_required, admin_required], name='dispatch')
class AdDefaultersView(ListView):
    model = Exeat
    template_name = 'portal_admin/admin_defaulters.html'

    def get_queryset(self):
        return self.model.objects.filter(security__clocked_in__gt=F('return_date'))


@login_required
@admin_required
def approve_exeat(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = Exeat.objects.get(id=i)
        p.status = "AE"
        p.save()
        data = {'i': p.status}
    return JsonResponse(data)


@login_required
@admin_required
def extend_exeat(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = ExeatExtension.objects.get(id=i)
        p.approval = "AC"
        p.save()
        data = {'i': p.approval}
    return JsonResponse(data)


# exeat_team Views
@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmDashboard(TemplateView):
    template_name = 'exeat_team/team_portal.html'


"""def exeat_team_dashboard(request, *args, **kwargs):
    return render(request, 'exeat_team/team_portal.html')"""


@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmChooseExeat(TemplateView):
    template_name = 'exeat_team/team_choose_exeat.html'


"""def exeat_team_choose_exeat(request, *args, **kwargs):
    return render(request, 'exeat_team/team_choose_exeat.html')"""


@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmHomeExeatView(ListView):
    model = Exeat
    template_name = 'exeat_team/team_home_exeat.html'

    def get_queryset(self):
        return self.model.objects.filter(status="AE", exeat_type="HE")


@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmBankExeatView(ListView):
    model = Exeat
    template_name = 'exeat_team/team_bank_exeat.html'

    def get_queryset(self):
        return self.model.objects.filter(status="P", exeat_type="BE")


@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmDayExeatView(ListView):
    model = Exeat
    template_name = 'exeat_team/team_day_exeat.html'

    def get_queryset(self):
        return self.model.objects.filter(status="AE", exeat_type="DE")


@method_decorator([login_required, exeat_team_required], name='dispatch')
class TmAllExeatView(ListView):
    model = Exeat
    template_name = 'exeat_team/team_all_exeats.html'

    def get_queryset(self):
        return self.model.objects.all()


@login_required
@exeat_team_required
def accept_exeat(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = Exeat.objects.get(id=i)
        p.status = "A"
        p.save()
        data = {'i': p.status}
    return JsonResponse(data)


# Security
@method_decorator([login_required, security_required], name='dispatch')
class ScDashboard(TemplateView):
    template_name = 'security/security_portal.html'


@method_decorator([login_required, security_required], name='dispatch')
class DepartingList(ListView):
    model = Security
    template_name = 'security/departing_list.html'

    def get_queryset(self):
        return self.model.objects.filter(exeat__leave_date__lte=date.today(), exeat__status="A",
                                         clocked_out__isnull=True)


@method_decorator([login_required, security_required], name='dispatch')
class ReturningList(ListView):
    model = Security
    template_name = 'security/returning_list.html'

    def get_queryset(self):
        return self.model.objects.filter(exeat__status="A", clocked_in__isnull=True,
                                         clocked_out__isnull=False)


@method_decorator([login_required, security_required], name='dispatch')
class AllList(ListView):
    model = Security
    template_name = 'security/returning_list.html'

    def get_queryset(self):
        return self.model.objects.filter(exeat__status="A")


def clock_in(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = Security.objects.get(exeat_id=i)
        p.clocked_in = datetime.datetime.now()
        p.save()
        data = {'i': p.clocked_in}
    return JsonResponse(data)


def clock_out(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = Security.objects.get(exeat_id=i)
        p.clocked_out = datetime.datetime.now()
        p.save()
        data = {'i': p.clocked_in}
    return JsonResponse(data)


def disapprove(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        j = request.GET.get('j', None)
        p = Exeat.objects.get(id=i)
        p.status = "D"
        p.disapproval_reason = j
        p.save()
        data = {'i': p.status}
    return JsonResponse(data)


def temp(request):
    return render(request, 'portal_admin/admin_portal.html')


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)
