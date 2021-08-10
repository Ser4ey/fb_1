import csv
import os
import pickle
import threading
import pyautogui
import selenium
from selenium import webdriver
import time
import data
from bs4 import BeautifulSoup

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# selenium.webdriver.common.keys


class FaceBookParser:
    def __init__(self, user_agent, firefox_profile='/home/ser4/.mozilla/firefox/8da9zz4w.default-release'):

        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        profile = webdriver.FirefoxProfile(firefox_profile)

        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("general.useragent.override", user_agent)

        driver = webdriver.Firefox(
            executable_path=data.path_to_geckodriver,
            firefox_binary=data.firefox_binary,
            capabilities=firefox_capabilities,
            options=options,
            firefox_profile=profile)

        self.driver = driver

    def infinity_scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        i = 0
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print('Страница полностью загружена')
                break
            else:
                last_height = new_height
                i += 1
                print(f'Прокрутка страницы...{i}')

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print('[+] Прокрутка страницы')
        time.sleep(10)

    def get_cards_by_selenium(self):
        cards = self.driver.find_elements_by_class_name('_99s5')

        if cards is None:
            print('[-] Не удалось найти карточки объявлений')
            return []
        return cards

    def get_cards_by_beautiful_soup(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        cards = soup.find_all('div', class_='_99s5')
        if cards is None:
            return []
        return cards

    def return_to_main_page(self):
        '''Нажатие на кнопку "Результаты поиска"
            (Возвращение на главную страницу с карточками)
        '''
        main_class = 'aoikulk7'
        next_class = 'abf56d1w'

        el1 = self.driver.find_elements_by_class_name(main_class)[-1]
        el1.find_element_by_class_name(next_class).click()
        time.sleep(1)


    @staticmethod
    def open_card(card):
        card.find_element_by_class_name('_3-8k').click()

    def get_instagram_account_from_card_page(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        try:
            instagram_account_block = soup.find_all('span', class_='l61y9joe j8otv06s ippphs35 a1itoznt te7ihjl9 svz86pwt a53abz89')[-1]
            instagram_account_name = instagram_account_block.find('div', class_='i0ppjblf e946d6ch').text
            # print(f'Instagram account: {instagram_account_name}')
            return instagram_account_name
        except Exception as er:
            print('[-] Ошибка при получении имени инстаграмм аккаунта')
            print(er)
            return 'Нет инстаграмм аккаунта'

    def get_instagram_account_full(self, card):
        self.open_card(card)
        time.sleep(2.5)
        inst1 = self.get_instagram_account_from_card_page()
        if inst1 == 'Нет инстаграмм аккаунта':
            time.sleep(5)
            inst1 = self.get_instagram_account_from_card_page()

        self.return_to_main_page()

        return inst1


    @staticmethod
    def get_all_info_from_card(card):
        # page_source = self.driver.page_source
        # soup = BeautifulSoup(page_source, 'lxml')
        # card = soup.find('div', class_='_99s5')

        zapusk = 'Нет времени запуска'
        fb_id = 'Нет facebook id'
        try:
            block_with_date_and_facebook_id = card.find('div', class_='_7jvz')
            date_and_facebook_id = block_with_date_and_facebook_id.find_all('div', class_='_9cd3')

            # время запуска
            zapusk = date_and_facebook_id[0].text
            #facebook id
            fb_id = date_and_facebook_id[1].text
        except:
            pass
        # print(f'{zapusk} -- {fb_id}')


        dict_of_data = {
            'zapusk': zapusk,
            'fb_id': fb_id
        }

        return dict_of_data

    def close_session(self):
        self.driver.close()
        self.driver.quit()
