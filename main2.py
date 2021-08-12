import time
import csv
from main_parser_class import FaceBookParser
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'

d1 = FaceBookParser(USER_AGENT)


def get_all_cards_from_page(key_word):

    URL = f'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q={key_word}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all'

    d1.driver.get(URL)
    time.sleep(5)
    d1.scroll_page()
    TIME_NOW = str(time.time()).split(".")[0]

    def save_in_scv(row):
        with open(f'results/{key_word}{TIME_NOW}.csv', 'a', encoding='utf-8') as file:
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
        'knopka',
        'product_image_link',
        'product_image2_link',
        'product_image3_link',
        'product_image4_link',
        'product_video_link'
    )
    save_in_scv(start_row)

    CardsData = []
    CARD_NUMBER = 0

    # for i1 in range(1):
    while True:
        beautiful_soup_cards = d1.get_cards_by_beautiful_soup()
        if len(beautiful_soup_cards) <= CARD_NUMBER:
            print(f'Все карточки получены ({CARD_NUMBER} шт.)')
            break

        for i in range(CARD_NUMBER, len(beautiful_soup_cards)):
            try:
                card_info1 = d1.get_all_info_from_card(beautiful_soup_cards[CARD_NUMBER])
                if card_info1 is None:
                    print('Пустая карточка')
                    raise Exception

                # запись в .csv
                work_row = (
                    card_info1['zapusk'],
                    card_info1['fb_id'],
                    card_info1['product_name'],
                    card_info1['socs'],
                    card_info1['fb_ava'],
                    card_info1['link'],
                    card_info1['opis'],
                    card_info1['knopka'],
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
            print('-' * 100)
            print(f'Card: {CARD_NUMBER}')
            print(card_info1)
            print('-' * 100)
            # максимум 30 карточек в 1 прокрутку
            if i - CARD_NUMBER >= 30:
                print('many cards')
                break

        print('Next page/')
        d1.scroll_page()


# получение ключевых слов
with open('key_words.txt', 'r', encoding='utf-8') as file:
    list_of_key_words = file.readlines()
    list_of_key_words = [i.strip() for i in list_of_key_words if not i.strip() == '']
    print('Список слов для парсинга:', list_of_key_words)


for i in range(len(list_of_key_words)):
    key_word = list_of_key_words[i]

    print('-'*100)
    print('-'*100)
    print(f'Парсинг ключевого слова: "{key_word}"')
    print('-'*100)
    print('-'*100)
    get_all_cards_from_page(key_word)



