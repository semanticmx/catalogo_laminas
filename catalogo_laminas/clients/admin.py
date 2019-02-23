from django.contrib import admin

from . import models as clients_models


admin.site.register(clients_models.OrderHistory)
admin.site.register(clients_models.Company)
admin.site.register(clients_models.Client)
