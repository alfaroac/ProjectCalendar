# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import CalendarEvent, Evidences
from .forms import EventForm, EvidenceForm
from serializers import event_serializer
from utils import timestamp_to_datetime

from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import datetime


class CalendarJsonListView(ListView):

    template_name = 'django_bootstrap_calendar/calendar_events.html'

    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date) + datetime.timedelta(-30),
                    timestamp_to_datetime(to_date)
                    )
            )
        elif from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )

        return event_serializer(queryset)


class CalendarView(TemplateView):

    template_name = 'django_bootstrap_calendar/calendar.html'


class CrearEvento(FormView):
    template_name = 'eventos/crear_evento.html'
    form_class = EventForm
    success_url = reverse_lazy('calendario_app:calendar')

    def form_valid(self, form):
        event = form.save()
        return super(CrearEvento, self).form_valid(form)
# evidences
def evidencias(request):
    obj_evid=Evidences.objects.all()
    cant=obj_evid.count()
    return render(request,'eventos/evidencias.html',{'evidences':obj_evid,'cantidad':cant})

def addEvidence(request):
    if request.method=='POST':
        modelform=EvidenceForm(request.POST,request.FILES)
        if modelform.is_valid():
            modelform.save()
            return redirect(reverse('calendario_app:evidence'))
    else:
        modelform=EvidenceForm()
    return render(request,'eventos/addEvidence.html',{'form':modelform})

def updEvidence (request, id):
    obj_update=Evidences.objects.get(pk=id)
    if request.method=='POST':
        modelform=EvidenceForm(request.POST, request.FILES, instance=obj_update)
        if modelform.is_valid():
            modelform.save()
            return redirect(reverse('calendario_app:evidence'))
    else:
        modelform=EvidenceForm(instance=obj_update)
    return render(request,'eventos/updEvidence.html', {'form':modelform},context_instance = RequestContext(request))

def delEvidence (request, id):
    obj_delete = Evidences.objects.get(pk=id)
    obj_delete.delete()
    return redirect(reverse('calendario_app:evidence'))