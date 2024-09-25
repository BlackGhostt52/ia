from django.contrib import admin
from contact import models
from contact.models import Contact

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name','last_name', 'phone', 'show',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id', 'phone',

    # c = Contact(first_name='Jose')
    # c.save()
    # c.last_name = 'Silva'
    # c.save()
    # c.delete()

    # c = Contact.objects.get(id=3)
    # c.first_name = 'Alexandre'
    # c.save()
    # c = Contact.objects.all()
    # for contato in c: contato.first_name
    # c = Contact.objects.filter(pk=3)
    # for contato in c: contato.first_name
    # c = Contact.objects.all().order_by('id')
    # c = Contact.objects.create(first_name='Joao', last_name='Oliveira')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',