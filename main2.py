import time
import csv
from main_parser_class import FaceBookParser
from bs4 import BeautifulSoup
import os


if not os.path.exists('media'):
    os.mkdir('media')

if not os.path.exists('results'):
    os.mkdir('results')

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'

d1 = FaceBookParser()

d1.driver.get('https://www.facebook.com/ads/library')
input('Вы можете зарегистрироваться в facebook аккаунте, затем нажмите Enter')

TIME_NOW = str(time.time()).split(".")[0]


def get_links_from_socs(socs_name, current_socs):
    if socs_name is None:
        return ''

    if 'facebook' in socs_name and current_socs == 'facebook':
        return 'https://spytool.ru/facebook.png'

    if 'instagram' in socs_name and current_socs == 'instagram':
        return 'https://spytool.ru/instagram.png'

    if 'audience' in socs_name and current_socs == 'audience':
        return 'https://spytool.ru/audience_network.png'

    if 'messenger' in socs_name and current_socs == 'messenger':
        return 'https://spytool.ru/messenger.jpg'

    return ''


def save_in_scv(row):
    with open(f'results/main{TIME_NOW}.csv', 'a', encoding='utf-8') as file:
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
    'fb_link',
    'product_image_link',
    'product_image2_link',
    'product_image3_link',
    'product_image4_link',
    'product_video_link',
    'price',
    'lang',
    'data1',
    'data2',
    'facebook1',
    'instagram1',
    'audience1',
    'messenger1',
    'lead_form',
    'lead_form_link',
    'teaser2'
)
save_in_scv(start_row)


def get_all_cards_from_page(key_word):

    URL = f'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q={key_word}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all'

    d1.driver.get(URL)
    time.sleep(5)
    d1.scroll_page()

    CardsData = []
    CARD_NUMBER = 0

    not_end_flag = True
    while True:
        beautiful_soup_cards = d1.get_cards_by_beautiful_soup()
        if len(beautiful_soup_cards) <= CARD_NUMBER:
            print(f'Все карточки получены ({CARD_NUMBER} шт.) {len(beautiful_soup_cards)}')
            if not_end_flag:
                d1.scroll_page()
                not_end_flag = False
                continue
            else:
                break
        else:
            not_end_flag = True

        counter_ = 0
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
                    card_info1['fb_link'],
                    card_info1['product_image_link'],
                    card_info1['product_image2_link'],
                    card_info1['product_image3_link'],
                    card_info1['product_image4_link'],
                    card_info1['product_video_link'],
                    '',
                    '',
                    '',
                    '',
                    get_links_from_socs(card_info1['socs'], 'facebook'),
                    get_links_from_socs(card_info1['socs'], 'instagram'),
                    get_links_from_socs(card_info1['socs'], 'audience'),
                    get_links_from_socs(card_info1['socs'], 'messenger'),
                    '',
                    '',
                    ''
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
            counter_ += 1
            if counter_ >= 30:
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



