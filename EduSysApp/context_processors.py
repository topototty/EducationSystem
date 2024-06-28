from django.contrib.auth.models import Group

def user_groups(request):
    if request.user.is_authenticated:
        groups = request.user.groups.values_list('name', flat=True)
        return {'user_groups': list(groups)}
    return {'user_groups': []}
