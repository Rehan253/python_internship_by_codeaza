import grequests
from bs4 import BeautifulSoup
import pandas as pd
import os



def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Remove any newline characters from each link
    links = [link.rstrip('\n') for link in links]
    return links
file_path = 'prod_links.txt'
product_links = read_links_from_file(file_path)

def remove_duplicates(input_list):
    # Convert the list to a set, which removes duplicates, then convert it back to a list
    return list(set(input_list))

product_urls = remove_duplicates(product_links)
print(len(product_urls))



def parse_html(response,**kwargs):
    # Parse the HTML content of the response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

 
    
    # Category
    elements = soup.select('div.col ul li')
    category1 = elements[2].text


    category2 = elements[3].text

    # Series
    series = soup.select_one('#collname')

    # Product name
    name = soup.select_one('#prod-name')

    # Article number
    article_number = soup.select_one('#prod-ref')

    # Dimensions
    dim = soup.select_one('#dim-txt').text
    L = dim[0:3]
    W = dim[6:9]
    H = dim[12:16]

    # Colors
    colors = soup.find_all('div', class_='colors-description')
    colours = [color.text.strip().replace('\r\n', '').replace('\n', '').replace('\t', '') for color in colors]

    # Types
    types = soup.find_all('div', class_='form-group')
    type = [t.text.strip().replace('\r\n', '').replace('\n', '').replace('\t', '') for t in types]

    # Short Description
    short_des = soup.findAll('div', class_='row r-body zero-margin-bottom')
    short_description = [d.text.strip().replace('\r\n', '').replace('\n', ' ').replace('\t', '') for d in short_des]

    # Material
    material = soup.find('div',class_='col-lg-12 caracteristicas-titulo').text

    # Long Description
    long_descirption = soup.find('p',class_='clamp').text

    # Data Sheet URL
    url_class = soup.find_all('div', class_='col-12 col-lg-8')
    root_src = 'https://www.laufen.co.at'
    data_sheet_url = []
    for u in url_class:
        url_elements = u.find_all('a')
        for url_element in url_elements:
            if url_element.has_attr('href'):
                url = url_element['href']
                full_url = root_src + url
                data_sheet_url.append(full_url)

    # 3D Data URL
    file_url = soup.find('p', class_='tabla-download')
    datafile_url = []
    if file_url and file_url.a and file_url.a['href']: 
        full_file_url = root_src + file_url.a['href']
        datafile_url.append(full_file_url)
    
    # Main Image
    div = soup.find('div',{"class":"slick-slide"})
    img_src = div.find('img').attrs['src']
    main_image = root_src + img_src

    # All Images
    divs = soup.find_all('div', {'class': 'slick-option-all'})
    image_list = []
    for div in divs:
        img = div.find('img')
        if img:
            relative_src = img.get('src')
            full_src = root_src + relative_src
            image_list.append(full_src)
    
    # Store the data in a dictionary
    data_dict = {
        'Category1': category1,
        'Category2': category2,
        'Series': series.text if series else '',
        'Name': name.text if name else '',
        'Article Number': article_number.text if article_number else '',
        'Length': L,
        'Width': W,
        'Height': H,
        'Colours': colours,
        'Types': type,
        'Short Description': short_description,
        'Material': material,
        'Long Description': long_descirption,
        'Data Sheet': data_sheet_url,
        '3D Data': datafile_url,
        'Main Image': main_image,
        'All Images': image_list,
        'Product URL':response.url
    }

    # Convert the dictionary into a pandas DataFrame
    new_data = pd.DataFrame([data_dict])

    # Check if the Excel file already exists
    if os.path.isfile('data.xlsx'):
        # Load existing data
        existing_data = pd.read_excel('data.xlsx')
        # Concatenate new data with existing data
        df = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        df = new_data

    # Save the DataFrame into the Excel file
    df.to_excel('data.xlsx', index=False)


# list of the URLs for all the products 
urls = [ 'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H817301...1091?sku=H8173010001091',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H817302...1091?sku=H8173020001091',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-semi-trockenen-bereichen-H817281...1051?sku=H8172810001051',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H818963...1041?sku=H8189630001041',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H813951...1041?sku=H8139510001041',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H813951...1421?sku=H8139510001421',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H813951...1561?sku=H8139510001561',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-H813961...1041?sku=H8139610001041',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-armaturenbank-H811391...0001?sku=H8113910000001',
        'https://www.laufen.co.at/produkte/einbauwaschtisch-oben-armaturenbank-H811392...0001?sku=H8113920000001',
        'https://www.laufen.co.at/produkte/halbeinbauwaschtisch-rund-H813431...1041?sku=H8134310001041',
        'https://www.laufen.co.at/produkte/halbeinbauwaschtisch-rechteckig-H813432...1041?sku=H8134320001041',
        'https://www.laufen.co.at/produkte/halbeinbauwaschtisch-H812951...1041?sku=H8129510001041',
        'https://www.laufen.co.at/produkte/halbeinbauwaschtisch-H812961...1041?sku=H8129610001041',
        'https://www.laufen.co.at/produkte/waschtisch-liberty-barrierefrei-verbundwerkstoff-marbond-H811474...1111?sku=H8114740001111',
        'https://www.laufen.co.at/produkte/waschtisch-liberty-barrierefrei-verbundwerkstoff-marbond-H811477...1111?sku=H8114770001111',
        'https://www.laufen.co.at/produkte/waschtisch-barrierefrei-H811950...1041?sku=H8119500001041',
        'https://www.laufen.co.at/produkte/waschtisch-barrierefrei-H811953...1041?sku=H8119530001041',
        'https://www.laufen.co.at/produkte/waschtisch-barrierefrei-H810603...0001?sku=H8106030000001',
        'https://www.laufen.co.at/produkte/aufsatz-waschtisch-ablage-links-verstecktem-ablauf-unterseite-geschliffen-H818339...1111?sku=H8183390001111'
        
        ]
links = urls + product_links

# list of grequests
reqs = [grequests.get(u, hooks={'response': parse_html}) for u in links]

# Send the requests and wait for the responses 
grequests.map(reqs)
