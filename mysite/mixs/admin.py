from django.contrib import admin

from .models import Customer, Operator, Item, Lot, ProductionPlan, Detail


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 3


class ProductionPlanAdmin(admin.ModelAdmin):
    inlines = [DetailInline]


admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Lot)
admin.site.register(ProductionPlan,ProductionPlanAdmin)
admin.site.register(Detail)
