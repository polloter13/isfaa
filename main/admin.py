from django.contrib import admin
from .models import Tool, Watering, Watering_tool, Message, Gübre, Plants, Plant, Texnika, Model

admin.site.register(Message)
admin.site.register(Plant)
admin.site.register(Plants)
admin.site.register(Texnika)
admin.site.register(Model)
admin.site.register(Tool)
admin.site.register(Gübre)
admin.site.register(Watering)
admin.site.register(Watering_tool)
