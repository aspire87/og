import pyperclip
import random
import sys
import os
import win32com.client as win32
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
from functi import convert as mac_conv
from gui import Ui_MainWindow
from dialog_repair_gui import Ui_OtherWindow


class App(QtWidgets.QMainWindow):

    def openwindow(self):
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def __init__(self):
        super(App, self).__init__()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonclear_common.clicked.connect(self.buttonclear_common)
        self.ui.checkboxklass_common.clicked.connect(self.checkboxklass_choose)
        self.ui.checkboxott_common.clicked.connect(self.checkboxott_choose)
        self.ui.checkboxinterop_common.clicked.connect(self.checkboxinterop_choose)
        self.ui.checkboxssid2yes_common.clicked.connect(self.ssid2yes_choose)
        self.ui.checkboxssid2no_common.clicked.connect(self.ssid2no_choose)
        self.ui.checkboxssid5yes_common.clicked.connect(self.ssid5yes_choose)
        self.ui.checkboxssid5no_common.clicked.connect(self.ssid5no_choose)
        self.ui.genpassent2_common.clicked.connect(self.pass_ssid2_generate)
        self.ui.genpassent5_common.clicked.connect(self.pass_ssid5_generate)
        self.ui.genpasslk_common.clicked.connect(self.pass_lk_generate)
        self.ui.createdomen_common.clicked.connect(self.create_domen)
        self.ui.createportal_common.clicked.connect(self.create_portal)
        self.ui.oblast_common.currentTextChanged.connect(self.autofill)
        self.ui.buttonmp_common.clicked.connect(self.sendmail_mp)
        self.ui.buttonmac_common.clicked.connect(self.macconvert_common)
        self.ui.buttonotchet_common.clicked.connect(self.formotchet_common)
        self.ui.buttonrepair_common.clicked.connect(self.openwindow)
        self.ui.buttonsave_common.clicked.connect(self.save_data)

    def formotchet_common(self):
        zakaz = self.ui.zakaz_common.text()
        klient = self.ui.klient_common.text()
        mrf = self.ui.mrf_common.text()
        gorod = self.ui.gorod_common.text()
        city = self.ui.city_common.text()
        ulica = self.ui.ulica_common.text()
        dom = self.ui.dom_common.text()
        td = self.ui.td_common.text()
        mac = self.ui.mac_common.toPlainText()
        cms = self.ui.cms_common.currentText()
        if zakaz == '':
            QMessageBox.about(self, 'Ошибка', 'Введите номер заказа')
            if QMessageBox.Ok:
                self.ui.zakaz_common.setFocus()
        elif klient == '':
            QMessageBox.about(self, 'Ошибка', 'Введите наименование клиента')
            if QMessageBox.Ok:
                self.ui.klient_common.setFocus()
        elif mrf == '':
            QMessageBox.about(self, 'Ошибка', 'Введите номер МРФ')
            if QMessageBox.Ok:
                self.ui.mrf_common.setFocus()
        elif gorod == '':
            QMessageBox.about(self, 'Ошибка', 'Введите обл. центр')
            if QMessageBox.Ok:
                self.ui.gorod_common.setFocus()
        elif city == '':
            QMessageBox.about(self, 'Ошибка', 'Введите населенный пункт')
            if QMessageBox.Ok:
                self.ui.city_common.setFocus()
        elif ulica == '':
            QMessageBox.about(self, 'Ошибка', 'Введите улицу')
            if QMessageBox.Ok:
                self.ui.ulica_common.setFocus()
        elif dom == '':
            QMessageBox.about(self, 'Ошибка', 'Введите номер дома')
            if QMessageBox.Ok:
                self.ui.dom_common.setFocus()
        elif td == '':
            QMessageBox.about(self, 'Ошибка', 'Введите количество ТД')
            if QMessageBox.Ok:
                self.ui.td_common.setFocus()
        elif mac == '':
            QMessageBox.about(self, 'Ошибка', 'Введите MAC-адреса')
            if QMessageBox.Ok:
                self.ui.mac_common.setFocus()
        elif cms == '':
            QMessageBox.about(self, 'Ошибка', 'Выберите статус заказа')
            if QMessageBox.Ok:
                self.ui.cms_common.setFocus()
        else:
            if gorod == city:
                addr = [klient, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz]
            else:
                addr = [klient, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz]

    def macconvert_common(self):
        maclist = self.ui.mac_common.toPlainText().split('\n')
        maclist = map(mac_conv, maclist)
        self.ui.mac_common.setText('\n'.join(maclist))

    def sendmail_mp(self):
        sside5 = self.ui.sside5_common.text()
        sside2 = self.ui.sside2_common.text()
        pwde5 = self.ui.passent5_common.text()
        pwde2 = self.ui.passent2_common.text()
        uzsside2 = self.ui.uzsside2_common.text()
        uzsside5 = self.ui.uzsside5_common.text()
        uzlk = self.ui.uzlk_common.text()
        passlk = self.ui.passlk_common.text()
        zagolovoklk = 'Вам предоставлен доступ в ЛК платформы Eltex:' + '\n' + 'https://lk.wifi.rt.ru/wifi-cab' + '\n' + '\n' + \
                      'Логин/пароль: ' + uzlk + '/' + passlk
        if len(sside5) > 0:
            zagolovokssid = 'Данные для подключения к закрытой сети 2.4 GHz ' + sside2 + ' : ' + uzsside2 + '/' + pwde2 + '\n' + \
                            'Данные для подключения к закрытой сети 5GHz ' + sside5 + ' : ' + uzsside5 + '/' + pwde5
        else:
            zagolovokssid = 'Данные для подключения к закрытой сети 2.4 GHz ' + sside2 + ' : ' + uzsside2 + '/' + pwde2
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = self.ui.pochtamp_common.text()
        mail.Subject = 'УЗ для ЛК по № ' + self.ui.zakaz_common.text()
        mail.Body = zagolovoklk + '\n' + '\n' + zagolovokssid
        mail.Display(True)

    def autofill(self):
        dictmrf = {'Алтайский край': ['Барнаул', '22', 'Сибирь'],
                   'Амурская область': ['Благовещенск', '28', 'ДВ'],
                   'Архангельская область': ['Архангельск', '29', 'СЗ'],
                   'Астраханская область': ['Астрахань', '30', 'Юг'],
                   'Белгородская область': ['Белгород', '31', 'Центр'],
                   'Брянская область': ['Брянск', '32', 'Центр'],
                   'Владимирская область': ['Владимир', '33', 'Центр'],
                   'Волгоградская область': ['Волгоград', '34', 'Юг'],
                   'Вологодская область': ['Вологда', '35', 'СЗ'],
                   'Воронежская область': ['Воронеж', '36', 'Центр'],
                   'Город Москва': ['Москва', '77', 'Центр'],
                   'Город Санкт-Петербург': ['Санкт-Петербург', '78', 'СЗ'],
                   'Еврейская автономная область': ['Биробиджан', '79', 'ДВ'],
                   'Забайкальский край': ['Чита', '75', 'Сибирь'],
                   'Ивановская область': ['Иваново', '37', 'Центр'],
                   'Иркутская область': ['Иркутск', '38', 'Сибирь'],
                   'Кабардино-Балкарская Республика': ['Нальчик', '7', 'Юг'],
                   'Калининградская область': ['Калининград', '39', 'СЗ'],
                   'Калужская область': ['Калуга', '40', 'Центр'],
                   'Камчатский край': ['Петропавловск-Камчатский', '41', 'ДВ'],
                   'Карачаево-Черкесская Республика': ['Черкесск', '9', 'Юг'],
                   'Кемеровская область': ['Кемерово', '42', 'Сибирь'],
                   'Кировская область': ['Киров', '43', 'Волга'],
                   'Костромская область': ['Кострома', '44', 'Центр'],
                   'Краснодарский край': ['Краснодар', '23', 'Юг'],
                   'Красноярский край': ['Красноярск', '24', 'Сибирь'],
                   'Курганская область': ['Курган', '45', 'Урал'],
                   'Курская область': ['Курск', '46', 'Центр'],
                   'Ленинградская область': ['Санкт-Петербург', '47', 'СЗ'],
                   'Липецкая область': ['Липецк', '48', 'Центр'],
                   'Магаданская область': ['Магадан', '49', 'ДВ'],
                   'Московская область': ['Красногорск, Москва', '50', 'Центр'],
                   'Мурманская область': ['Мурманск', '51', 'СЗ'],
                   'Ненецкий автономный округ': ['Нарьян-Мар', '83', 'СЗ'],
                   'Нижегородская область': ['Нижний Новгород', '52', 'Волга'],
                   'Новгородская область': ['Великий Новгород', '53', 'СЗ'],
                   'Новосибирская область': ['Новосибирск', '54', 'Сибирь'],
                   'Омская область': ['Омск', '55', 'Сибирь'],
                   'Оренбургская область': ['Оренбург', '56', 'Волга'],
                   'Орловская область': ['Орёл', '57', 'Центр'],
                   'Пензенская область': ['Пенза', '58', 'Волга'],
                   'Пермский край': ['Пермь', '59', 'Урал'],
                   'Приморский край': ['Владивосток', '25', 'ДВ'],
                   'Псковская область': ['Псков', '60', 'СЗ'],
                   'Республика Адыгея': ['Майкоп', '1', 'Юг'],
                   'Республика Алтай': ['Горно-Алтайск', '4', 'Сибирь'],
                   'Республика Башкортостан': ['Уфа', '2', 'Волга'],
                   'Республика Бурятия': ['Улан-Удэ', '3', 'Сибирь'],
                   'Республика Дагестан': ['Махачкала', '5', 'Юг'],
                   'Республика Ингушетия': ['Магас', '6', 'Юг'],
                   'Республика Калмыкия': ['Элиста', '8', 'Юг'],
                   'Республика Карелия': ['Петрозаводск', '10', 'СЗ'],
                   'Республика Коми': ['Сыктывкар', '11', 'СЗ'],
                   'Республика Марий Эл': ['Йошкар-Ола', '12', 'Волга'],
                   'Республика Мордовия': ['Саранск', '13', 'Волга'],
                   'Республика Саха': ['Якутск', '14', 'ДВ'],
                   'Республика Северная Осетия - Алания': ['Владикавказ', '15', 'Юг'],
                   'Республика Татарстан': ['Казань', '16', 'Волга'],
                   'Республика Тыва': ['Кызыл', '17', 'Сибирь'],
                   'Республика Хакасия': ['Абакан', '19', 'Сибирь'],
                   'Ростовская область': ['Ростов-на-Дону', '61', 'Юг'],
                   'Рязанская область': ['Рязань', '62', 'Центр'],
                   'Самарская область': ['Самара', '63', 'Волга'],
                   'Саратовская область': ['Саратов', '64', 'Волга'],
                   'Сахалинская область': ['Южно-Сахалинск', '65', 'ДВ'],
                   'Свердловская область': ['Екатеринбург', '66', 'Урал'],
                   'Смоленская область': ['Смоленск', '67', 'Центр'],
                   'Ставропольский край': ['Ставрополь', '26', 'Юг'],
                   'Тамбовская область': ['Тамбов', '68', 'Центр'],
                   'Тверская область': ['Тверь', '69', 'Центр'],
                   'Томская область': ['Томск', '70', 'Сибирь'],
                   'Тульская область': ['Тула', '71', 'Центр'],
                   'Тюменская область': ['Тюмень', '72', 'Урал'],
                   'Удмуртская республика': ['Ижевск', '18', 'Волга'],
                   'Ульяновская область': ['Ульяновск', '73', 'Волга'],
                   'Хабаровский край': ['Хабаровск', '27', 'ДВ'],
                   'ХМАО': ['Ханты-Мансийск', '86', 'Урал'],
                   'Челябинская область': ['Челябинск', '74', 'Урал'],
                   'Чувашская Республика': ['Чебоксары', '21', 'Волга'],
                   'Чукотский автономный округ': ['Анадырь', '87', 'ДВ'],
                   'Ямало-Ненецкий автономный округ': ['Салехард', '89', 'Урал'],
                   'Ярославская область': ['Ярославль', '76', 'Центр']}
        text = self.ui.oblast_common.currentText()
        if dictmrf.get(text) is None:
            pass
        else:
            self.ui.gorod_common.setText(dictmrf.get(text)[0])
            self.ui.region_common.setText(dictmrf.get(text)[1])
            self.ui.mrf_common.setText(dictmrf.get(text)[2])

    def buttonclear_common(self):
        self.ui.checkboxklass_common.setChecked(False)
        self.ui.checkboxklass_common.setDisabled(False)
        self.ui.checkboxott_common.setChecked(False)
        self.ui.checkboxott_common.setDisabled(False)
        self.ui.checkboxinterop_common.setChecked(False)
        self.ui.checkboxinterop_common.setDisabled(False)
        self.ui.checkboxesia_common.setChecked(False)
        self.ui.checkboxesia_common.setDisabled(False)
        self.ui.checkboxsms_common.setChecked(False)
        self.ui.checkboxsms_common.setDisabled(False)
        self.ui.checkboxzvonok_common.setChecked(False)
        self.ui.checkboxzvonok_common.setDisabled(False)
        self.ui.checkboxssid2no_common.setChecked(False)
        self.ui.checkboxssid2no_common.setDisabled(False)
        self.ui.checkboxssid2yes_common.setChecked(False)
        self.ui.checkboxssid2yes_common.setDisabled(False)
        self.ui.checkboxssid5no_common.setChecked(False)
        self.ui.checkboxssid5no_common.setDisabled(False)
        self.ui.checkboxssid5yes_common.setChecked(False)
        self.ui.checkboxssid5yes_common.setDisabled(False)
        self.ui.checkboxsside2no_common.setChecked(False)
        self.ui.checkboxsside2no_common.setDisabled(False)
        self.ui.checkboxsside2yes_common.setChecked(False)
        self.ui.checkboxsside2yes_common.setDisabled(False)
        self.ui.checkboxsside5no_common.setChecked(False)
        self.ui.checkboxsside5no_common.setDisabled(False)
        self.ui.checkboxsside5yes_common.setChecked(False)
        self.ui.checkboxsside5yes_common.setDisabled(False)
        self.ui.checkboxlkyes_common.setChecked(False)
        self.ui.checkboxlkyes_common.setDisabled(False)
        self.ui.checkboxlkno_common.setChecked(False)
        self.ui.checkboxlkno_common.setDisabled(False)

    def checkboxklass_choose(self):
        if self.ui.checkboxklass_common.isChecked():
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(True)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(True)
        else:
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(False)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(False)

    def checkboxott_choose(self):
        if self.ui.checkboxott_common.isChecked():
            self.ui.checkboxklass_common.setChecked(False)
            self.ui.checkboxklass_common.setDisabled(True)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(True)
        else:
            self.ui.checkboxklass_common.setChecked(False)
            self.ui.checkboxklass_common.setDisabled(False)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(False)

    def checkboxinterop_choose(self):
        if self.ui.checkboxinterop_common.isChecked():
            self.ui.checkboxklass_common.setChecked(False)
            self.ui.checkboxklass_common.setDisabled(True)
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(True)
            self.ui.tarif_common.setText("INTERNET")
        else:
            self.ui.checkboxklass_common.setChecked(False)
            self.ui.checkboxklass_common.setDisabled(False)
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(False)

    def ssid2yes_choose(self):
        if self.ui.checkboxssid2yes_common.isChecked():
            self.ui.checkboxssid2no_common.setChecked(False)
            self.ui.checkboxssid2no_common.setDisabled(True)
            self.ui.ssid2_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)
        else:
            self.ui.checkboxssid2no_common.setDisabled(False)

    def ssid2no_choose(self):
        if self.ui.checkboxssid2no_common.isChecked():
            self.ui.checkboxssid2yes_common.setChecked(False)
            self.ui.checkboxssid2yes_common.setDisabled(True)
            self.ui.ssid2_common.setDisabled(True)
            self.ui.portal_common.setDisabled(True)
        else:
            self.ui.checkboxssid2yes_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)
            self.ui.ssid2_common.setDisabled(False)

    def ssid5yes_choose(self):
        if self.ui.checkboxssid5yes_common.isChecked():
            self.ui.checkboxssid5no_common.setChecked(False)
            self.ui.checkboxssid5no_common.setDisabled(True)
            self.ui.ssid5_common.setDisabled(False)
        else:
            self.ui.checkboxssid5no_common.setDisabled(False)
            self.ui.ssid5_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)

    def ssid5no_choose(self):
        if self.ui.checkboxssid5no_common.isChecked():
            self.ui.checkboxssid5yes_common.setChecked(False)
            self.ui.checkboxssid5yes_common.setDisabled(True)
            self.ui.ssid5_common.setDisabled(True)
            self.ui.portal_common.setDisabled(True)
        else:
            self.ui.checkboxssid5yes_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)
            self.ui.ssid5_common.setDisabled(False)

    def pass_ssid2_generate(self):
        password = ''
        length = 4
        chars = '1234567890'
        for i in range(length):
            password += random.choice(chars)
        self.ui.passent2_common.setText(password)

    def pass_ssid5_generate(self):
        password = ''
        length = 4
        chars = '1234567890'
        for i in range(length):
            password += random.choice(chars)
        self.ui.passent5_common.setText(password)

    def pass_lk_generate(self):
        password = ''
        length = 6
        chars = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(length):
            password += random.choice(chars)
        self.ui.passlk_common.setText(password)

    def create_domen(self):
        capital_letters = {u'А': u'A',
                           u'Б': u'B',
                           u'В': u'V',
                           u'Г': u'G',
                           u'Д': u'D',
                           u'Е': u'E',
                           u'Ё': u'E',
                           u'Ж': u'Zh',
                           u'З': u'Z',
                           u'И': u'I',
                           u'Й': u'Y',
                           u'К': u'K',
                           u'Л': u'L',
                           u'М': u'M',
                           u'Н': u'N',
                           u'О': u'O',
                           u'П': u'P',
                           u'Р': u'R',
                           u'С': u'S',
                           u'Т': u'T',
                           u'У': u'U',
                           u'Ф': u'F',
                           u'Х': u'H',
                           u'Ц': u'C',
                           u'Ч': u'Ch',
                           u'Ш': u'Sh',
                           u'Щ': u'Sh',
                           u'Ъ': u'',
                           u'Ы': u'Y',
                           u'Ь': u'',
                           u'Э': u'E',
                           u'Ю': u'U',
                           u'Я': u'Ya', }

        lower_case_letters = {u'а': u'a',
                              u'б': u'b',
                              u'в': u'v',
                              u'г': u'g',
                              u'д': u'd',
                              u'е': u'e',
                              u'ё': u'e',
                              u'ж': u'zh',
                              u'з': u'z',
                              u'и': u'i',
                              u'й': u'y',
                              u'к': u'k',
                              u'л': u'l',
                              u'м': u'm',
                              u'н': u'n',
                              u'о': u'o',
                              u'п': u'p',
                              u'р': u'r',
                              u'с': u's',
                              u'т': u't',
                              u'у': u'u',
                              u'ф': u'f',
                              u'х': u'h',
                              u'ц': u'c',
                              u'ч': u'ch',
                              u'ш': u'sh',
                              u'щ': u'sh',
                              u'ъ': u'',
                              u'ы': u'y',
                              u'ь': u'',
                              u'э': u'e',
                              u'ю': u'u',
                              u'я': u'ya', }

        k = self.ui.klientsoc_common.text()
        u = self.ui.ulica_common.text()
        d = self.ui.dom_common.text()
        translit_domen = k + '_' + u + '_' + d
        translit_string = ""
        for index, char in enumerate(translit_domen):
            if char in lower_case_letters.keys():
                char = lower_case_letters[char]
            elif char in capital_letters.keys():
                char = capital_letters[char]
                if len(translit_domen) > index + 1:
                    if translit_domen[index + 1] not in lower_case_letters.keys():
                        char = char.upper()
                else:
                    char = char.upper()
            translit_string += char

        self.ui.domen_common.setText(translit_string)

    def create_portal(self):
        capital_letters = {u'А': u'A',
                           u'Б': u'B',
                           u'В': u'V',
                           u'Г': u'G',
                           u'Д': u'D',
                           u'Е': u'E',
                           u'Ё': u'E',
                           u'Ж': u'Zh',
                           u'З': u'Z',
                           u'И': u'I',
                           u'Й': u'Y',
                           u'К': u'K',
                           u'Л': u'L',
                           u'М': u'M',
                           u'Н': u'N',
                           u'О': u'O',
                           u'П': u'P',
                           u'Р': u'R',
                           u'С': u'S',
                           u'Т': u'T',
                           u'У': u'U',
                           u'Ф': u'F',
                           u'Х': u'H',
                           u'Ц': u'C',
                           u'Ч': u'Ch',
                           u'Ш': u'Sh',
                           u'Щ': u'Sh',
                           u'Ъ': u'',
                           u'Ы': u'Y',
                           u'Ь': u'',
                           u'Э': u'E',
                           u'Ю': u'U',
                           u'Я': u'Ya', }

        lower_case_letters = {u'а': u'a',
                              u'б': u'b',
                              u'в': u'v',
                              u'г': u'g',
                              u'д': u'd',
                              u'е': u'e',
                              u'ё': u'e',
                              u'ж': u'zh',
                              u'з': u'z',
                              u'и': u'i',
                              u'й': u'y',
                              u'к': u'k',
                              u'л': u'l',
                              u'м': u'm',
                              u'н': u'n',
                              u'о': u'o',
                              u'п': u'p',
                              u'р': u'r',
                              u'с': u's',
                              u'т': u't',
                              u'у': u'u',
                              u'ф': u'f',
                              u'х': u'h',
                              u'ц': u'c',
                              u'ч': u'ch',
                              u'ш': u'sh',
                              u'щ': u'sh',
                              u'ъ': u'',
                              u'ы': u'y',
                              u'ь': u'',
                              u'э': u'e',
                              u'ю': u'u',
                              u'я': u'ya', }

        m = self.ui.mrf_common.text()
        c = self.ui.city_common.text()
        k = self.ui.klientsoc_common.text()
        translit_string = ""
        if self.ui.checkboxott_common.isChecked():
            translit_portal = m + '_' + c + '_' + k + '_ОТТ'
        elif self.ui.checkboxinterop_common.isChecked():
            translit_portal = m + '_' + c + '_' + k + '_ESR10'
        else:
            translit_portal = m + '_' + c + '_' + k

        for index, char in enumerate(translit_portal):
            if char in lower_case_letters.keys():
                char = lower_case_letters[char]
            elif char in capital_letters.keys():
                char = capital_letters[char]
                if len(translit_portal) > index + 1:
                    if translit_portal[index + 1] not in lower_case_letters.keys():
                        char = char.upper()
                else:
                    char = char.upper()
            translit_string += char

        self.ui.portal_common.setText(translit_string)

    def save_data(self):
        list = [
                self.ui.zakaz_common.text(),
                self.ui.klient_common.text(),
                self.ui.klientsoc_common.text(),
                self.ui.address_common.text(),
                self.ui.oblast_common.currentText(),
                self.ui.gorod_common.text(),
                self.ui.city_common.text(),
                self.ui.ulica_common.text(),
                self.ui.dom_common.text(),
                self.ui.region_common.text(),
                self.ui.inn_common.text(),
                self.ui.kl_common.text(),
                self.ui.telkl_common.text(),
                self.ui.mailkl_common.text(),
                self.ui.mac_common.toPlainText(),
                self.ui.domen_common.text(),
                self.ui.tarif_common.text(),
                self.ui.checkboxklass_common.checkState(),
                self.ui.checkboxott_common.checkState(),
                self.ui.checkboxinterop_common.checkState(),
                self.ui.ssid2_common.text(),
                self.ui.checkboxssid2yes_common.checkState(),
                self.ui.checkboxssid2no_common.checkState(),
                self.ui.ssid5_common.text(),
                self.ui.checkboxssid5yes_common.checkState(),
                self.ui.checkboxssid5no_common.checkState(),
                self.ui.checkboxsms_common.checkState(),
                self.ui.checkboxesia_common.checkState(),
                self.ui.checkboxzvonok_common.checkState(),
                self.ui.portal_common.text(),
                self.ui.redirect_common.text(),
                self.ui.sside2_common.text(),
                self.ui.checkboxsside2yes_common.checkState(),
                self.ui.checkboxsside2no_common.checkState(),
                self.ui.sside5_common.text(),
                self.ui.checkboxsside5yes_common.checkState(),
                self.ui.checkboxsside5no_common.checkState(),
                self.ui.uzsside2_common.text(),
                self.ui.passent2_common.text(),
                self.ui.uzsside5_common.text(),
                self.ui.passent5_common.text(),
                self.ui.checkboxlkyes_common.checkState(),
                self.ui.checkboxlkno_common.checkState(),
                self.ui.uzlk_common.text(),
                self.ui.passlk_common.text(),
                self.ui.pochtamp_common.text(),
                self.ui.mrf_common.text(),
                self.ui.cms_common.currentText()
                ]
        nowdate = datetime.datetime.today().strftime("%d-%m-%Y")
        with open(nowdate + ".txt", "a") as file:
            lines = ('|').join(list) + '\n'
            file.writelines(list)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.show()

    sys.exit(app.exec())
