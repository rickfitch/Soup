def get_numbers():
    from bs4 import BeautifulSoup
    import requests
    import time

    fantasy5 = []
    draw_number = 0

    url = "https://www.calottery.com/draw-games/fantasy-5"

    response = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(response)
    #print(soup.prettify())

    links = soup.find_all('a')
    #print(len(links))

    divs = soup.find('div',id = 'winningNumbers10')

    # get Date and time of the draw
    p = divs.find_all('p')
    fantasy5.append(p[2].text)
    fantasy5.append(p[1].text)

    #clean the draw number removed from list, stripped then converted to int
    x = fantasy5[0]
    clean = x.strip("Draw #")
    fantasy5[0] = int(clean)

    #clean the date and time remove from list, cleaned then converted to string
    clean = fantasy5[1][4:]
    #print(type(clean))
    fantasy5[1] = clean  
    #print(type(fantasy5[0]))   

    # get the winning numbers
    spans = divs.find_all('span')
    for span in spans:
        fantasy5.append(int(span.text))
    #print(fantasy5)
    # list ready for export to csv
    # draw number, date, winning numbers
    return fantasy5
