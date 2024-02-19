from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'

class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'output_order',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

# Регистрируем кастомное представление админ-зоны
admin.site.register(Topping)
admin.site.register(Wrapper) 