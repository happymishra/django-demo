from django.http import JsonResponse
from django.shortcuts import render

from .models import PlayerInfo, Team


def insert_player_details(request):
    try:
        name = request.POST['name']
        team_name = request.POST['teamName']
        runs = request.POST['runs']
        wickets = request.POST['wickets']
        rank = request.POST['rank']

        team = Team.objects.get(country=team_name)

        player_obj = PlayerInfo(name=name, team_id=team, runs=runs,
                                wickets=wickets, ranks=rank)

        player_obj.save()

        resp = JsonResponse({'message': "Insertion successful"}, status=200)

    except Exception as ex:
        resp = JsonResponse({'message': str(ex)}, status=500)

    return resp


def get_players(request):
    country = request.GET.get('country', None)

    try:
        if country:
            player_objs = PlayerInfo.objects.filter(team_id__country=country)
        else:
            player_objs = PlayerInfo.objects.select_related('team_id')

        # players_list = get_json_data(player_objs)
        players_list = get_tabular_data(player_objs)

        resp = JsonResponse({
            'data': players_list
        }, status=200)

    except Exception as ex:
        resp = JsonResponse({'message': str(ex)}, status=500)

    return resp


def get_json_data(player_objs):
    players_list = list()

    for each_player in player_objs:
        players_list.append({
            'name': each_player.name,
            'country': each_player.team_id.country,
            'runs': each_player.runs,
            'wickets': each_player.wickets,
            'ranks': each_player.ranks
        })

    return players_list


def get_tabular_data(player_objs):
    columns = ['Name', 'Country', 'Runs', 'Wicket', 'Rank']

    table_list = list()
    table_list.append(columns)

    for each_player in player_objs:
        table_list.append([each_player.name, each_player.team_id.country,
                           each_player.runs, each_player.wickets,
                           each_player.ranks])

    return table_list


def players_page(request):
    return render(request, 'players.html')


def add_player_page(request):
    return render(request, 'addplayers.html')
