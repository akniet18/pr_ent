from django.contrib import admin
from .models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class VariantInline(admin.TabularInline):
    model = question_variant

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'subject')
    list_filter = ('subject', )
    inlines = [VariantInline]

class Variant(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_right', 'question')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(question_variant, Variant)
admin.site.register(TestPhoto)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FeedBack)
