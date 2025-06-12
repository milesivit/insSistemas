import csv

from django.contrib import admin

# Register your models here.
from home.models import FileUpload
from product.models import Product, Category
@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    actions= ['load_data_from_file']

    def load_data_from_file(self, request, queryset):
        for file_obj in queryset:
            if not file_obj.file.name.endswith('.csv'):
                self.message_user(
                    request,
                    "solo soporta csv",
                    level='error'
                )
                continue

            with open(file_obj.file.path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category, _ = Category.objects.get_or_create(
                        name=row['category']
                    )
                    Product.objects.create(
                        name=row['name'],
                        price=row['price'],
                        stock=row['stock'],
                        category=category,
                        description=row['description']
                    )
            self.message_user(
                request,
                "se uso esta categoria anteriormente",
                level='error'
            )
    load_data_from_file.short_description = "cargar productos"