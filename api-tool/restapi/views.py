from django.shortcuts import render
from django.http import HttpResponse

import requests

def index(request):
    template_name = "index.html"

    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["results"][0]
        keys = list()
        values = list()
        for k,b in data.items():
            try:
                for l,n in b.items():
                    print("l", l)
                    print("n", n)
                    keys.append(l)
                    values.append(n)
            except:
                print("k", k)
                print("b", b)
                keys.append(k)
                values.append(b)

    else:
        data = None

    context = {'keys':keys, 'values':values}

    return render(request, template_name, context)
