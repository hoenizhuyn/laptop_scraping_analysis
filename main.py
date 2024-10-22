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


# Example: Extract laptop links (assuming they are within a div with class "css-7nga9q")
# laptop_block = soup.find("div", class_="css-7nga9q")
# if laptop_block:
#     links = laptop_block.find_all("a", class_="css-1h3fn00")
#     for link in links:
#         href = link['href']
#         full_url = f"https://phongvu.vn{href}"  # Assuming the link is relative
#         print(full_url)
# else:
#     print("Laptop block not found")
