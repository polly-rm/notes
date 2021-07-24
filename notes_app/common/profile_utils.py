from notes_app.notes.models import Profile, Note


def get_profile():
    profile = Profile.objects.first()
    all_notes_list = list(Note.objects.all())
    if profile:
        profile.total_notes = len(all_notes_list)
    return profile
