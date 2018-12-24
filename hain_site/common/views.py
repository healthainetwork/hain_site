from django.shortcuts import render
from itertools import chain
from .models import *
from django_tables2 import RequestConfig
from .tables  import SeminarTable

import collections

def makehash():
    return collections.defaultdict(makehash)

def index_view(request):
    team_members = AboutMembers.objects.exclude(team_role = "Advisor")

    founders = team_members.filter(team_role = 'Founder & Co-President').values()
    department_members = team_members.exclude(team_department__isnull=True).exclude(team_department__exact='').order_by('team_department').values()
    other_members = team_members.filter(team_department__exact='').exclude(team_role = 'Founder & Co-President').order_by('team_role').values()
    member_list = list(chain(founders, department_members, other_members))

    advisors = AboutMembers.objects.filter(team_role = "Advisor").values()

    context = {
    'member_list': member_list,
    'advisors': advisors, }

    return render(request, 'pages/index.html', context)

def updates_view(request, type_of_update, page_number = 1):
    update_categories = {'clinical': 'C', 'business_funding': 'B', 'technology': 'T'}

    updates = Updates.objects.filter(type_of_update=update_categories[type_of_update]).order_by('-publication_date')

    context = {'updates': updates, 'category': type_of_update, }

    return render(request, 'pages/updates.html', context)

def careers_view(request):

    careers = Career.objects.all()
    company_list = careers.order_by('company').values('company').distinct()
    companies = list(Company.objects.filter(id__in = company_list).values())

    for company_obj in companies:
        career_objs = list(Career.objects.filter(company = company_obj["id"]).values())
        company_obj["careers"] = career_objs

    context = {'companies': companies}

    return render(request, 'pages/careers.html', context)

def seminars_view(request):

    seminars = Seminar.objects.all()
    table = SeminarTable(seminars)
    RequestConfig(request).configure(table)
    context = {'table': table}

    return render(request, 'pages/seminars-upenn.html', context)

