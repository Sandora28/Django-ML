import joblib
import os
from django.shortcuts import render
from .forms import HouseForm

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            prediction = model.predict([data])[0]
            prediction = round(prediction, 2)
    else:
        form = HouseForm()

    return render(request, 'predict/predict.html', {'form': form, 'prediction': prediction})
