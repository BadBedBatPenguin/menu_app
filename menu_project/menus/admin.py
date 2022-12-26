from django.contrib import admin

from .models import Node

class NodeInline(admin.StackedInline):
    model = Node
    extra = 1


class NodeAdmin(admin.ModelAdmin):
    list_display = ('text', 'level')


admin.site.register(Node, NodeAdmin)
