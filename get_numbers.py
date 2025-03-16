# new version for github "lotto_info"
def get_numbers():
    from bs4 import BeautifulSoup
    import requests
    import time

    mega_millions = []
    draw_number = 0

    #url = "https://www.calottery.com/draw-games/fantasy-5"
    url = "https://www.calottery.com/draw-games/mega-millions"

    response = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(response.text, 'html.parser')
    def get_numbers():
        from bs4 import BeautifulSoup
    import requests
    import time

    mega_millions = []
    draw_number = 0

    # url = "https://www.calottery.com/draw-games/fantasy-5"
    url = "https://www.calottery.com/draw-games/mega-millions"

    response = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.find('div', id='winningNumbers15')

    # get Date and time of the draw
    p = divs.find_all('p')
    mega_millions.append(p[2].text)
    mega_millions.append(p[1].text)

    # clean the draw number removed from list, stripped then converted to int
    x = mega_millions[0]
    clean = x.strip("Draw #")
    mega_millions[0] = int(clean)

    # clean the date and time remove from list, cleaned then converted to string
    clean = mega_millions[1][5:]
    mega_millions[1] = clean

    # get the winning numbers
    spans = divs.find_all('span')
    for span in spans:
        if span.text.isdigit():  # add this check
            mega_millions.append(int(span.text))
    return mega_millions
    #
    print(response)
    #print(soup.prettify())

    links = soup.find_all('a')
    #print(len(links))

    divs = soup.find('div',id = 'winningNumbers15')

    # get Date and time of the draw
    p = divs.find_all('p')
    mega_millions.append(p[2].text)
    mega_millions.append(p[1].text)

    #clean the draw number removed from list, stripped then converted to int
    x = mega_millions[0]
    clean = x.strip("Draw #")
    mega_millions[0] = int(clean)

    #clean the date and time remove from list, cleaned then converted to string
    clean = mega_millions[1][5:]
    #print(type(clean))
    mega_millions[1] = clean
    #print(type(fantasy5[0]))   

    # get the winning numbers
    spans = divs.find_all('span')
    for span in spans:
        mega_millions.append(int(span.text))
    print(mega_millions)
    # list ready for export to csv
    # draw number, date, winning numbers
    return mega_millions
