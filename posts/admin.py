from django.contrib import admin
from posts.models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status',]
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class PostImageInline(admin.TabularInline):
    model = Images
    extra = 4

class PostAdmin(admin.ModelAdmin):
    list_display= ['id', 'title1', 'category', 'trending_songs','slide1', 'slide2','slide3','frontpage']
    list_filter= ['category']
    list_display_links = ['title1', 'category']
    inlines = [PostImageInline]
    prepopulated_fields = {'slug': ('title1',)}
    list_editable=['trending_songs','slide1', 'slide2','slide3','frontpage']


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Images)
admin.site.register(Moderator)
admin.site.register(Comment)
