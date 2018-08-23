from dpasteapp.models import *
from  django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from dpasteapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class dPasteItemListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = dPasteListItem
    template_name = 'dpaste_list_items.html'

    def get_context_data(self, **kwargs):
        context = super(dPasteItemListView, self).get_context_data(**kwargs)
        dpastelistitems = dPasteListItem.objects.filter(**self.kwargs)
        context.update({
            'title' : 'dPaste Code Files',
            'dpastelistitems' : dpastelistitems,
            'dpastelist_id' : self.kwargs.get('dpastelist_id'),
        })
        return context


# class dPasteListItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class dPasteListItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = dPasteListItem
    form_class = dPasteListItemForm
    # permission_required = ('dpastelistapp.add_dpastelistitem')
    template_name = 'add_dpastelistitem.html'

    def get_context_data(self, **kwargs):
        context = super(dPasteListItemCreateView, self).get_context_data(**kwargs)
        context.update({
            'title' : 'Add Code repository'
        })
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        dpastelistitem_form = dPasteListItemForm(request.POST)
        dpastelist_id = self.kwargs.get('dpastelist_id')
        if dpastelistitem_form.is_valid():
            dpastelistitem = dpastelistitem_form.save(False)
            dpastelistitem.dpastelist = dPasteList.objects.get(id = dpastelist_id)
            dpastelistitem.save()

        return redirect("dpastelistitem_list", dpastelist_id = dpastelist_id)


# class dPasteListItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class dPasteListItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = dPasteListItem
    form_class = dPasteListItemForm
    template_name = 'add_dpastelistitem.html'
    # permission_required = ('dpasteapp.edit_dpastelistitem')

    def get_success_url(self, **kwargs):
        return redirect('dpastelistitem_list', dpastelist_id = self.kwargs.get('dpastelist_id')).url

    def has_permission(self):
        pk = self.kwargs.get('pk')
        dpastelistitem = get_object_or_404(dPasteListItem, pk = pk)
        if dpastelistitem:
            return dpastelistitem.dpastelist.user == self.request.user
        else:
            self.raise_exception = True
            return

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super(dPasteListItemUpdateView, self).handle_no_permission()

    def get_context_data(self, **kwargs):
        context = super(dPasteListItemUpdateView, self).get_context_data(**kwargs)
        context.update({
            'edit' : True,
        })
        return context


# class dPasteListItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class dPasteListItemDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = dPasteListItem
    template_name = 'confirm_delete.html'
    # permission_required = ('dpasteapp.delete_dpastelistitem')

    def get_success_url(self, **kwargs):
        return redirect('dpastelistitem_list', dpastelist_id = self.kwargs.get('dpastelist_id')).url

    def has_permission(self):
        pk = self.kwargs.get('pk')
        dpastelistitem = get_object_or_404(dPasteListItem, pk = pk)
        if dpastelistitem:
            return dpastelistitem.dpastelist.user == self.request.user
        else:
            self.raise_exception = True
            return

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super(dPasteListItemDeleteView, self).handle_no_permission()
