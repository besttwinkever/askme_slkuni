from django.core.management.base import BaseCommand
from django.core.cache import cache
from askme_app.models import Profile, Tag

class Command(BaseCommand):
    help = 'Update cache'

    def handle(self, *args, **options):
        popularProfiles = Profile.objects.popular()
        cache.set('popularProfiles', popularProfiles, 62)
    
        popularTags = Tag.objects.popular()
        cache.set('popularTags', popularTags, 62)