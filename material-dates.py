import uuid
import pandas as pd
from datetime import datetime, timedelta

material_ids = [str(uuid.uuid4()) for i in range(0,3)] # Generate a list of material ids

start_date = datetime.strptime("2020-10-12", "%Y-%m-%d") # Specify start date
end_date = datetime.strptime("2020-10-15", "%Y-%m-%d") # Specify end date
dates = [start_date + timedelta(days=i) for i in range(0, (end_date - start_date).days + 1)] # Generate a list of dates, inclusive

output_list = [{
    "date": date.strftime("%Y-%m-%d"),
    "material_id": material_id
} for material_id in material_ids for date in dates] # Use nested list comprehension to produce output as a list of dictionaries

output_df = pd.DataFrame(output_list) # Create df from list of dicts

print(output_df) # Print df