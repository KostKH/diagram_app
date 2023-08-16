import json
from collections import defaultdict

from django.db.models import F
from django.shortcuts import render

from .forms import get_city_form_class
from .models import PlanFact


def index(request):
    """Функция возвращает сгенерированную страницу index."""
    plan_fact_queryset = [item for item in
                          PlanFact.objects
                          .annotate(city_name=F('city__name'))
                          .values('city_name', 'year', 'plan', 'fact')]
    plan_fact = defaultdict(lambda: defaultdict(list))
    for item in plan_fact_queryset:
        plan_fact[item['city_name']]['year'].append(item['year'])
        plan_fact[item['city_name']]['plan'].append(item['plan'])
        plan_fact[item['city_name']]['fact'].append(item['fact'])

    cities = sorted(plan_fact.keys())
    city_form_class = get_city_form_class(cities)

    if request.method == 'POST':
        form = city_form_class(request.POST)
        if form.is_valid():
            cities = form.cleaned_data.get('cities')
    else:
        form = city_form_class()

    data = {
        'cities': cities or sorted(plan_fact.keys()),
        'plan_fact': json.dumps(plan_fact, ensure_ascii=False),
        'form': form,
    }
    return render(request, 'cities/index.html', data)
