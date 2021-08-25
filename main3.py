import time
import csv
from main_parser_class import FaceBookParser
from bs4 import BeautifulSoup
import os

TIME_NOW = str(time.time()).split(".")[0]

d1 = FaceBookParser()
#
# d1.driver.get('https://www.facebook.com/ads/library')
# input('Вы можете зарегистрироваться в facebook аккаунте, затем нажмите Enter')


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


def create_start_scv():
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


def save_all_cards(cards):
    number_of_cards = len(cards)
    print(f'Начинается загрузка {number_of_cards} карточек')
    time.sleep(2)
    for i in range(number_of_cards):
        try:
            card_info1 = cards[i]
            card_info1 = d1.get_all_info_from_card(card_info1)
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
            print(f'Карточка {i} пропущена')
            continue

        print('-' * 100)
        print(f'Card: {i}/{number_of_cards}')
        print(work_row)
        print('-' * 100)


if __name__ == '__main__':
    # получение ключевых слов
    with open('key_words.txt', 'r', encoding='utf-8') as file:
        list_of_key_words = file.readlines()
        list_of_key_words = [i.strip() for i in list_of_key_words if not i.strip() == '']
        print('Список слов для парсинга:', list_of_key_words)

    # создание директорий
    if not os.path.exists('media'):
        os.mkdir('media')
    if not os.path.exists('results'):
        os.mkdir('results')

    # создаём таблицу
    create_start_scv()

    for key_word in list_of_key_words:

        d1.go_to_page(key_word)
        cards = d1.infinity_scroll2()
        save_all_cards(cards)

        print(f'Для ключевого слова {key_word} загружено {len(cards)} карточек')
        time.sleep(4)
        d1.driver.get('https://2ip.ru')
        time.sleep(5)





