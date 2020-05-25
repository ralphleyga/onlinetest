from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import (
    Exam,
    Question,
    QuestionOption,
    Answer
    )


class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}?_to_field=id&_popup=1" onclick="return showAddAnotherPopup(this);">edit</a>'.format(u=url))
        else:
            return ''


class QuestionInline(EditLinkToInlineObject, admin.TabularInline):
    model = Question
    readonly_fields = ('edit_link', )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'created')
    search_fields = ('name', 'description')
    
    inlines = [
        QuestionInline,
    ]


class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'question')
    inlines = [
        QuestionOptionInline,
    ]


@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('order', 'question', 'option')