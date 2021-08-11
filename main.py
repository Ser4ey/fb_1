import time

from main_parser_class import FaceBookParser
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'

URL = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=%D0%B1%D0%BE%D1%82%D0%BE%D0%BA%D1%81&search_type=keyword_unordered&media_type=all'

CardsData = []
CARD_NUMBER = 0

d1 = FaceBookParser(USER_AGENT)
d1.driver.get(URL)
time.sleep(5)


for i1 in range(3):
# while True:
    beautiful_soup_cards = d1.get_cards_by_beautiful_soup()
    # selenium_cards = d1.get_cards_by_selenium()
    if len(beautiful_soup_cards) <= CARD_NUMBER:
        print(f'Все карточки получены ({CARD_NUMBER} шт.)')
        break

    for i in range(CARD_NUMBER, len(beautiful_soup_cards)):
        try:
            card_info1 = d1.get_all_info_from_card(beautiful_soup_cards[CARD_NUMBER])
            # card_info2_inst_account = d1.get_instagram_account_full(selenium_cards[CARD_NUMBER])
        except:
            CARD_NUMBER += 1
            print(f'Карточка {CARD_NUMBER} пропущена')
            continue
        CARD_NUMBER += 1
        print('-'*100)
        print(f'Card: {CARD_NUMBER}')
        print(card_info1)
        print('-'*100)

    # time.sleep(3)
    print('Next page/')
    d1.scroll_page()
    # time.sleep(3)
    # print(f'Page {i1+1} done')

# d1.driver.find_element_by_class_name('_3-8k').click()
# time.sleep(5)
#
# page_source = d1.driver.page_source
#

# for i in range(1):
#     cards, number_of_cards = d1.get_cards_by_selenium()
#     print(f'Собрано карточек: {number_of_cards}')
#     # d1.scroll_page()
#
# for i in range(len(cards)):
#     print(f'Card: {i+1}')
#     d1.open_card(cards[i])
#     inst1 = d1.get_instagram_account_from_card_page()
#     # time.sleep(1)
#     d1.return_to_main_page()
#
# d1.open_card(cards[2])
# inst1 = d1.get_instagram_account_from_card_page()



# d1.return_to_main_page()
# soup = BeautifulSoup(page_source, 'lxml')
#
# card = soup.find('div', class_='_99s5')
# print(card)
# time.sleep(5)
# print('-'*100)
# id = soup.find_all('div', class_='i0ppjblf e946d6ch')
# for i in id:
#     print(i, i.text)

