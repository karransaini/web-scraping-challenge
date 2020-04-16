#!/usr/bin/env python
# coding: utf-8

#import dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


def scrape():
# # NASA Mars News


# def mars_news_scrape():
    url_mars = "https://mars.nasa.gov/news/"
    response_news = requests.get(url_mars)
    html_news = response_news.text
    soup_news = bs(html_news, "html.parser")
    news = soup_news.find_all('div',class_='content_title')
    latestnews = news[0].text.strip() 
    parag = soup_news.find('div',class_='rollover_description_inner')
    latestparag = parag.text.strip()

    # return (latestnews, latestparag)



# # JPL Mars Space Images - Featured Image

# def mars_jpl_scrape():
    url_JPL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response_JPL = requests.get(url_JPL)
    html_JPL = response_JPL.text
    soup_JPL = bs(html_JPL, "html.parser")
    jpl_img = soup_JPL.find('div',class_='carousel_items')
    featuredimage = jpl_img.a['data-fancybox-href']
    featured_image_url = "https://www.jpl.nasa.gov"+featuredimage


    # return (featured_image_url)


# # Mars Weather

# def mars_weather_scrape():
    url_mw = "https://twitter.com/marswxreport?lang=en"
    response_mw = requests.get(url_mw)
    html_mw = response_mw.text
    soup_mw = bs(html_mw, "html.parser")
    mw_tweet = soup_mw.find('div',class_='js-tweet-text-container')
    mars_weather = mw_tweet.p.text
    
    # return (mars_weather)


# # Mars Facts
# def mars_facts_scrape():
    url_facts = "https://space-facts.com/mars/"
    tables = pd.read_html(url_facts)
    mars_facts = tables[0]
    mars_facts.columns = ['Data Point', 'Value']
    mars_facts.set_index('Data Point', inplace=True)
    html_facts_mars = mars_facts.to_html()
    html_facts_mars.replace('\n', '')
    html_facts_mars
    # return (mars_facts)



# # Mars Hemispheres
# def mars_hemis_scrape():
    url_hem = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response_hem = requests.get(url_hem)
    html_hem = response_hem.text
    soup_hem = bs(html_hem, "html.parser")
    hem_container = soup_hem.find_all('div',class_='item')
    hem_url = hem_container[0].a['href']

    hemisphere_image_urls = []

    for item in hem_container:
        hem_url = item.find('a')['href']
        update_hem_url = "https://astrogeology.usgs.gov"+ hem_url
        response_ = requests.get(update_hem_url)
        html_hem_ = response_.text
        soup_hem_ = bs(html_hem_, "html.parser")
        img_path = "https://astrogeology.usgs.gov"+soup_hem_.find("img", class_="wide-image")["src"]
        title = soup_hem_.div.h2.text
        hemisphere_image_urls.append({'title': title,'url_img': img_path})


    
    # def final():
        mars_info = {
            "latestnews":latestnews,
            "latestparag":latestparag,
            "featured_image_url":featured_image_url,
            "mars_weather": mars_weather,
            "html_facts_mars":html_facts_mars,
            "hemisphere_image_urls":hemisphere_image_urls
        }
        
        return (mars_info)

    print(scrape())