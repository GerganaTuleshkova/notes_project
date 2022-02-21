from django.contrib import admin
from django.urls import path

from notes_project.notes_app.views import home, add_note, edit_note, delete_note, note_details, profile_details, \
    delete_profile

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete_note'),
    path('details/<int:pk>/', note_details, name='note_details'),
    path('profile/', profile_details, name='profile_details'),
    path('profile/delete/<int:pk>/', delete_profile, name='delete_profile'),
]
