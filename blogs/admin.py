from django.contrib import admin

from .models import Post
# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     search_fields = ['title', 'author__username']
#     list_display = ('title', 'author', 'public', 'created','updated',\
#                  'published')
#     date_hierarchy = 'created'
#     list_filter = ['created', 'updated', 'public']
    
#     raw_id_fields = ['author']

#     fieldsets = (
#         ('Basic', {
#             'fields': ['author','title' ,'content']
#         }),

             
#         ('Status', {
#             'fields': ['public']
#         }),
#     )


admin.site.register(Post)

