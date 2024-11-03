from scraping import *
import pandas as pd

url = "https://phongvu.vn/c/laptop"
laptop_list = get_all_laptop(url)
print(laptop_list)
# Convert list of dictionaries to DataFrame
lap_df = pd.DataFrame(laptop_list)
# Display the DataFrame
print(lap_df)
lap_df.to_csv("phongvulaptop.csv", header=True, index=False)
lap_df.to_json("pvlaptop.json")

