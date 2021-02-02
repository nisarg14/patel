from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    response = requests.get('https://graph.instagram.com/me/media?fields=id,media_type,media_url,username,timestamp,caption&access_token=IGQVJXUF92Ynk0bHJXU28zV0FSUnVGMzAtaDJuemJYZA0FTSWw3czlsVWlreWxTcUdrVXJBMDVTbmJESTdDcmluX0pUYzE3bVVlanVuXzB0V3FaZAGg3SWVBMWlYM3JMRUtrMjlUT3lDZAGU3dVkxcThacAZDZD')
    data = response.json()
    return render(request,'home.html',{"data" : data['data']})