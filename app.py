import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open("flight_rf.pkl", "rb"))

# Function to calculate duration
def calculate_duration(dep_hour, dep_min, arrival_hour, arrival_min):
    dur_hour = abs(arrival_hour - dep_hour)
    dur_min = abs(arrival_min - dep_min)
    return dur_hour, dur_min

def main():
    st.title("Flight Fare Prediction")
    
    # Input fields
    date_dep = st.date_input("Date of Departure", value=pd.to_datetime("2025-01-31").date())
    time_dep = st.time_input("Time of Departure", value=pd.to_datetime("10:00").time())
    
    date_arr = st.date_input("Date of Arrival", value=pd.to_datetime("2025-01-31").date())
    time_arr = st.time_input("Time of Arrival", value=pd.to_datetime("12:00").time())
    
    Total_stops = st.selectbox("Total Stops", [0, 1, 2, 3])
    
    airline = st.selectbox("Airline", ["Jet Airways", "IndiGo", "Air India", "Multiple carriers", "SpiceJet", "Vistara", "GoAir", "Multiple carriers Premium economy", "Jet Airways Business", "Vistara Premium economy", "Trujet"])
    
    Source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai"])
    Destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata"])

    # Parsing the departure time
    dep_time = pd.to_datetime(f"{date_dep} {time_dep}")
    dep_hour = dep_time.hour
    dep_min = dep_time.minute
    Journey_day = dep_time.day
    Journey_month = dep_time.month
    
    # Parsing the arrival time
    arr_time = pd.to_datetime(f"{date_arr} {time_arr}")
    arrival_hour = arr_time.hour
    arrival_min = arr_time.minute
    
    # Calculate duration
    dur_hour, dur_min = calculate_duration(dep_hour, dep_min, arrival_hour, arrival_min)
    
    # Encoding the airline
    airline_dict = {
        'Jet Airways': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'IndiGo': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Air India': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        'Multiple carriers': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        'SpiceJet': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        'Vistara': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        'GoAir': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        'Multiple carriers Premium economy': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        'Jet Airways Business': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        'Vistara Premium economy': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        'Trujet': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    }
    
    airline_features = airline_dict.get(airline, [0]*11)
    
    # Encoding the source and destination
    source_dict = {'Delhi': [1, 0, 0, 0], 'Kolkata': [0, 1, 0, 0], 'Mumbai': [0, 0, 1, 0], 'Chennai': [0, 0, 0, 1]}
    destination_dict = {'Cochin': [1, 0, 0, 0, 0], 'Delhi': [0, 1, 0, 0, 0], 'New Delhi': [0, 0, 1, 0, 0], 'Hyderabad': [0, 0, 0, 1, 0], 'Kolkata': [0, 0, 0, 0, 1]}

    source_features = source_dict.get(Source, [0]*4)
    destination_features = destination_dict.get(Destination, [0]*5)
    
    # Prepare input for prediction
    input_data = [
        Total_stops, Journey_day, Journey_month, dep_hour, dep_min,
        arrival_hour, arrival_min, dur_hour, dur_min,
        *airline_features, *source_features, *destination_features
    ]
    
    # Prediction
    if st.button("Predict Price"):
        prediction = model.predict([input_data])
        output = round(prediction[0], 2)
        st.success(f"Your flight price is Rs. {output}")

if __name__ == "__main__":
    main()
