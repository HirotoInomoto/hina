from django.shortcuts import render
from .models import Log
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    year_list = []
    month_list = []
    day_list = []
    for i in range(1900, 2024):
        year_list.append(i)
    for i in range(1, 13):
        month_list.append(i)
    for i in range(1, 32):
        day_list.append(i)
    
    if request.method == "POST":
        try:
            start_date = datetime.strptime(f'{request.POST["start_year"]}-{request.POST["start_month"]}-{request.POST["start_day"]}', "%Y-%m-%d")
            end_date = datetime.strptime(f'{request.POST["end_year"]}-{request.POST["end_month"]}-{request.POST["end_day"]}', "%Y-%m-%d")
            delta = end_date - start_date
            delta = int(delta.days) + 1
            Log.objects.create(
                start_date = start_date,
                end_date = end_date,
                comment = request.POST["comment"],
                delta = delta,
            )
            params = {
                "year_list": year_list,
                "month_list": month_list,
                "day_list": day_list,
                "delta": delta,
                "start_date": start_date,
                "end_date": end_date,
                "comment": request.POST["comment"],
            }
            return render(request, "main/index.html", params)
        except:
            params = {
                "year_list": year_list,
                "month_list": month_list,
                "day_list": day_list,
                "error": True,
            }
            return render(request, "main/index.html", params)

    else:
        pass


    params = {
        "year_list": year_list,
        "month_list": month_list,
        "day_list": day_list,
    }
    return render(request, "main/index.html", params)

# @login_required
def listView(request):
    return render(request, "main/list_view.html", {"log_list":Log.objects.all().order_by("-pub_date")})

# def result(request):
#     print(request.POST)
#     # delta = datetime.strptime(request.POST["end"], "%Y-%m-%d") - datetime.strptime(request.POST["start"], "%Y-%m-%d")
#     # delta = int(delta.days) + 1
#     # Log.objects.create(
#     #     start_date = datetime.strptime(request.POST["start"], "%Y-%m-%d"),
#     #     end_date = datetime.strptime(request.POST["end"], "%Y-%m-%d"),
#     #     comment = request.POST["comment"],
#     #     delta = delta,
#     # )
#     return render(request, "main/result.html", {"delta": delta})

@login_required
def admin_list(request):
    return render(request, "main/admin_list.html", {"log_list":Log.objects.all().order_by("-pub_date")})
    
@login_required
def admin_table(request):
    return render(request, "main/admin_table.html", {"log_list":Log.objects.all().order_by("-pub_date")})