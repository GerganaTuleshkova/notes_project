from django import forms

from notes_project.notes_app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']

        labels = {
            'image_url': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']

        labels = {
            'image_url': 'Link to Image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']

        labels = {
            'image_url': 'Link to Image',
        }
