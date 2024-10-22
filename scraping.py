import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def show_more_products(driver, button_tag):
    """Clicks the 'Show More Products' button if it's present."""
    try:
        # Scroll down to make sure the button is VISIBLE
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust this sleep if necessary

        # Wait for the "Show more products" button to become clickable
        wait = WebDriverWait(driver, 5)
        show_more_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, button_tag))
        )

        # show_more_button.click() can easily get interrupted
        # Click the button using JavaScript to avoid "element click intercepted" error
        driver.execute_script("arguments[0].click();", show_more_button)

        # Wait for the new products to load (you can adjust this)
        time.sleep(5)
        return True
    except Exception as e:
        # print(f"No more 'Show more products' button found or an error occurred: {e}")
        return False

def laptoplistpage(url): 
    #let url be the main laptop page products
    #get the soup format òf the page that contains all the laptop products
    # Set up your Edge WebDriver
    webdriver_service = Service('C:/Users/buing/Downloads/fundamentalDS/msedgedriver.exe')
    more_button_tag = "css-b0m1yo"
    # Initialize the driver
    driver = webdriver.Edge(service=webdriver_service)
    try:
        # Open the webpage
        driver.get(url)
        
        # Use WebDriverWait to wait until the product content block is present
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1y2krk0")))

        # Keep clicking the "Show More Products" button until it disappears
        while show_more_products(driver, more_button_tag):
            pass

        # Get the page source after expanding products
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        
        return soup
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the driver
        driver.quit()

def get_laptop_info(product_url):
    """Extract INFO of a product given that there is a link"""
    webdriver_service = Service('C:/Users/buing/Downloads/fundamentalDS/msedgedriver.exe')
    more_tag = "css-1alns4t"
    # Initialize the driver
    driver = webdriver.Edge(service=webdriver_service)
    try:
        # Open the webpage
        driver.get(product_url)
        
        # wait until page load
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "css-6l7rf5")))
        features_dict = {}

        # GET PRODUCT NAME and PRICE 
        title = driver.find_element(By.CLASS_NAME, "css-nlaxuc")  # Locate the <h1> tag
        features_dict["Product name"] = title.text.strip()
        price = driver.find_element(By.CLASS_NAME, "att-product-detail-latest-price") 
        features_dict["Price"] = price.text.strip()
          
        while show_more_products(driver, more_tag):
            pass  
         
        # Extract each LINE of FEATURES
        features = driver.find_elements(By.CLASS_NAME, "css-1i3ajxp")
        for feature in features:
            try:
                # Find the first and second divs within the feature
                key_element = feature.find_element(By.XPATH, './div[1]')
                value_element = feature.find_element(By.XPATH, './div[2]')
                
                # Extract text from the div elements
                key = key_element.text.strip()
                value = value_element.text.strip()

                # Add the key-value pair to the dictionary
                features_dict[key] = value            
            except Exception as e:
                print(f"Error extracting feature: {e}")
        return(features_dict)
    finally:
        # Close the driver
        driver.quit()
    
def get_all_laptop(url): 
    """Input: main product page
    Output: a list of dictionary with each dict correspond to a laptop sample"""
    #get soup at main laptop page
    soup = laptoplistpage(url)
    """use to get each laptop info"""
    #take content block that only contains products
    product_content = soup.find("div", class_ = "css-1y2krk0")
    count = 0
    laptop_list = []
    if product_content: #IF THERE IS PRODUCT BLOCK
        links = product_content.find_all("a", class_="css-pxdb0j")
        # Loop for extracting links from Tag Objects
        for link in links:
            href = link['href']
            laptop_url = f"https://phongvu.vn{href}"   
            #get the laptop info as dictionary as each key = 1 info
            laptop_info = get_laptop_info(laptop_url)
            laptop_list.append(laptop_info)
    return laptop_list
             

    


    



