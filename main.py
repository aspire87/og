import pyperclip
import random
import sys
import openpyxl
import win32com.client as win32
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
from functions import translit, autofill, Excel, convert
import datetime
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
        self.ui.checkboxklass_common.clicked.connect(self.klass_checked)
        self.ui.checkboxott_common.clicked.connect(self.checkboxott_choose)
        self.ui.checkboxinterop_common.clicked.connect(self.checkboxinterop_choose)
        self.ui.checkboxssid2yes_common.clicked.connect(self.ssid2yes_choose)
        self.ui.checkboxssid2no_common.clicked.connect(self.ssid2no_choose)
        self.ui.checkboxssid5yes_common.clicked.connect(self.ssid5yes_choose)
        self.ui.checkboxssid5no_common.clicked.connect(self.ssid5no_choose)
        self.ui.checkboxsside2yes_common.clicked.connect(self.sside2yes_choose)
        self.ui.checkboxsside2no_common.clicked.connect(self.sside2no_choose)
        self.ui.checkboxsside5yes_common.clicked.connect(self.sside5yes_choose)
        self.ui.checkboxsside5no_common.clicked.connect(self.sside5no_choose)
        self.ui.checkboxlkyes_common.clicked.connect(self.lkyes_choose)
        self.ui.checkboxlkno_common.clicked.connect(self.lkno_choose)
        self.ui.genpassent2_common.clicked.connect(self.pass_ssid2_generate)
        self.ui.genpassent5_common.clicked.connect(self.pass_ssid5_generate)
        self.ui.genpasslk_common.clicked.connect(self.pass_lk_generate)
        self.ui.createdomen_common.clicked.connect(self.create_domen_common)
        self.ui.createdomen_rrs.clicked.connect(self.create_domen_rrs)
        self.ui.createdomen_psb.clicked.connect(self.create_domen_psb)
        self.ui.createdomen_gpb.clicked.connect(self.create_domen_gpb)
        self.ui.createdomen_vtb.clicked.connect(self.create_domen_vtb)
        self.ui.createdomen_sber.clicked.connect(self.create_domen_sber)
        self.ui.createportal_common.clicked.connect(self.create_portal_comom)
        self.ui.oblast_common.currentTextChanged.connect(self.autofill_common)
        self.ui.oblast_rrs.currentTextChanged.connect(self.autofill_rrs)
        self.ui.oblast_psb.currentTextChanged.connect(self.autofill_psb)
        self.ui.oblast_gpb.currentTextChanged.connect(self.autofill_gpb)
        self.ui.oblast_vtb.currentTextChanged.connect(self.autofill_vtb)
        self.ui.oblast_sber.currentTextChanged.connect(self.autofill_sber)
        self.ui.buttonmp_common.clicked.connect(self.sendmail_mp)
        self.ui.buttonmac_common.clicked.connect(self.macconvert_common)
        self.ui.buttonmac_rrs.clicked.connect(self.macconvert_rrs)
        self.ui.buttonmac_psb.clicked.connect(self.macconvert_psb)
        self.ui.buttonmac_gpb.clicked.connect(self.macconvert_gpb)
        self.ui.buttonmac_vtb.clicked.connect(self.macconvert_vtb)
        self.ui.buttonmac_sber.clicked.connect(self.macconvert_sber)
        self.ui.buttonrepair_common.clicked.connect(self.openwindow)
        self.ui.buttonrepair_rrs.clicked.connect(self.openwindow)
        self.ui.buttonrepair_psb.clicked.connect(self.openwindow)
        self.ui.buttonrepair_gpb.clicked.connect(self.openwindow)
        self.ui.buttonrepair_vtb.clicked.connect(self.openwindow)
        self.ui.buttonrepair_sber.clicked.connect(self.openwindow)
        self.ui.buttonsave_common.clicked.connect(self.save_data_common)
        self.ui.gosb_sber.editingFinished.connect(self.pass_equs)
        self.ui.vsp_sber.editingFinished.connect(self.sside_sbrf)
        self.ui.vsp_sber.editingFinished.connect(self.pass_sside_sbrf)
        self.ui.buttonopis_common.clicked.connect(self.form_opis_common)
        self.ui.buttonopis_rrs.clicked.connect(self.form_opis_rrs)
        self.ui.buttonopis_psb.clicked.connect(self.form_opis_psb)
        self.ui.buttonopis_gpb.clicked.connect(self.form_opis_gpb)
        self.ui.buttonopis_vtb.clicked.connect(self.form_opis_vtb)
        self.ui.buttoncms_sber.clicked.connect(self.form_opis_sber)
        self.ui.buttoncms_common.clicked.connect(self.form_cms_common)
        self.ui.buttoncms_rrs.clicked.connect(self.form_cms_rrs)
        self.ui.buttoncms_psb.clicked.connect(self.form_cms_psb)
        self.ui.buttoncms_gpb.clicked.connect(self.form_cms_gpb)
        self.ui.buttoncms_vtb.clicked.connect(self.form_cms_vtb)
        self.ui.buttoncms_sber.clicked.connect(self.form_cms_sber)
        self.ui.buttonadd_common.clicked.connect(self.add_to_excel_common)
        self.ui.buttonadd_rrs.clicked.connect(self.add_to_excel_rrs)
        self.ui.buttonadd_psb.clicked.connect(self.add_to_excel_psb)
        self.ui.buttonadd_gpb.clicked.connect(self.add_to_excel_gpb)
        self.ui.buttonadd_vtb.clicked.connect(self.add_to_excel_vtb)
        self.ui.buttonadd_sber.clicked.connect(self.add_to_excel_sber)
        self.ui.otd_rrs.editingFinished.connect(self.form_ssid_rrs)
        self.ui.actionClose.triggered.connect(self.close)

    # Отправка отчета в скайп
    """def form_otchet_common(self):
        nowdate =datetime.datetime.today().strftime("%d.%m.%Y")
        filename = nowdate+'_Ульянов.xlsx'
        wb = openpyxl.load_workbook('template.xlsx')
        wb.save(filename)"""


    # Добавление строки в файл excel с заказами
    def add_to_excel_common(self):
        klient = self.ui.klient_common.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_common.text()
        gorod = self.ui.gorod_common.text()
        city = self.ui.city_common.text()
        ulica = self.ui.ulica_common.text()
        dom = self.ui.dom_common.text()
        td = self.ui.td_common.text()
        cms = self.ui.cms_common.currentText()
        zakaz = self.ui.zakaz_common.text()
        domen = self.ui.domen_common.text()
        mac = (', ').join(self.ui.mac_common.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    def add_to_excel_rrs(self):
        klient = self.ui.klient_rrs.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_rrs.text()
        gorod = self.ui.gorod_rrs.text()
        city = self.ui.city_rrs.text()
        ulica = self.ui.ulica_rrs.text()
        dom = self.ui.dom_rrs.text()
        td = self.ui.td_rrs.text()
        cms = self.ui.cms_rrs.currentText()
        zakaz = self.ui.zakaz_rrs.text()
        domen = self.ui.domen_rrs.text()
        mac = (', ').join(self.ui.mac_rrs.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    def add_to_excel_psb(self):
        klient = self.ui.klient_psb.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_psb.text()
        gorod = self.ui.gorod_psb.text()
        city = self.ui.city_psb.text()
        ulica = self.ui.ulica_psb.text()
        dom = self.ui.dom_psb.text()
        td = self.ui.td_psb.text()
        cms = self.ui.cms_psb.currentText()
        zakaz = self.ui.zakaz_psb.text()
        domen = self.ui.domen_psb.text()
        mac = (', ').join(self.ui.mac_psb.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    def add_to_excel_gpb(self):
        klient = self.ui.klient_gpb.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_gpb.text()
        gorod = self.ui.gorod_gpb.text()
        city = self.ui.city_gpb.text()
        ulica = self.ui.ulica_gpb.text()
        dom = self.ui.dom_gpb.text()
        td = self.ui.td_gpb.text()
        cms = self.ui.cms_gpb.currentText()
        zakaz = self.ui.zakaz_gpb.text()
        domen = self.ui.domen_gpb.text()
        mac = (', ').join(self.ui.mac_gpb.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    def add_to_excel_vtb(self):
        klient = self.ui.klient_vtb.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_vtb.text()
        gorod = self.ui.gorod_vtb.text()
        city = self.ui.city_vtb.text()
        ulica = self.ui.ulica_vtb.text()
        dom = self.ui.dom_vtb.text()
        td = self.ui.td_vtb.text()
        cms = self.ui.cms_vtb.currentText()
        zakaz = self.ui.zakaz_vtb.text()
        domen = self.ui.domen_vtb.text()
        mac = (', ').join(self.ui.mac_vtb.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    def add_to_excel_sber(self):
        klient = self.ui.klient_sber.text()
        nowdate = datetime.datetime.today().strftime('%d.%m.%Y')
        dateout = ''
        mrf = self.ui.mrf_sber.text()
        gorod = self.ui.gorod_sber.text()
        city = self.ui.city_sber.text()
        ulica = self.ui.ulica_sber.text()
        dom = self.ui.dom_sber.text()
        td = self.ui.td_sber.text()
        cms = self.ui.cms_sber.currentText()
        zakaz = self.ui.zakaz_sber.text()
        domen = self.ui.domen_sber.text()
        mac = (', ').join(self.ui.mac_sber.toPlainText().split('\n'))
        if str(gorod) == str(city):
            addr = [klient, nowdate, dateout, mrf, gorod, ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        else:
            addr = [klient, nowdate, dateout, mrf, gorod, city + ', ' + ulica + ', ' + dom, td, cms, zakaz, domen, mac]
        exc = Excel()
        exc.write_list(addr)

    # Формирование заметки  для CMS
    def form_cms_common(self):
        # zakaz = self.ui.zakaz_common.text()
        # klient = self.ui.klient_common.text()
        # address = self.ui.address_common.text()
        domen = self.ui.domen_common.text()
        tarif = self.ui.tarif_common.text()
        portal = self.ui.portal_common.text()
        ssid2 = self.ui.ssid2_common.text()
        sside2 = self.ui.sside2_common.text()
        ssid5 = self.ui.ssid5_common.text()
        sside5 = self.ui.sside5_common.text()
        # td = self.ui.td_common.text()
        mac = (', ').join(self.ui.mac_common.toPlainText().split('\n'))
        pochta = self.ui.pochtamp_common.text()
        # uzssid2 = self.ui.uzsside2_common.text()
        # uzssid5 = self.ui.uzsside5_common.text()
        # uzlk = self.ui.uzlk_common.text()
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(tarif) > 0:
            labeltarif = '\n' + 'Тариф: '
        else:
            labeltarif = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid2) > 0:
            labelssid2 = '\n' + 'SSID: '
        else:
            labelssid2 = ''
        if len(ssid5) > 0:
            labelssid5 = '\n' + 'SSID 5 GHZ: '
        else:
            labelssid5 = ''
        if len(sside2) > 0:
            labelsside2 = '\n' + 'SSID закр.:'
        else:
            labelsside2 = ''
        if len(sside5) > 0:
            labelsside5 = '\n' + 'SSID закр. 5GHz:'
        else:
            labelsside5 = ''
        if len(pochta) > 0:
            labelpochta = '\n' + 'Учетные данные для ЛК отправлены - '
        else:
            labelpochta = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labeltarif + tarif + labelportal + portal + labelssid2 + ssid2 + labelssid5 + ssid5 + labelsside2 + sside2 + labelsside5 + sside5 + labelmac + mac + labelpochta + pochta
        pyperclip.copy(to_cms)

    def form_cms_rrs(self):
        domen = self.ui.domen_rrs.text()
        portal = self.ui.portal_rrs.text()
        ssid = self.ui.ssid_rrs.text()
        sside = self.ui.sside_rrs.text()
        ssidp = self.ui.ssidp_rrs.text()
        mac = (', ').join(self.ui.mac_rrs.toPlainText().split('\n'))
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid) > 0:
            labelssid = '\n' + 'SSID откр: '
        else:
            labelssid = ''
        if len(sside) > 0:
            labelsside = '\n' + 'SSID закр. Enterpise: '
        else:
            labelsside = ''
        if len(ssidp) > 0:
            labelssidp = '\n' + 'SSID закр. Personal:'
        else:
            labelssidp = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labelportal + portal + labelssid + ssid + labelsside + sside + labelssidp + ssidp + labelmac + mac
        pyperclip.copy(to_cms)

    def form_cms_psb(self):
        domen = self.ui.domen_psb.text()
        portal = self.ui.portal_psb.text()
        ssid = self.ui.ssid_psb.text()
        mac = (', ').join(self.ui.mac_psb.toPlainText().split('\n'))
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid) > 0:
            labelssid = '\n' + 'SSID: '
        else:
            labelssid = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labelportal + portal + labelssid + ssid + labelmac + mac
        pyperclip.copy(to_cms)

    def form_cms_gpb(self):
        domen = self.ui.domen_gpb.text()
        portal = self.ui.portal_gpb.text()
        ssid = self.ui.ssid_gpb.text()
        mac = (', ').join(self.ui.mac_gpb.toPlainText().split('\n'))
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid) > 0:
            labelssid = '\n' + 'SSID: '
        else:
            labelssid = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labelportal + portal + labelssid + ssid + labelmac + mac
        pyperclip.copy(to_cms)

    def form_cms_vtb(self):
        domen = self.ui.domen_vtb.text()
        tarif = self.ui.tarif_vtb.text()
        portal = self.ui.portal_vtb.text()
        ssid = self.ui.ssid_vtb.text()
        sside = self.ui.sside_vtb.text()
        mac = (', ').join(self.ui.mac_vtb.toPlainText().split('\n'))
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(tarif) > 0:
            labeltarif = '\n' + 'Тариф: '
        else:
            labeltarif = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid) > 0:
            labelssid = '\n' + 'SSID откр.: '
        else:
            labelssid = ''
        if len(sside) > 0:
            labelsside = '\n' + 'SSID закр.: '
        else:
            labelsside = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labeltarif + tarif + labelportal + portal + labelssid + ssid + labelsside + sside + labelmac + mac
        pyperclip.copy(to_cms)

    def form_cms_sber(self):
        domen = self.ui.domen_sber.text()
        tarif = self.ui.tarif_sber.text()
        portal = self.ui.portal_sber.text()
        ssid = self.ui.ssid_sber.text()
        sside = self.ui.sside_sber.text()
        ssideq = self.ui.ssidequs_sber.text()
        mac = (', ').join(self.ui.mac_sber.toPlainText().split('\n'))
        if len(domen) > 0:
            labeldomen = '\n' + 'Домен: '
        else:
            labeldomen = ''
        if len(tarif) > 0:
            labeltarif = '\n' + 'Тариф: '
        else:
            labeltarif = ''
        if len(portal) > 0:
            labelportal = '\n' + 'Портал: '
        else:
            labelportal = ''
        if len(ssid) > 0:
            labelssid = '\n' + 'SSID откр.: '
        else:
            labelssid = ''
        if len(sside) > 0:
            labelsside = '\n' + 'SSID закр.: '
        else:
            labelsside = ''
        if len(ssideq) > 0:
            labelssideq = '\n' + 'SSID EQUs:'
        else:
            labelssideq = ''
        if len(mac) > 0:
            labelmac = '\n' + 'Создано правило инициализации для ТД с МАС: '
        else:
            labelmac = ''
        to_cms = labeldomen + domen + labeltarif + tarif + labelportal + portal + labelssid + ssid + labelsside + sside + labelssideq + ssideq + labelmac + mac
        pyperclip.copy(to_cms)

# Формирование пароля для сети EQUS_SBRF при запролнении поля ГОСБ

    def pass_equs(self):
        gosb = self.ui.gosb_sber.text()
        if gosb != 0:
            self.ui.passequs_sber.setText(gosb + 'Sb7+')
        else:
            self.ui.passequs_sber.setText('')

    # Формирование названия сети для ВСП
    def sside_sbrf(self):
        gosb = self.ui.gosb_sber.text()
        vsp = self.ui.vsp_sber.text()
        if gosb != 0 and vsp != 0:
            self.ui.sside_sber.setText('SBRF_' + gosb + '_' + vsp)

    # Формирование пароля для закрытой сети Сбербанка
    def pass_sside_sbrf(self):
        month = datetime.datetime.today().strftime("%m")
        vsp = self.ui.vsp_sber.text()
        self.ui.passent_sber.setText(vsp + 's' + month)

    # Формирование названия сети для RRS
    def form_ssid_rrs(self):
        otd = self.ui.otd_rrs.text()
        if otd != 0:
            self.ui.sside_rrs.setText('RRS_HOME'+otd)
            self.ui.ssidp_rrs.setText('RRS_SB'+otd)

    # Формирование описания для EMS
    def form_opis_common(self):
        zakaz = self.ui.zakaz_common.text()
        klient = self.ui.klient_common.text()
        address = self.ui.address_common.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)

    def form_opis_psb(self):
        zakaz = self.ui.zakaz_psb.text()
        klient = self.ui.klient_psb.text()
        address = self.ui.address_psb.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)

    def form_opis_rrs(self):
        zakaz = self.ui.zakaz_rrs.text()
        klient = self.ui.klient_rrs.text()
        address = self.ui.address_rrs.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)

    def form_opis_gpb(self):
        zakaz = self.ui.zakaz_gpb.text()
        klient = self.ui.klient_gpb.text()
        address = self.ui.address_gpb.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)

    def form_opis_vtb(self):
        zakaz = self.ui.zakaz_vtb.text()
        klient = self.ui.klient_vtb.text()
        address = self.ui.address_vtb.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)

    def form_opis_sber(self):
        zakaz = self.ui.zakaz_sber.text()
        klient = self.ui.klient_sber.text()
        address = self.ui.address_sber.text()
        opis = zakaz + ' ' + klient + ' ' + address
        pyperclip.copy(opis)



    # Конвертация mac- адресов  в корректные

    def macconvert_common(self):
        maclist = self.ui.mac_common.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_common.setText('\n'.join(maclist))

    def macconvert_rrs(self):
        maclist = self.ui.mac_rrs.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_rrs.setText('\n'.join(maclist))

    def macconvert_psb(self):
        maclist = self.ui.mac_psb.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_psb.setText('\n'.join(maclist))

    def macconvert_gpb(self):
        maclist = self.ui.mac_gpb.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_gpb.setText('\n'.join(maclist))

    def macconvert_vtb(self):
        maclist = self.ui.mac_vtb.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_vtb.setText('\n'.join(maclist))

    def macconvert_sber(self):
        maclist = self.ui.mac_sber.toPlainText().split('\n')
        maclist = map(convert, maclist)
        self.ui.mac_sber.setText('\n'.join(maclist))

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
        mail.CC = 'wifi-hs@rt.ru'
        mail.Subject = 'УЗ для ЛК по № ' + self.ui.zakaz_common.text()
        mail.Body = zagolovoklk + '\n' + '\n' + zagolovokssid
        mail.Display(True)

    def autofill_common(self):
        text = self.ui.oblast_common.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_common.setText(dict.get(text)[0])
            self.ui.region_common.setText(dict.get(text)[1])
            self.ui.mrf_common.setText(dict.get(text)[2])

    def autofill_rrs(self):
        text = self.ui.oblast_rrs.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_rrs.setText(dict.get(text)[0])
            self.ui.region_rrs.setText(dict.get(text)[1])
            self.ui.mrf_rrs.setText(dict.get(text)[2])

    def autofill_psb(self):
        text = self.ui.oblast_psb.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_psb.setText(dict.get(text)[0])
            self.ui.region_psb.setText(dict.get(text)[1])
            self.ui.mrf_psb.setText(dict.get(text)[2])

    def autofill_gpb(self):
        text = self.ui.oblast_gpb.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_gpb.setText(dict.get(text)[0])
            self.ui.region_gpb.setText(dict.get(text)[1])
            self.ui.mrf_gpb.setText(dict.get(text)[2])

    def autofill_vtb(self):
        text = self.ui.oblast_vtb.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_vtb.setText(dict.get(text)[0])
            self.ui.region_vtb.setText(dict.get(text)[1])
            self.ui.mrf_vtb.setText(dict.get(text)[2])

    def autofill_sber(self):
        text = self.ui.oblast_sber.currentText()
        dict = autofill(text)
        if dict.get(text) is None:
            pass
        else:
            self.ui.gorod_sber.setText(dict.get(text)[0])
            self.ui.region_sber.setText(dict.get(text)[1])
            self.ui.mrf_sber.setText(dict.get(text)[2])

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
        self.ui.ssid2_common.setDisabled(False)
        self.ui.ssid5_common.setDisabled(False)
        self.ui.portal_common.setDisabled(False)
        self.ui.redirect_common.setDisabled(False)
        self.ui.sside2_common.setDisabled(False)
        self.ui.sside5_common.setDisabled(False)
        self.ui.uzsside2_common.setDisabled(False)
        self.ui.passent2_common.setDisabled(False)
        self.ui.genpassent2_common.setDisabled(False)
        self.ui.uzsside5_common.setDisabled(False)
        self.ui.passent5_common.setDisabled(False)
        self.ui.genpassent5_common.setDisabled(False)
        self.ui.redirect_common.setDisabled(False)
        self.ui.kl_common.setDisabled(False)
        self.ui.telkl_common.setDisabled(False)
        self.ui.mailkl_common.setDisabled(False)
        self.ui.uzlk_common.setDisabled(False)
        self.ui.passlk_common.setDisabled(False)
        self.ui.genpasslk_common.setDisabled(False)
        self.ui.pochtamp_common.setDisabled(False)

    def klass_checked(self):
        ch = functions.Checkboxes()
        ch.checkboxklass_choose()


    """def checkboxklass_choose(self):
        if self.ui.checkboxklass_common.isChecked():
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(True)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(True)
        else:
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(False)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(False)"""

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
            self.ui.redirect_common.setDisabled(True)
            self.ui.checkboxsms_common.setDisabled(True)
            self.ui.checkboxesia_common.setDisabled(True)
            self.ui.checkboxzvonok_common.setDisabled(True)
        else:
            self.ui.checkboxssid2yes_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)
            self.ui.redirect_common.setDisabled(False)
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
            #self.ui.portal_common.setDisabled(True)
        else:
            self.ui.checkboxssid5yes_common.setDisabled(False)
            self.ui.portal_common.setDisabled(False)
            self.ui.ssid5_common.setDisabled(False)

    def sside2yes_choose(self):
        if self.ui.checkboxsside2yes_common.isChecked():
            self.ui.checkboxsside2no_common.setChecked(False)
            self.ui.checkboxsside2no_common.setDisabled(True)
            self.ui.uzsside2_common.setDisabled(False)
            self.ui.genpassent2_common.setDisabled(False)
            self.ui.passent2_common.setDisabled(False)
        else:
            self.ui.checkboxsside2no_common.setDisabled(False)

    def sside5yes_choose(self):
        if self.ui.checkboxsside5yes_common.isChecked():
            self.ui.checkboxsside5no_common.setChecked(False)
            self.ui.checkboxsside5no_common.setDisabled(True)
            self.ui.uzsside5_common.setDisabled(False)
            self.ui.genpassent5_common.setDisabled(False)
            self.ui.passent5_common.setDisabled(False)
        else:
            self.ui.checkboxsside5no_common.setDisabled(False)

    def sside2no_choose(self):
        if self.ui.checkboxsside2no_common.isChecked():
            self.ui.checkboxsside2yes_common.setChecked(False)
            self.ui.checkboxsside2yes_common.setDisabled(True)
            self.ui.sside2_common.setDisabled(True)
            self.ui.uzsside2_common.setDisabled(True)
            self.ui.passent2_common.setDisabled(True)
            self.ui.genpassent2_common.setDisabled(True)
        else:
            #self.ui.checkboxsside2yes_common.setChecked(False)
            self.ui.checkboxsside2yes_common.setDisabled(False)
            self.ui.sside2_common.setDisabled(False)
            self.ui.uzsside2_common.setDisabled(False)
            self.ui.passent2_common.setDisabled(False)
            self.ui.genpassent2_common.setDisabled(False)


    def sside5no_choose(self):
        if self.ui.checkboxsside5no_common.isChecked():
            self.ui.checkboxsside5yes_common.setChecked(False)
            self.ui.checkboxsside5yes_common.setDisabled(True)
            self.ui.sside5_common.setDisabled(True)
            self.ui.uzsside5_common.setDisabled(True)
            self.ui.passent5_common.setDisabled(True)
            self.ui.genpassent5_common.setDisabled(True)
        else:
            self.ui.checkboxsside5yes_common.setChecked(False)
            self.ui.checkboxsside5yes_common.setDisabled(False)
            self.ui.sside5_common.setDisabled(False)
            self.ui.uzsside5_common.setDisabled(False)
            self.ui.passent5_common.setDisabled(False)
            self.ui.genpassent5_common.setDisabled(False)

    def lkyes_choose(self):
        if self.ui.checkboxlkyes_common.isChecked():
            self.ui.checkboxlkno_common.setDisabled(True)
            self.ui.checkboxlkno_common.setChecked(False)
            self.ui.uzlk_common.setDisabled(False)
            self.ui.passlk_common.setDisabled(False)
            self.ui.genpasslk_common.setDisabled(False)
            self.ui.kl_common.setDisabled(False)
            self.ui.telkl_common.setDisabled(False)
            self.ui.mailkl_common.setDisabled(False)
            self.ui.pochtamp_common.setDisabled(False)
        else:
            self.ui.checkboxlkno_common.setDisabled(False)
    def lkno_choose(self):
        if self.ui.checkboxlkno_common.isChecked():
            self.ui.checkboxlkyes_common.setChecked(False)
            self.ui.checkboxlkyes_common.setDisabled(True)
            self.ui.uzlk_common.setDisabled(True)
            self.ui.passlk_common.setDisabled(True)
            self.ui.genpasslk_common.setDisabled(True)
            self.ui.kl_common.setDisabled(True)
            self.ui.telkl_common.setDisabled(True)
            self.ui.mailkl_common.setDisabled(True)
            self.ui.pochtamp_common.setDisabled(True)
        else:
            self.ui.checkboxlkyes_common.setDisabled(False)
            self.ui.uzlk_common.setDisabled(False)
            self.ui.passlk_common.setDisabled(False)
            self.ui.genpasslk_common.setDisabled(False)
            self.ui.kl_common.setDisabled(False)
            self.ui.telkl_common.setDisabled(False)
            self.ui.mailkl_common.setDisabled(False)
            self.ui.pochtamp_common.setDisabled(False)


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

    def create_domen_common(self):
        k = self.ui.klientsoc_common.text()
        u = self.ui.ulica_common.text()
        d = self.ui.dom_common.text()
        translit_domen = k + '_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_common.setText(trans)

    def create_domen_rrs(self):
        u = self.ui.ulica_rrs.text()
        d = self.ui.dom_rrs.text()
        translit_domen = 'RRS_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_rrs.setText(trans)

    def create_domen_psb(self):
        c = self.ui.city_psb.text()
        u = self.ui.ulica_psb.text()
        d = self.ui.dom_psb.text()
        translit_domen = c + '_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_psb.setText(trans)

    def create_domen_gpb(self):
        c = self.ui.city_gpb.text()
        u = self.ui.ulica_gpb.text()
        d = self.ui.dom_gpb.text()
        translit_domen = c + '_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_gpb.setText(trans)

    def create_domen_vtb(self):
        c = self.ui.city_vtb.text()
        u = self.ui.ulica_vtb.text()
        d = self.ui.dom_vtb.text()
        translit_domen = c + '_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_vtb.setText(trans)

    def create_domen_sber(self):
        g = self.ui.gosb_sber.text()
        v = self.ui.vsp_sber.text()
        u = self.ui.ulica_sber.text()
        d = self.ui.dom_sber.text()
        translit_domen = g + '_' + v + '_' + u + '_' + d
        trans = translit(translit_domen)
        self.ui.domen_sber.setText(trans)

    def create_portal_comom(self):
        m = self.ui.mrf_common.text()
        c = self.ui.city_common.text()
        k = self.ui.klientsoc_common.text()
        if self.ui.checkboxott_common.isChecked():
            translit_portal = m + '_' + c + '_' + k + '_ОТТ'
        elif self.ui.checkboxinterop_common.isChecked():
            translit_portal = m + '_' + c + '_' + k + '_ESR10'
        else:
            translit_portal = m + '_' + c + '_' + k
        transp = translit(translit_portal)
        self.ui.portal_common.setText(transp)

    def save_data_common(self):
        list = {self.ui.zakaz_common.text(),
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
                }
        stri = (', ').join(map(str, list))

        nowdate = datetime.datetime.today().strftime("%d-%m-%Y")
        # with open(nowdate + ".txt", "a") as file:
        #    list = ('|').join(list) + '\n'
        #    file.writelines(list)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.show()

    sys.exit(app.exec())
