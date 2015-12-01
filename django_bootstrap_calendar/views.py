# -*- coding: utf-8 -*-


from .models import CalendarEvent
from .forms import EventForm
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

