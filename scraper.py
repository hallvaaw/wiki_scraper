import requests
from bs4 import BeautifulSoup


def scrapeWikiArticle(url):
    response = requests.get(
    	url=url,
    )
    
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    print(title.text)
    main_text_title = soup.find(id = "mw-content-text")
    main_text = main_text_title.find_all('p')
    
    for i in main_text:
        a_text = i.a
        if a_text != None:
            a_text_parent = a_text.parent.parent.parent
            if "href" in str(a_text):
                if "/wiki/" in a_text['href']:
                    break
            
    # main_text_a = main_text[0]
    # main_text_link = main_text_a.find("a")
    scrapeWikiArticle("https://en.wikipedia.org" + a_text['href'])
    # scrapeWikiArticle("https://en.wikipedia.org" + main_text_link['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Logic")
