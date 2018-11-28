from django.shortcuts import render
from itertools import chain
from .models import *


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
