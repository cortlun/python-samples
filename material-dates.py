import uuid
import pandas as pd
from datetime import datetime, timedelta


material_ids = [str(uuid.uuid4()) for i in range(0,3)] # Generate a list of material ids


start_date = datetime.strptime("2020-10-12", "%Y-%m-%d") # Specify start date
end_date = datetime.strptime("2020-10-15", "%Y-%m-%d") # Specify end date
dates_list = [start_date + timedelta(days=i) for i in range(0, (end_date - start_date).days + 1)] # Generate a list of dates, inclusive

output = [{
    "date": date.strftime("%Y-%m-%d"),
    "material_id": material_id
} for material_id in material_ids for date in dates_list] # Use nested list comprehension to produce output as a list of dictionaries

output_df = pd.DataFrame(output) # Generate a DataFrame with the output you want

print(output_df)