from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = question_variant
        fields = '__all__'

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class VariantInline(admin.TabularInline):
    model = question_variant

class QuestionAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'text', 'subject')
    list_filter = ('subject', )
    inlines = [VariantInline]
    search_fields = ('text',)

class Variant(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'text', 'is_right', 'question')

class IMG(admin.ModelAdmin):
    list_display = ('id', 'question')
    search_fields = ('question',)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(question_variant, Variant)
admin.site.register(TestPhoto, IMG)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FeedBack)
