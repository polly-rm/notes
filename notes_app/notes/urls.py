from django.urls import path

from notes_app.notes.views import home_page, add_note, edit_note, delete_note, show_note_details, show_profile_page, \
    create_profile, delete_profile

urlpatterns = [
    # profile urls
    path('', home_page, name='home page'),
    path('create/', create_profile, name='create profile'),
    path('profile/', show_profile_page, name='profile page'),
    path('profile/delete/', delete_profile, name='delete profile'),
    # notes urls
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', show_note_details, name='note details'),
]
