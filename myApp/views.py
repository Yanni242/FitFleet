from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from .models import Bmi, Weight, Exercise
from math import pi
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource, Legend
from datetime import datetime


def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')  
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Custom logout so that it doesn't logout without asking
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  
    return render(request, 'logout.html')

def bmi(request):
    context = {}
    if request.method == "POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric")) / 100 # Convert cm to m
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial")) / 2.205
            height = (float(request.POST.get("feet")) * 30.48 + float(request.POST.get("inches")) * 2.54) / 100

        bmi = (weight / (height ** 2))
        save = request.POST.get("save")

        if save == "on":
            Bmi.objects.create(user = request.user, weight = weight, height = height, bmi = round(bmi))
    
        if bmi < 16:
            state = "Severe Thinness"
        elif bmi >= 16 and bmi < 17:
            state = "Moderate Thinness"
        elif bmi >= 17 and bmi < 18.5:
            state = "Mild Thinness"
        elif bmi >= 18.5 and bmi < 25:
            state = "Normal"
        elif bmi >= 25 and bmi < 30:
            state = "Overweight"
        elif bmi >= 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi >= 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi >= 40:
            state = "Obese Class III"

        context["bmi"] = round(bmi, 1)
        context["state"] = state

    if request.user.is_authenticated:
        dates = []
        bmis = []
        current_date = None
        count = 0

        dates_queryset = Bmi.objects.all().filter(user = request.user).order_by('date') 
        for qr in dates_queryset:
            date_str = str(qr.date)
            if date_str != current_date:
                current_date = date_str
                count = 1
            else:
                count += 1

            dates.append(f"{date_str}({count})")
            bmis.append(int(qr.bmi))
        
        plot = figure(x_range = dates, plot_height = 400, plot_width = 1200, title = "BMI Statistics", 
                      toolbar_location = "right", tools = "pan, wheel_zoom, box_zoom, reset, hover, tap, crosshair")
        plot.title.text_font_size = "20pt"
        plot.xaxis.major_label_text_font_size = "14pt"

        plot.step(dates, bmis, line_width = 2)
        plot.legend.label_text_font_size = "14pt"
        plot.xaxis.major_label_orientation = pi/4

        script, div = components(plot)
        context["script"] = script
        context["div"] = div

    return render(request, 'bmi.html', context)

def calorie(request):
    calorie_intake = None
    context = {}
    
    if request.method == "POST":
        # Extract data from form
        age = int(request.POST.get("age"))
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")
        gender = request.POST.get("gender")
        activity_level = request.POST.get("activity-level")

        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric")) 
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial")) / 2.205  # Convert from lbs to kg
            height = (float(request.POST.get("feet")) * 30.48 + float(request.POST.get("inches")) * 2.54)  # Convert from feet and inches to cm

        # Calculate calorie intake using Mifflin-St Jeor Equation
        if gender == "male":
            calorie_intake = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:  # female
            calorie_intake = (10 * weight) + (6.25 * height) - (5 * age) - 161
        
        # Adjust calorie intake based on activity level
        if activity_level == "sedentary":
            calorie_intake *= 1.2
        elif activity_level == "light":
            calorie_intake *= 1.375
        elif activity_level == "moderate":
            calorie_intake *= 1.55
        elif activity_level == "active":
            calorie_intake *= 1.725
        else:  # very-active or extra-active
            calorie_intake *= 1.9

    if calorie_intake is not None:
        # Calculate macros for moderate diet
        moderate_protein = (round(calorie_intake) * 0.3) / 4
        moderate_fat =  (round(calorie_intake) * 0.35) / 9
        moderate_carbs = (round(calorie_intake) * 0.35) / 4

        # Calculate macros for lower carb diet
        lower_carb_protein = (round(calorie_intake) * 0.4) / 4
        lower_carb_fat = (round(calorie_intake) * 0.4) / 9
        lower_carb_carbs = (round(calorie_intake) * 0.2) / 4

        # Calculate macros for high carb diet
        high_carb_protein = (round(calorie_intake) * 0.3) / 4
        high_carb_fat = (round(calorie_intake) * 0.2) / 9
        high_carb_carbs = (round(calorie_intake) * 0.5) / 4

        context['moderate_diet'] = {
            'protein': moderate_protein,
            'fat': moderate_fat,
            'carbs': moderate_carbs
        }
        context['lower_carb_diet'] = {
            'protein': lower_carb_protein,
            'fat': lower_carb_fat,
            'carbs': lower_carb_carbs
        }
        context['high_carb_diet'] = {
            'protein': high_carb_protein,
            'fat': high_carb_fat,
            'carbs': high_carb_carbs
        }

        context["calorie_intake"] = round(calorie_intake)
    else:
        context["calorie_intake"] = None

    return render(request, 'calorie.html', context)


def weight(request):
    context = {}

    if request.method == "POST" and request.user.is_authenticated:
        weight_value = float(request.POST.get("weight"))
        notes_value = request.POST.get("notes")
        date_value = request.POST.get("date")
        date_value = datetime.strptime(date_value, "%Y-%m-%d").date()

        # Update or create a Weight object with the given parameters
        Weight.objects.update_or_create(user = request.user, date = date_value, defaults = {'weight': weight_value, 'notes': notes_value})

        # Check if a Weight object for the given date and user already exists
        weight_entry, created = Weight.objects.get_or_create(user = request.user, date = date_value)
        
        # Update the weight and notes
        weight_entry.weight = weight_value
        weight_entry.notes = notes_value
        weight_entry.save()

    if request.user.is_authenticated:
        dates = []
        weights = []
        weight_records = []
        weight_records_reversed = []
        moving_averages = []
        total_changes = []
        weights_queryset = Weight.objects.filter(user=request.user).order_by('date')

        for i, qr in enumerate(weights_queryset):
            dates.append(str(qr.date))
            weights.append(float(qr.weight))

            # Calculate moving average for all available weights up to this day
            moving_average = sum(weights[:i+1]) / (i + 1)
            moving_average = round(moving_average, 1)
            moving_averages.append(moving_average)

            # Calculate total progress as the change in weight from the earliest available day
            total_change = weights[i] - weights[0] if i > 0 else 0
            total_change = round(total_change, 1)
            total_changes.append(total_change)

            weight_records.append({
                'date': qr.date,
                'weight': qr.weight,
                'moving_average': moving_average,
                'total_change': total_change,
                'notes': qr.notes
            })

            weight_records_reversed.append({
                'date': qr.date,
                'weight': qr.weight,
                'moving_average': moving_average,
                'total_change': total_change,
                'notes': qr.notes
            })

        plot = figure(x_range=dates, plot_height=400, plot_width=1200, title="Weight Statistics",
                      toolbar_location="right", tools="pan, wheel_zoom, box_zoom, reset, hover, tap, crosshair")
        plot.title.text_font_size = "20pt"
        plot.xaxis.major_label_text_font_size = "14pt"

        # Step renderer
        plot.step(dates, weights, line_width=2)
        plot.xaxis.major_label_orientation = pi / 4

        script, div = components(plot)
        context['weight_records'] = weight_records
        context['weight_records_reversed'] = reversed(weight_records_reversed)
        context["script"] = script
        context["div"] = div

    return render(request, 'weight.html', context)

def exercises(request):
    exercises = Exercise.objects.all()
    categories = Exercise.CATEGORY_CHOICES

    context = {
        'exercises': exercises,
        'categories': categories}

    return render(request, 'exercises.html', context)
