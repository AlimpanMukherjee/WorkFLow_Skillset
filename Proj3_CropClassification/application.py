

# from flask import Flask, render_template, request
# import numpy as np
# import pickle

# application = Flask(__name__)
# app = application

# # Load model and scaler
# randomforest_model = pickle.load(open('C:/python prog/Proj3_CropClassification/models/model.pkl', 'rb'))
# standard_scaler = pickle.load(open('C:/python prog/Proj3_CropClassification/models/scaler.pkl', 'rb'))

# def build_full_feature_vector(N, P, K, temp, humid, ph, rain):
#     total_npk = N + P + K
#     n_p_ratio = N / (P + 1e-6)
#     n_k_ratio = N / (K + 1e-6)
#     p_k_ratio = P / (K + 1e-6)
#     nutrient_balance = abs(N - P) + abs(P - K) + abs(N - K)
#     soil_fertility_index = N * 0.4 + P * 0.3 + K * 0.3

#     if temp <= 15:
#         temp_cat = 0
#     elif temp <= 25:
#         temp_cat = 1
#     elif temp <= 35:
#         temp_cat = 2
#     else:
#         temp_cat = 3

#     if humid <= 40:
#         humid_cat = 0
#     elif humid <= 70:
#         humid_cat = 1
#     elif humid <= 90:
#         humid_cat = 2
#     else:
#         humid_cat = 3

#     if rain <= 50:
#         rain_cat = 0
#     elif rain <= 100:
#         rain_cat = 1
#     elif rain <= 200:
#         rain_cat = 2
#     else:
#         rain_cat = 3

#     base_temp = 10
#     growing_degree_days = max(temp - base_temp, 0)
#     heat_index = temp + (humid / 100) * temp
#     aridity_index = rain / (temp + 1e-6)

#     if ph <= 5.5:
#         ph_cat = 0
#     elif ph <= 6.5:
#         ph_cat = 1
#     elif ph <= 7.5:
#         ph_cat = 2
#     else:
#         ph_cat = 3

#     ph_nutrient_availability = 1 if 6.0 <= ph <= 7.5 else 0
#     ph_optimality = 1 - abs(ph - 6.75) / 6.75

#     temp_humidity_interaction = temp * humid / 100
#     water_temp_balance = rain / (temp + 1e-6)
#     nutrient_climate_index = (total_npk / 100) * (temp / 30) * (rain / 150)
#     heat_stress = 1 if temp > 35 else 0
#     drought_stress = 1 if rain < 50 else 0
#     waterlogging_risk = 1 if rain > 250 else 0
#     optimal_conditions = int(
#         20 <= temp <= 30 and 60 <= humid <= 80 and 75 <= rain <= 200 and 6.0 <= ph <= 7.5
#     )
#     water_requirement_index = rain * humid / 1000
#     soil_richness = (N / 140) * 0.4 + (P / 145) * 0.3 + (K / 205) * 0.3
#     climate_suitability = (1 - abs(temp - 25) / 25) * 0.4 + (humid / 100) * 0.3 + (min(rain, 200) / 200) * 0.3

#     return [
#         N, P, K, temp, humid, ph, rain,
#         total_npk, n_p_ratio, n_k_ratio, p_k_ratio, nutrient_balance,
#         temp_cat, rain_cat, heat_index, 
#         ph_nutrient_availability, ph_optimality,
#         nutrient_climate_index, heat_stress, drought_stress, waterlogging_risk,
#         optimal_conditions, water_requirement_index,
#         climate_suitability
#     ]

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     if request.method == 'POST':
#         Nitrogen = float(request.form.get('Nitrogen'))
#         phosphorus = float(request.form.get('phosphorus'))
#         potassium = float(request.form.get('potassium'))
#         temperature = float(request.form.get('temperature'))
#         humidity = float(request.form.get('humidity'))
#         ph = float(request.form.get('ph'))
#         rainfall = float(request.form.get('rainfall'))

#         full_features = build_full_feature_vector(Nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
#         new_data_scaled = standard_scaler.transform([full_features])
#         result = randomforest_model.predict(new_data_scaled)
#         return render_template('home.html', crop=result[0])
#     else:
#         return render_template('home.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")
#     app.debug = True




from flask import Flask, render_template, request
import numpy as np
import pickle
import os

application = Flask(__name__)
app = application


# Crop label mapping (number → crop name)
label_mapping = {
    0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea',
    4: 'coconut', 5: 'coffee', 6: 'cotton', 7: 'grapes',
    8: 'jute', 9: 'kidneybeans', 10: 'lentil', 11: 'maize',
    12: 'mango', 13: 'mothbeans', 14: 'mungbean', 15: 'muskmelon',
    16: 'orange', 17: 'papaya', 18: 'pigeonpeas', 19: 'pomegranate',
    20: 'rice', 21: 'watermelon'
}

def load_models():
    try:
        # Try different possible paths
        model_paths = [
            'models/model.pkl',
            'model.pkl',
            'C:/python prog/Proj3_CropClassification/models/model.pkl'
        ]
        
        scaler_paths = [
            'models/scaler.pkl',
            'scaler.pkl',
            'C:/python prog/Proj3_CropClassification/models/scaler.pkl'
        ]
        
        model_loaded = False
        scaler_loaded = False
        
        for path in model_paths:
            if os.path.exists(path):
                global randomforest_model
                randomforest_model = pickle.load(open(path, 'rb'))
                print(f"Model loaded from: {path}")
                # Verify model is fitted
                if hasattr(randomforest_model, 'estimators_'):
                    print("Model is properly fitted")
                    model_loaded = True
                else:
                    print("Warning: Model is not fitted!")
                break
        
        for path in scaler_paths:
            if os.path.exists(path):
                global standard_scaler
                standard_scaler = pickle.load(open(path, 'rb'))
                print(f"Scaler loaded from: {path}")
                scaler_loaded = True
                break
        
        if not model_loaded:
            raise FileNotFoundError("Model file not found in any expected location")
        if not scaler_loaded:
            raise FileNotFoundError("Scaler file not found in any expected location")
            
        return True
    except Exception as e:
        print(f"Error loading models: {e}")
        return False

# Load models at startup
models_loaded = load_models()

def build_full_feature_vector(N, P, K, temp, humid, ph, rain):
    total_npk = N + P + K
    n_p_ratio = N / (P + 1e-6)
    n_k_ratio = N / (K + 1e-6)
    p_k_ratio = P / (K + 1e-6)
    nutrient_balance = abs(N - P) + abs(P - K) + abs(N - K)
    soil_fertility_index = N * 0.4 + P * 0.3 + K * 0.3

    if temp <= 15:
        temp_cat = 0
    elif temp <= 25:
        temp_cat = 1
    elif temp <= 35:
        temp_cat = 2
    else:
        temp_cat = 3

    if humid <= 40:
        humid_cat = 0
    elif humid <= 70:
        humid_cat = 1
    elif humid <= 90:
        humid_cat = 2
    else:
        humid_cat = 3

    if rain <= 50:
        rain_cat = 0
    elif rain <= 100:
        rain_cat = 1
    elif rain <= 200:
        rain_cat = 2
    else:
        rain_cat = 3

    base_temp = 10
    growing_degree_days = max(temp - base_temp, 0)
    heat_index = temp + (humid / 100) * temp
    aridity_index = rain / (temp + 1e-6)

    if ph <= 5.5:
        ph_cat = 0
    elif ph <= 6.5:
        ph_cat = 1
    elif ph <= 7.5:
        ph_cat = 2
    else:
        ph_cat = 3

    ph_nutrient_availability = 1 if 6.0 <= ph <= 7.5 else 0
    ph_optimality = 1 - abs(ph - 6.75) / 6.75

    temp_humidity_interaction = temp * humid / 100
    water_temp_balance = rain / (temp + 1e-6)
    nutrient_climate_index = (total_npk / 100) * (temp / 30) * (rain / 150)
    heat_stress = 1 if temp > 35 else 0
    drought_stress = 1 if rain < 50 else 0
    waterlogging_risk = 1 if rain > 250 else 0
    optimal_conditions = int(
        20 <= temp <= 30 and 60 <= humid <= 80 and 75 <= rain <= 200 and 6.0 <= ph <= 7.5
    )
    water_requirement_index = rain * humid / 1000
    soil_richness = (N / 140) * 0.4 + (P / 145) * 0.3 + (K / 205) * 0.3
    climate_suitability = (1 - abs(temp - 25) / 25) * 0.4 + (humid / 100) * 0.3 + (min(rain, 200) / 200) * 0.3

    return [
        N, P, K, temp, humid, ph, rain,
        total_npk, n_p_ratio, n_k_ratio, p_k_ratio, nutrient_balance,
        temp_cat, rain_cat, heat_index, 
        ph_nutrient_availability, ph_optimality,
        nutrient_climate_index, heat_stress, drought_stress, waterlogging_risk,
        optimal_conditions, water_requirement_index,
        climate_suitability
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])



def predict_datapoint():
    if not models_loaded:
        return render_template('home.html', crop="Error: Models not loaded properly")

    if request.method == 'POST':
        try:
            Nitrogen = float(request.form.get('Nitrogen'))
            phosphorus = float(request.form.get('phosphorus'))
            potassium = float(request.form.get('potassium'))
            temperature = float(request.form.get('temperature'))
            humidity = float(request.form.get('humidity'))
            ph = float(request.form.get('ph'))
            rainfall = float(request.form.get('rainfall'))

            full_features = build_full_feature_vector(
                Nitrogen, phosphorus, potassium,
                temperature, humidity, ph, rainfall
            )

            new_data_scaled = standard_scaler.transform([full_features])
            result = randomforest_model.predict(new_data_scaled)

            # Convert number → crop name
            predicted_crop = label_mapping.get(result[0], "Unknown")

            return render_template('home.html', crop=predicted_crop)

        except ValueError as e:
            return render_template('home.html', crop=f"Error: Invalid input values - {str(e)}")
        except Exception as e:
            return render_template('home.html', crop=f"Error: {str(e)}")
    else:
        return render_template('home.html')



if __name__ == "__main__":
    if models_loaded:
        app.run(host="0.0.0.0", debug=True)
    else:
        print("Cannot start app: Models failed to load")

