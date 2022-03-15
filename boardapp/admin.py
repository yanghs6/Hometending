from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content', 'create_date', 'modify_date', 'author_id']
    list_display = ['subject', 'content', 'create_date', 'modify_date', 'author_id']
    list_filter = ['create_date', 'modify_date']

    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content', 'create_date', 'modify_date', 'author_id', 'post_id']
    list_display = ['content', 'create_date', 'modify_date', 'author_id', 'post_id']
    list_filter = ['create_date', 'modify_date']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content', 'create_date', 'modify_date', 'author_id', 'answer_id', 'post_id']
    list_display = ['content', 'create_date', 'modify_date', 'author_id', 'answer_id', 'post_id']
    list_filter = ['create_date', 'modify_date']

    
class CandidateAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'position', 'total_vote']
    list_display = ['full_name', 'position', 'total_vote']


class RegistrationAdmin(admin.ModelAdmin):
    search_fields = ['fname', 'lname', 'dob']
    list_display = ['fname', 'lname', 'dob']

    

admin.site.register(Post, PostAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(candidate, CandidateAdmin)
admin.site.register(Registration, RegistrationAdmin)
