import time
import csv
from main_parser_class import FaceBookParser
from bs4 import BeautifulSoup

TIME_NOW = str(time.time()).split(".")[0]
def save_in_scv(row):
    with open(f'table{TIME_NOW}.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)

start_row = (
    'zapusk',
    'fb_id',
    'product_name',
    'socs',
    'fb_ava',
    'link',
    'opis',
    'product_image_link',
    'product_image2_link',
    'product_image3_link',
    'product_image4_link',
    'product_video_link'
)
save_in_scv(start_row)


USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'

URL = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=%D0%B1%D0%BE%D1%82%D0%BE%D0%BA%D1%81&search_type=keyword_unordered&media_type=all'

CardsData = []
CARD_NUMBER = 0

d1 = FaceBookParser(USER_AGENT)
d1.driver.get(URL)
time.sleep(5)
d1.scroll_page()

for i1 in range(1):
# while True:
    # print(i1)
    beautiful_soup_cards = d1.get_cards_by_beautiful_soup()
    if len(beautiful_soup_cards) <= CARD_NUMBER:
        print(f'Все карточки получены ({CARD_NUMBER} шт.)')
        break

    for i in range(CARD_NUMBER, len(beautiful_soup_cards)):
        try:
            card_info1 = d1.get_all_info_from_card(beautiful_soup_cards[CARD_NUMBER])

            # запись в .csv
            work_row = (
                card_info1['zapusk'],
                card_info1['fb_id'],
                card_info1['product_name'],
                card_info1['socs'],
                card_info1['fb_ava'],
                card_info1['link'],
                card_info1['opis'],
                card_info1['product_image_link'],
                card_info1['product_image2_link'],
                card_info1['product_image3_link'],
                card_info1['product_image4_link'],
                card_info1['product_video_link']
            )
            save_in_scv(work_row)
        except:
            CARD_NUMBER += 1
            print(f'Карточка {CARD_NUMBER} пропущена')
            continue
        CARD_NUMBER += 1
        print('-'*100)
        print(f'Card: {CARD_NUMBER}')
        print(card_info1)
        print('-'*100)
        # максимум 30 карточек в 1 прокрутку
        if i-CARD_NUMBER >= 30:
            print('many cards')
            break

    # time.sleep(3)
    print('Next page/')
    d1.scroll_page()


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

