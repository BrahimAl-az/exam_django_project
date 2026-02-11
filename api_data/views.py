import requests
from django.shortcuts import render

def api_view(request):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=chicken'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        meals = data.get('meals', [])
        if meals:
            for meal in meals:
                if meal.get('strTags'):
                    meal['strTags_list'] = meal['strTags'].split(',')
                else:
                    meal['strTags_list'] = []
    except requests.RequestException:
        meals = []
        return render(request, 'api_data/list.html', {'error': 'Failed to fetch recipes from the kitchen.'})

    return render(request, 'api_data/list.html', {'meals': meals})
