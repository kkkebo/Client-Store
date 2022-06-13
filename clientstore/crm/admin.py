from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm
# Register your models here.


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('com_date', 'com_text')
    readonly_fields = ('com_date',)
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'name', 'email', 'order_phone', 'order_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'order_phone', 'email', 'order_date')
    list_filter = ('order_date', 'order_phone')
    list_editable = ('order_status',)
    list_per_page = 20
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_date', 'name', 'email', 'order_phone',)
    readonly_fields = ('id', 'order_date')
    #добавляем класс комент
    inlines = (Comment, )
    empty_value_display = "-пусто-"


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)