from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # essa tupla indica como deve ser ordanado as informações
    ordering = '-id', # essa é a ordenação por id so q começando de do maior para o menor    
    search_fields = 'id', 'first_name', 'last_name', # aponta uma busca por esses campos
    list_editable = 'first_name', 'last_name', # habilita editar ao entrar no admin de contact
    list_display_links = 'id', 'phone', # habilita links onde podemos clicar para abrir mais informações do usuario
    list_per_page = 10 # habilitado 10 usuarios por pagina
    list_max_show_all = 200 # habilita ate 200 usuarios por pagina


    
