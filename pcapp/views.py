from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login,  authenticate, logout
from . models import Record, Criminal, Staff, Crime
from django.views.generic import DetailView, CreateView, UpdateView, ListView

# Create your views here.


class CrimeListView(ListView):
    model = Crime
    template_name = 'pcapp/index.html'
    context_object_name = 'cases'


class CaseDetailView(DetailView):
    model = Record


class CaseCreateView(CreateView):
    model = Record
    template_name = 'pcapp/inputcrime.html'
    fields = ['OB_no', 'first_name', 'last_name', 'ID_no', 'contacts', 'area_of_stay', 'nationality', 'age', 'gender']


class CrimeUpdateView(UpdateView):
    model = Crime
    fields = ['status', 'investigating_officer']


def criminals(request):
    crimes = Criminal.objects.all()
    return render(request, 'pcapp/criminal_list.html', {'crimes': crimes})


def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'pcapp/staffs.html', {'staffs': staffs})


class CriminalUpdateView(UpdateView):
    model = Criminal
    fields = ['offences']


class StaffUpdateView(UpdateView):
    model = Staff
    fields = ['position', 'department']


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['contacts', 'area_of_stay']


class CrimeCreateView(CreateView):
    model = Crime
    fields = ['record', 'nature_of_crime', 'description_of_crime', 'status', 'investigating_officer', 'section_of_CPC_offence']


class RecordListView(ListView):
    model = Record
    template_name = 'pcapp/record_detail.html'
    context_object_name = 'records'


#class CrimeUpdateView(UpdateView):
   # model = Crime
    #fields = ['status']


class CriminalCreateView(CreateView):
    model = Criminal
    template_name = 'pcapp/addcriminal.html'
    fields = ['picture', 'first_name', 'last_name', 'ID_no', 'nationality', 'offences']

    def form_valid(self, form, **kwargs):
        crime = get_object_or_404(Crime, pk=self.kwargs.get('pk'))
        form.instance.crime = crime
        form.instance.picture = self.request.FILES['picture']
        #form.instance.post = self.request.post
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('pcapp:index')







