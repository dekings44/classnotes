from django.urls import path
from .views import NotesView, NotesDetailView, UpdateNotesView, CreateNotesView, DeleteNotesView, allNotes

app_name = 'notebooks'

urlpatterns = [
    path('', NotesView.as_view(), name='notebooks'),
    path('all_notes/', allNotes, name='all_notes'),
    path('<slug:slug>/', NotesDetailView.as_view(), name='note-detail'),
    path('create', CreateNotesView.as_view(), name='create-note'),
    # path('<pk>/dislike', DisLike.as_view(), name='dislike'),
    # path('<pk>/like', AddLike.as_view(), name='like'),
    path('<int:pk>/update', UpdateNotesView.as_view(), name='update'),
    path('<pk>/delete', DeleteNotesView.as_view(), name='delete'),
   
]