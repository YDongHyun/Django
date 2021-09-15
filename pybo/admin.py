from django.contrib import admin
from.models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']   #제목검색

admin.site.register(Question,QuestionAdmin)    #어드민의 권한을 주는것
# Register your models here.
