import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config import settings
from main.forms import MailingForm, ClientForm, LetterForm, MailingFormForManager
from main.models import Client, Mailing, Letter

"""CRUD Клиентов"""


class ClientListView(ListView):
    model = Client
    template_name = 'main/client/client_list.html'
    # permission_required = 'main.view_client'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'main/client/client_info.html'
    # permission_required = 'main.view_client'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    # permission_required = 'catalog.add_product'
    success_url = reverse_lazy('main:client_list')
    template_name = 'main/client/client_form.html'

    def form_valid(self, client):
        if client.is_valid():
            new_obj = client.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(client)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    # permission_required = 'catalog.change_product'
    success_url = reverse_lazy('main:client_list')
    template_name = 'main/client/client_form.html'

    def get_success_url(self):
        return reverse('main:client_info', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    # permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('main:client_list')
    template_name = 'main/client/client_confirm_delete.html'


"""CRUD Рассылки"""


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'main/mailing/mailing_list.html'
    # permission_required = 'catalog.view_product'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'main/mailing/mailing_info.html'


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    # permission_required = 'catalog.add_product'
    success_url = reverse_lazy('main:mailing_list')
    template_name = 'main/mailing/mailing_form.html'

    def form_valid(self, mailing):
        if mailing.is_valid():
            new_obj = mailing.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(mailing)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    # permission_required = 'catalog.change_product'
    success_url = reverse_lazy('main:mailing_list')
    template_name = 'main/mailing/mailing_form.html'

    def get_success_url(self):
        return reverse('main:mailing_info', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author or user.is_superuser:
            # print(user, self.object.name)
            return MailingForm
        elif user.groups.filter(name='manager').exists():
            return MailingFormForManager
        else:
            # print(user.email, self.object.author)
            raise PermissionDenied()


class MailingDeleteView(DeleteView):
    model = Mailing
    # permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('main:mailing_list')
    template_name = 'main/mailing/mailing_confirm_delete.html'


"""CRUD Письма"""


class LetterListView(ListView):
    model = Letter
    template_name = 'main/letter/letter_list.html'
    # permission_required = 'catalog.view_product'


class LetterDetailView(DetailView):
    model = Letter
    template_name = 'main/letter/letter_info.html'


class LetterCreateView(CreateView):
    model = Letter
    form_class = LetterForm
    # permission_required = 'catalog.add_product'
    success_url = reverse_lazy('main:letter_list')
    template_name = 'main/letter/letter_form.html'

    def form_valid(self, letter):
        if letter.is_valid():
            new_obj = letter.save()
            new_obj.author = self.request.user
            new_obj.save()

        return super().form_valid(letter)


class LetterUpdateView(UpdateView):
    model = Letter
    form_class = LetterForm
    # permission_required = 'catalog.change_product'
    success_url = reverse_lazy('main:letter_list')
    template_name = 'main/letter/letter_form.html'

    def get_success_url(self):
        return reverse('main:letter_info', args=[self.kwargs.get('pk')])


class LetterDeleteView(DeleteView):
    model = Letter
    # permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('main:letter_list')
    template_name = 'main/letter/letter_confirm_delete.html'