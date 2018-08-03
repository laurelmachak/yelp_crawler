from bs4 import BeautifulSoup
from parser import simple_get

# raw_html = open('test.html').read()

raw_html = simple_get('https://www.yelp.com/biz/jacks-prime-san-mateo-4?osq=burger')
print("done")
html = BeautifulSoup(raw_html, 'html.parser')
#for span in html.select('span'):
    #if span['class_'] == 'biz-website':
        #print(span.contents)

        
#bus_url = html.find_all("span", class_="biz-website")


def get_business_website():
    business_url = html.find("span", class_="biz-website")
    return(business_url.contents[3].contents)

print(get_business_website())


#bus_url = html.find("span", class_="biz-website")
#print("contents: ", bus_url.contents)
#print("children: ", bus_url.children)
# the business url
#print(bus_url.contents[3].contents)

def get_phone():
    business_phone = html.find("span", class_="biz-phone").text.split()
    #TODO check format
    return(business_phone[0] + business_phone[1])

print(get_phone())



def get_price():
    price_range = html.find("span", class_="price-range")
    return(price_range.text)
    #return(price_range['data-remainder'])

print(get_price())


def get_title():
    business_title_list = html.find("h1", class_="biz-page-title").text.split()
    business_title = ""
    for word in range(len(business_title_list)):
        business_title += business_title_list[word]
        if word != len(business_title_list):
            business_title += " "
        
    return(business_title)
    

print(get_title())


def get_info():
    info_list = html.find("div", class_="short-def-list")
    
    # make a list of all the keys
    info_list_keys = info_list.find_all("dt", class_="attribute-key")
    for each_key in range(len(info_list_keys)):
        info_list_keys[each_key] = info_list_keys[each_key].text.strip()
        
    # make a list of all the values
    info_list_values = info_list.find_all("dd")
    for each_value in range(len(info_list_values)):
        info_list_values[each_value] = info_list_values[each_value].text.strip()
        
    business_info_dict = dict(zip(info_list_keys, info_list_values))
    
    return(business_info_dict)

print(get_info())


def get_hours():
    hours_table = html.find("table", class_="hours-table")
    
    days_of_week = hours_table.find_all("th", scope="row")
    
    for day in range(len(days_of_week)):
        days_of_week[day] = days_of_week[day].text

        
    hours_list = hours_table.find_all("span", class_="nowrap")
    
    now_open_tag_index = None
    
    for time in range(len(hours_list)):

        if hours_list[time]['class'] == ["nowrap", "open"]:
            now_open_tag_index = time

        hours_list[time] = hours_list[time].text


    if now_open_tag_index != None:
        hours_list.pop(now_open_tag_index)  

    business_hours_dict = dict()

    open_hour = 0
    close_hour = 1

    for day in days_of_week:
        print(day)
        business_hours_dict[day] = [hours_list[open_hour], hours_list[close_hour]]
        open_hour += 2
        close_hour += 2
    
    return business_hours_dict

print(get_hours())

def get_address():
    full_address = html.find("address")

    address_dict = dict()

    address_dict["street_address"] = full_address.find("span", itemprop="streetAddress").text

    address_dict["city"] = full_address.find("span", itemprop="addressLocality").text

    address_dict["state"] = full_address.find("span", itemprop="addressRegion").text

    address_dict["postal_code"] = full_address.find("span", itemprop="postalCode").text

    return(address_dict)

print(get_address())





def get_categories():
    catetories_html = html.find("span", class_="category-str-list")

    categories_list = catetories_html.find_all("a")

    for category in range(len(categories_list)):
        categories_list[category] = categories_list[category].text

    return(categories_list)

print(get_categories())


def get_claimed_status():
    claimed = False
    
    claimed_string = html.find("div", class_="claim-status_teaser").text.strip()

    if claimed_string == "Claimed":
        claimed = True

    return(claimed)

print(get_claimed_status())


def get_url_to_pics():
    base_url = "https://www.yelp.com/"
    link_to_pics_html = html.find("a", class_="see-more")["href"]

    link_to_pics = base_url + link_to_pics_html

    return(link_to_pics)

print(get_url_to_pics())




def get_pictures():
    raw_html_pics = simple_get(get_url_to_pics())
    html_pics = BeautifulSoup(raw_html_pics, 'html.parser')

    picture_links = html_pics.find_all("img", class_="photo-box-img")

    for link in range(len(picture_links)):
        picture_links[link] = picture_links[link]["src"]

    return(picture_links)

# print(get_pictures())


def get_total_pic_pages():

    # kinda hacky rn, maybe check how the javascript or something else
    # generates the page nums 
    raw_html_pics = simple_get(get_url_to_pics())
    html_pics = BeautifulSoup(raw_html_pics, 'html.parser')

    total_num_html = html_pics.find("div", class_="page-of-pages").text.strip()
    total_num_html = total_num_html.split()[3]
    total_num_html = int(total_num_html)
    return(total_num_html)

print(get_total_pic_pages())

def get_total_pics():
    raw_html_pics = simple_get(get_url_to_pics())
    html_pics = BeautifulSoup(raw_html_pics, 'html.parser')

    num_of_pics = html_pics.find("span", class_="tab-link_count").text.strip('()')
    return(int(num_of_pics))

print(get_total_pics())


def go_to_next_page_pics(current_page):
    # assume total pics per page is 30
    pass 

def get_pic_description():
    pass

def get_link_to_pic_slideshow():
    raw_html_pics = simple_get(get_url_to_pics())
    html_pics = BeautifulSoup(raw_html_pics, 'html.parser')
    first_pic_link = html_pics.find("div", class_="photo-box--interactive").a["href"]
    first_pic_link = 'https://www.yelp.com' + first_pic_link

    return(first_pic_link)

# print(get_link_to_pic_slideshow())



    






















