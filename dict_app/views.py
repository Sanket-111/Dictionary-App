from django.shortcuts import render
import requests

# Free dict API
# "https://api.dictionaryapi.dev/api/v2/entries/en/<word>"

# Create your views here.
def home(request):
    if request.method == "POST":
        word = request.POST.get("word")
        resp = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        data = resp.json()
        p_link = ""

        try:
            if len(data[0]["phonetics"]) != 0:
                p_link = data[0]["phonetics"][0]["audio"]

                if len(p_link) == 0:
                    try:
                        p_link = data[0]["phonetics"][1]["audio"]
                    except IndexError:
                        pass
        except KeyError or IndexError:
            pass

        return render(request, "index.html", {'data':data, 'p_link':p_link})

    return render(request, "index.html")