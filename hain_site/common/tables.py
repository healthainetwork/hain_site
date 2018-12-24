import django_tables2 as tables
from .models import *

class SeminarTable(tables.Table):
    location = tables.TemplateColumn('{{ record.event_date |date:"F j, Y (D)" }}<p>{{ record.location | safe }}')
    description = tables.TemplateColumn('{{ record.description | safe }}')
    recap = tables.TemplateColumn('{{ record.recap | safe }}')
    class Meta:
        model = Seminar
        exclude = ('id', 'term', 'event_date', )
        template_name = 'django_tables2/bootstrap.html'
