from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os , sys
from .models import CoinData

# Create your views here.

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            print("httt")
            data = json.loads(request.body)
            print("data ", data)
            CoinData.objects.all().delete()
            # Loop through the data and save it to the database
            for item in data:
                coin_data = CoinData(
                    name=item['name'],
                    price=item['price'],
                    one_hour_change=item['one_hour_change'],
                    twenty_four_hour_change=item['twenty_four_hour_change'],
                    seven_day_change=item['seven_day_change'],
                    market_cap=item['market_cap'],
                    volume_24h=item['volume_24h'],
                    circulating_supply=item['circulating_supply']
                )
                coin_data.save()

            return JsonResponse({'message': 'Data received and saved successfully.'}, status=200)
        except Exception as e:
            traceback = sys.exc_info()[2]
            line_no = str(traceback.tb_lineno)
            print("ERROR LINE NO----", line_no)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def get_latest_data(request):
    coin_data = CoinData.objects.all()  # Retrieve data from the database
    return render(request, 'coinmarketcap/coin_data_table.html', {'coin_data': coin_data})