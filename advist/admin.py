from django.contrib import admin
from .models import Advistments, Rubric
# Register your models here.
admin.site.register(Rubric)
@admin.register(Advistments)
class AdvistmentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'rubric')

