from dpasteapp.models import *
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from dpasteapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class HomeRedirectView(View):
    def get(self):
        return redirect('dpastelists')


class dPasteListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = dPasteList
    template_name = 'dpaste_list.html'

    def get_context_data(self, **kwargs):
        context = super(dPasteListView, self).get_context_data(**kwargs)
        dpastelists = dPasteList.objects.filter(user = self.request.user)
        context.update({
            'title' : 'dPaste Projects',
            'dpastelists' : list(
                map(lambda x: {'list' : x, 'count' : len(x.dpastelistitem_set.all())}, dpastelists)
            ),
        })
        return context


# class dPasteListCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class dPasteListCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = dPasteList
    form_class = dPasteListForm
    # permission_required = ('dpastelistapp.add_dpastelist')
    template_name = 'add_dpastelist.html'

    def get_context_data(self, **kwargs):
        context = super(dPasteListCreateView,self).get_context_data(**kwargs)
        context.update({
            'title' : 'Add dPaste Project'
        })
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        dPaste_form = dPasteListForm(request.POST)

        if dPaste_form.is_valid():
            dPaste = dPaste_form.save(False)
            dPaste.user = user
            dPaste.save()

        return redirect("dpastelists")


# class dPasteListDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class dPasteListDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = dPasteList
    context_object_name = 'dpastelist'
    template_name = 'dpastelist_details.html'
    permission_denied_message = "You don't have permissions to access the requested dPaste:("

    def has_permission(self):
        pk = self.kwargs.get('pk')
        dPaste = self.request.user.dpastelist_set.filter(pk = pk)
        if dPaste:
            return True
        else:
            self.raise_exception = True
            return False

    def handle_no_permission(self):
        messages.error(self.request,self.permission_denied_message)
        return super(dPasteListDetailView, self).handle_no_permission()

    def get_object(self, queryset=None):
        obj = get_object_or_404(dPasteList, **self.kwargs)
        return obj

    def get_context_data(self, **kwargs):
        context = super(dPasteListDetailView, self).get_context_data(**kwargs)
        context.update({
            'title' : 'List details'
        })
        return context


# class dPasteListUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class dPasteListUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = dPasteList
    form_class = dPasteListForm
    template_name = 'add_dpastelist.html'
    # permission_required = ('dpasteapp.edit_dpastelist')
    success_url = reverse_lazy('dpastelists')

    def has_permission(self):
        pk = self.kwargs.get('pk')
        dPaste = get_object_or_404(dPasteList, pk = pk)
        if dPaste:
            return dPaste.user == self.request.user
        else:
            self.raise_exception = True
            return

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super(dPasteListUpdateView, self).handle_no_permission()

    def get_context_data(self, **kwargs):
        context = super(dPasteListUpdateView, self).get_context_data(**kwargs)
        context.update({
            'edit' : True,
        })
        return context


# class dPasteListDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class dPasteListDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = dPasteList
    template_name = 'confirm_delete.html'
    # permission_required = ('manageapp.delete_dpastelist')
    success_url = reverse_lazy('dpastelists')

    def has_permission(self):
        pk = self.kwargs.get('pk')
        dpastelist = get_object_or_404(dPasteList, pk = pk)
        if dpastelist:
            return dpastelist.user == self.request.user
        else:
            self.raise_exception = True
            return

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super(dPasteListDeleteView, self).handle_no_permission()

