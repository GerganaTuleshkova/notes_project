from django import template

from notes_project.notes_app.models import Profile, Note

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0


@register.simple_tag()
def get_profile():
    if has_profile:
        profile = Profile.objects.all()[0]
        return profile.first_name


@register.simple_tag()
def has_notes():
    return Note.objects.count() > 0
