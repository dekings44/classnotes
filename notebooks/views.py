from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.views import View
from .models import Notes
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class NotesView(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    model = Notes
    template_name = 'notebooks/notes.html'
    context_object_name = 'note'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        return context
        
 
@login_required(redirect_field_name='accounts:login')       
def allNotes(request):
    all_notes = Notes.objects.all()

    context = {'all_notes': all_notes}
    return render(request, 'notebooks/all_notes.html', context)
        
        
class NotesDetailView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'accounts:login'
    model = Notes
    template_name = 'notebooks/note-detail.html'
    context_object_name = 'note'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context
        
        
class CreateNotesView(LoginRequiredMixin, CreateView): 
    redirect_field_name = 'accounts:login'
    # specify the model for create view 
    model = Notes 
    form_class = NoteForm
    template_name = 'notebooks/create-note.html'
        
class UpdateNotesView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'accounts:login'
    model = Notes
    template_name = 'notebooks/update-note.html'
    form_class = NoteForm
    context_object_name = 'note'
        
        
class DeleteNotesView(LoginRequiredMixin, DeleteView):
    redirect_field_name = 'accounts:login'
    model = Notes
    template_name = 'notebooks/confirm-delete.html'
    context_object_name = 'note'

    success_url ="/"
    
    
    
# Creating a live and dislike view
    
# class AddLike(LoginRequiredMixin, CreateView):
#     def note(self, request, pk, *args, **kwargs):
#         note = Notes.objects.get(pk=pk)
        
#         is_dislike = False
        
#         for dislike in note.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
            
#         if is_dislike:
#             note.dislikes.remove(request.user)
        
#         is_like = False
        
#         for like in note.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
            
#         if not is_like:
#             note.likes.add(request.user)
            
#         if is_like:
#             note.likes.remove(request.user)
            
#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)
            
            
# class DisLike(LoginRequiredMixin, CreateView):
#     def note(self, request, pk, *args, **kwargs):
#         note = Notes.objects.get(pk=pk)
        
#         is_like = False
        
#         for like in note.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
            
#         if is_like:
#             note.likes.remove(request.user)
        
#         is_dislike = False
        
#         for dislike in note.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
            
#         if not is_dislike:
#             note.dislikes.add(request.user)
            
#         if is_dislike:
#             note.dislikes.remove(request.user)
            
#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)