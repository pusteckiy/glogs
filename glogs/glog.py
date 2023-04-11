import asyncio
from typing import Union
import re

import pyotp
import aiohttp
from bs4 import BeautifulSoup


class Sort:
    DESC = 'desc'
    ASC = 'asc'


class Limit:
    L100 = 100
    L500 = 500
    L1000 = 1000


class Type:
    CONTAINER_NFT_OPEN = 'container_nft_open'
    ANTI_WARN = 'anti_warn'
    ANTI_WARN_REMOVE = 'anti_warn_remove'
    ANTI_WARN_ADD = 'anti_warn_add'
    AUCTION_FAMAPART_BET = 'auction_famapart_bet'
    ADMIN_SALARY = 'admin_salary'
    ADMIN_SALARY_ADD = 'admin_salary_add'
    ADMIN_SALARY_REMOVE = 'admin_salary_remove'
    INVENTORY_FROM_SECURITY = 'inventory_from_security'
    INVENTORY_TO_SECURITY = 'inventory_to_security'
    USE_ITEM_SHARPENING_13 = 'use_item_sharpening_13'
    CRAFT = 'craft'
    CRAFT_SUCCESS = 'craft_success'
    CRAFT_FAIL = 'craft_fail'
    PROPERTY_OBJECTS = 'property_objects'
    PROPERTY_OBJECTS_DESTROY = 'property_objects_destroy'
    PROPERTY_OBJECTS_INSTALL = 'property_objects_install'
    ELIXIR_MASTER_BUY_ASC = 'elixir_master_buy_asc'
    ELIXIR_MASTER = 'elixir_master'
    PRIVATE_FRACTION_BUY = 'private_fraction_buy'
    PRIVATE_FRACTION_BET = 'private_fraction_bet'
    PRIVATE_FRACTION_BUY_ASC = 'private_fraction_buy_asc'
    PRIVATE_FRACTION = 'private_fraction'
    PRIVATE_FRACTION_SELL_ADMIN = 'private_fraction_sell_admin'
    PRIVATE_FRACTION_ADD_TAX = 'private_fraction_add_tax'
    PRIVATE_FRACTION_SELL = 'private_fraction_sell'
    PRIVATE_FRACTION_SELL_FAMILY = 'private_fraction_sell_family'
    PRIVATE_FRACTION_UVALLEADER = 'private_fraction_uvalleader'
    PRIVATE_FRACTION_MAKELEADER = 'private_fraction_makeleader'
    RENT_SPUTNIK = 'rent_sputnik'
    RENT_SPUTNIK_FINISH = 'rent_sputnik_finish'
    RENT_SPUTNIK_OFFER = 'rent_sputnik_offer'
    RENT_SPUTNIK_ACCEPT = 'rent_sputnik_accept'
    REFERAL_ENTER = 'referal_enter'
    ARZ_STABLE_COIN = 'arz_stable_coin'
    ARZ_STABLE_COIN_GIVE = 'arz_stable_coin_give'
    ARZ_STABLE_COIN_REMOVE = 'arz_stable_coin_remove'
    ARZ_STABLE_COIN_ADD = 'arz_stable_coin_add'
    INVENTORY_STORAGE = 'inventory_storage'
    INVENTORY_STORAGE_GIVE_ITEMS = 'inventory_storage_give_items'
    RECONSTRUCTION = 'reconstruction'
    RECONSTRUCTION_PUT_MONEY = 'reconstruction_put_money'
    RECONSTRUCTION_STATUS = 'reconstruction_status'
    LAREC_GIVE_SUPERPRIZE = 'larec_give_superprize'
    PROPERTY_TAX = 'property_tax'
    SET_BUSINESS_TAX = 'set_business_tax'
    SET_HOUSE_TAX = 'set_house_tax'
    PRIVATE_AUTOSALON_VC = 'private_autosalon_vc'
    AUTOSALON_VC_RETURN_CAR = 'autosalon_vc_return_car'
    AUTOSALON_VC_BUY_CAR = 'autosalon_vc_buy_car'
    AUTOSALON_VC_SELL_CAR = 'autosalon_vc_sell_car'
    DONATE_PACKS = 'donate_packs'
    PROMO = 'promo'
    PROMO_SET_DOMAIN = 'promo_set_domain'
    PROMO_CREATE = 'promo_create'
    PROMO_ENTER = 'promo_enter'
    TIDEX = 'tidex'
    TIDEX_FROM_DEPOSIT = 'tidex_from_deposit'
    TIDEX_ON_DEPOSIT = 'tidex_on_deposit'
    TIDEX_REMOVE = 'tidex_remove'
    RENT_CAR = 'rent_car'
    BOOKMAKER = 'bookmaker'
    BOOKMAKER_BET = 'bookmaker_bet'
    VKOIN = 'vkoin'
    VKOIN_REMOVE = 'vkoin_remove'
    VKOIN_ADD = 'vkoin_add'
    BITCOIN = 'bitcoin'
    BUY_NFT_SKIN = 'buy_nft_skin'
    BITCOIN_ADD = 'bitcoin_add'
    BITCOIN_REMOVE = 'bitcoin_remove'
    BITCOIN_GIVE = 'bitcoin_give'
    EURO = 'euro'
    EURO_GIVE = 'euro_give'
    EURO_REMOVE = 'euro_remove'
    EURO_ADD = 'euro_add'
    ITEM_UPGRADE = 'item_upgrade'
    FAMILY = 'family'
    DEPUTY_FAMILY = 'deputy_family'
    GIFTS = 'gifts'
    GIFTS_REMOVE = 'gifts_remove'
    GIFTS_ADD = 'gifts_add'
    WANTED = 'wanted'
    CHIPS = 'chips'
    CHIPS_GIVE = 'chips_give'
    CHIPS_REMOVE = 'chips_remove'
    CHIPS_ADD = 'chips_add'
    PRIVATE_BANK = 'private_bank'
    PRIVATE_BANK_GET_SAFE = 'private_bank_get_safe'
    PRIVATE_BANK_ADD_SAFE = 'private_bank_add_safe'
    PRIVATE_BANK_GET_DEP = 'private_bank_get_dep'
    PRIVATE_BANK_ADD_DEP = 'private_bank_add_dep'
    PRIVATE_BANK_UPGRADE_2 = 'private_bank_upgrade_2'
    PRIVATE_BANK_UPGRADE_1 = 'private_bank_upgrade_1'
    DONATE_BUY_ITEMS = 'donate_buy_items'
    RENT_ACCESSORY = 'rent_accessory'
    TAKE_ENDLESS_ADDVIP = 'take_endless_addvip'
    CITYHALL_TRANSFER_CARS = 'cityhall_transfer_cars'
    BATTLEPASS_SKIP_MISSION_FREE = 'battlepass_skip_mission_free'
    VKOIN_STORE_BUY = 'vkoin_store_buy'
    EXCHANGE_PROPERTY = 'exchange_property'
    FORTUNEWHEEL = 'fortunewheel'
    FORTUNE_WHEEL_GIVE_PRIZE = 'fortune_wheel_give_prize'
    BLACKJACK = 'blackjack'
    BLACKJACK_MONEY_TAKE = 'blackjack_money_take'
    BLACKJACK_WIN = 'blackjack_win'
    BATTLEPASS = 'battlepass'
    BATTLEPASS_PRIZE_BAD_1 = 'battlepass_prize_bad_1'
    BATTLEPASS_TAKE_PRIZE = 'battlepass_take_prize'
    BATTLEPASS_TAKE_PRIZE = 'battlepass_take_prize'
    BATTLEPASS_SELL_PRIZE_AZ = 'battlepass_sell_prize_az'
    BATTLEPASS_LAREC = 'battlepass_larec'
    BATTLEPASS_BUY_BASIC_PASS = 'battlepass_buy_basic_pass'
    BATTLEPASS_BUY_GOLD_PASS = 'battlepass_buy_gold_pass'
    BATTLEPASS_SKIP_MISSION_AZ = 'battlepass_skip_mission_az'
    BATTLEPASS_COMPLETE_MISSION = 'battlepass_complete_mission'
    BATTLEPASS_GIVE_PROGRESS = 'battlepass_give_progress'
    BATTLEPASS_GIVE_MISSION = 'battlepass_give_mission'
    VEHICLE_CERTIFICATE_OPEN = 'vehicle_certificate_open'
    AUCTION_BIZ_BET = 'auction_biz_bet'
    AUCTION_HOUSE_BET = 'auction_house_bet'
    RETURN_MONEY_DONATE = 'return_money_donate'
    RETURN_MONEY_BANK = 'return_money_bank'
    RETURN_MONEY_CASH = 'return_money_cash'
    FLIGHT_TICKET_BUY = 'flight_ticket_buy'
    VC_TRANSFER_CARS = 'vc_transfer_cars'
    FLIGHT_FROM_VICECITY = 'flight_from_vicecity'
    VC_CURRENCY_EXCHANGE_BUY = 'vc_currency_exchange_buy'
    VC_CURRENCY_EXCHANGE_SELL = 'vc_currency_exchange_sell'
    FLIGHT_FROM_LOSSANTOS = 'flight_from_lossantos'
    FLIGHT_TO_LOSSANTOS = 'flight_to_lossantos'
    FLIGHT_TO_VICECITY = 'flight_to_vicecity'
    CRASH = 'crash'
    BANK = 'bank'
    BANK_ADD = 'bank_add'
    BANK_GIVE = 'bank_give'
    BANK_REMOVE = 'bank_remove'
    ADMIN = 'admin'
    REMOVE_AUTOADS = 'remove_autoads'
    ASELLSKLAD = 'asellsklad'
    PLPOS = 'plpos'
    RMUTE = 'rmute'
    UNRMUTE = 'unrmute'
    SLAPCAR = 'slapcar'
    FLIP = 'flip'
    UNFREEZE = 'unfreeze'
    FREEZE = 'freeze'
    RECON = 'recon'
    PM = 'pm'
    TRSPAWN = 'trspawn'
    SETINT = 'setint'
    SETVW = 'setvw'
    SP = 'sp'
    SPC = 'spc'
    REMOVETUNE = 'removetune'
    CHECK = 'check'
    TP_ADMIN_ZONE = 'tp_admin_zone'
    GIVE_MEDCARD = 'give_medcard'
    GIVE_ARMYTICKET = 'give_armyticket'
    GIVE_MEDCARD = 'give_medcard'
    GIVE_ARMYTICKET = 'give_armyticket'
    AGL = 'agl'
    DELLFAM = 'dellfam'
    PLVEH = 'plveh'
    ACMAIL = 'acmail'
    ACCEPTTRADE = 'accepttrade'
    GETIP = 'getip'
    GIVEITEM = 'giveitem'
    APUNISH = 'apunish'
    GIVEDONATE = 'givedonate'
    SETSTATS = 'setstats'
    SKICK = 'skick'
    WEAP = 'weap'
    REMOVEITEM = 'removeitem'
    ANTICHEAT = 'anticheat'
    SETBIZ = 'setbiz'
    SETGANGZONE = 'setgangzone'
    SPAWNPLAYER = 'spawnplayer'
    AO_CHAT = 'ao_chat'
    BAN = 'ban'
    KPZ = 'kpz'
    GOTO = 'goto'
    JAIL = 'jail'
    KICK = 'kick'
    MUTE = 'mute'
    SLAP = 'slap'
    UVAL = 'uval'
    WARN = 'warn'
    BANIP = 'banip'
    EVENT = 'event'
    SETHP = 'sethp'
    UNBAN = 'unban'
    UNKPZ = 'unkpz'
    ADMREP = 'admrep'
    UNJAIL = 'unjail'
    UNMUTE = 'unmute'
    UNWARN = 'unwarn'
    GETHERE = 'gethere'
    GIVEGUN = 'givegun'
    SETSKIN = 'setskin'
    UNBANIP = 'unbanip'
    BANIPOFF = 'banipoff'
    GIVEMONEY = 'givemoney'
    MAKEADMIN = 'makeadmin'
    BANK_ADMIN = 'bank_admin'
    MAKELEADER = 'makeleader'
    DONATE_ADMIN = 'donate_admin'
    CINEMA_CANCEL = 'cinema_cancel'
    REPORT_ANSWER = 'report_answer'
    SELLBIZ_ADMIN = 'sellbiz_admin'
    SELLCAR_ADMIN = 'sellcar_admin'
    SETNAME_ADMIN = 'setname_admin'
    SELLHOUSE_ADMIN = 'sellhouse_admin'
    MONEY = 'money'
    TRADECAR = 'tradecar'
    TAX = 'tax'
    BUYBIZ = 'buybiz'
    BUYCAR = 'buycar'
    REFERAL = 'referal'
    SELLBIZ = 'sellbiz'
    SELLCAR = 'sellcar'
    BUYHOUSE = 'buyhouse'
    MONEY_ADD = 'money_add'
    SELLBIZTO = 'sellbizto'
    SELLCARTO = 'sellcarto'
    SELLHOUSE = 'sellhouse'
    MONEY_GIVE = 'money_give'
    SELLHOUSETO = 'sellhouseto'
    MONEY_REMOVE = 'money_remove'
    REFERAL_RETURN = 'referal_return'
    OTHER = 'other'
    LEVEL = 'level'
    EFFECTX4 = 'effectx4'
    DEPUTY_BIZ = 'deputy_biz'
    UNWARN_TALON = 'unwarn_talon'
    CREDIT = 'credit'
    CREDIT_ADD = 'credit_add'
    CREDIT_REMOVE = 'credit_remove'
    DONATE = 'donate'
    SELLBIZ_DONATE = 'sellbiz_donate'
    BUYBIZ_DONATE = 'buybiz_donate'
    DONATE_ADD = 'donate_add'
    DONATE_GIVE = 'donate_give'
    DONATE_REMOVE = 'donate_remove'
    PLAYER = 'player'
    LOGIN = 'login'
    CONNECT = 'connect'
    REGISTER = 'register'
    DISCONNECT = 'disconnect'
    LOGIN_SETNAME = 'login_setname'
    SERVER = 'server'
    SERVERSTATS = 'serverstats'
    STOP = 'stop'
    START = 'start'
    TUNING = 'tuning'
    TUNING_ATTACH = 'tuning_attach'
    TUNING_DETACH = 'tuning_detach'
    DEPOZIT = 'depozit'
    DEPOZIT_ADD = 'depozit_add'
    DEPOZIT_REMOVE = 'depozit_remove'
    FRACTION = 'fraction'
    FRACTION_MONEY_ADD = 'fraction_money_add'
    CAPTURE = 'capture'
    SWITCH_WAREHOUSE = 'switch_warehouse'
    SET_RANKNAME = 'set_rankname'
    ORG_BANK_TAKE = 'org_bank_take'
    GIVESKIN = 'giveskin'
    SETTAG = 'settag'
    INVITE = 'invite'
    PUNISH = 'punish'
    PREMIUM = 'premium'
    GIVERANK = 'giverank'
    UNINVITE = 'uninvite'
    UNPUNISH = 'unpunish'
    SECURITY = 'security'
    GOOGLEAUTH_ENABLE = 'googleauth_enable'
    GOOGLEAUTH_DISABLE = 'googleauth_disable'
    MAIL_ENABLE = 'mail_enable'
    MAIL_DISABLE = 'mail_disable'
    MAIL = 'mail'
    SETNAME = 'setname'
    PASSWORD = 'password'
    VK_ATTACH = 'vk_attach'
    VK_DETACH = 'vk_detach'
    GOOGLEAUTH_ATTACH = 'googleauth_attach'
    GOOGLEAUTH_DETACH = 'googleauth_detach'
    INVENTORY = 'inventory'
    INVENTORY_TO_TRAILER = 'inventory_to_trailer'
    INVENTORY_FROM_TRAILER = 'inventory_from_trailer'
    INVENTORY_TO_FAMFLAT = 'inventory_to_famflat'
    INVENTORY_FROM_FAMFLAT = 'inventory_from_famflat'
    INVENTORY_TO_PAWNSHOP = 'inventory_to_pawnshop'
    INVENTORY_FROM_PAWNSHOP = 'inventory_from_pawnshop'
    INVENTORY_TO_STOREHOUSE = 'inventory_to_storehouse'
    INVENTORY_FROM_STOREHOUSE = 'inventory_from_storehouse'
    INVENTORY_TO_HOTELROOM = 'inventory_to_hotelroom'
    INVENTORY_FROM_HOTELROOM = 'inventory_from_hotelroom'
    INVENTORY_FROM_CHEST = 'inventory_from_chest'
    INVENTORY_TO_CHEST = 'inventory_to_chest'
    INVENTORY_FROM_TRASH = 'inventory_from_trash'
    INVENTORY_TO_TRASH = 'inventory_to_trash'
    INVENTORY_FROM_BUSINESS = 'inventory_from_business'
    INVENTORY_TO_BUSINESS = 'inventory_to_business'
    INVENTORY_ADD = 'inventory_add'
    INVENTORY_GIVE = 'inventory_give'
    INVENTORY_ADMIN = 'inventory_admin'
    INVENTORY_REMOVE = 'inventory_remove'
    INVENTORY_TO_CAR = 'inventory_to_car'
    INVENTORY_FROM_CAR = 'inventory_from_car'
    INVENTORY_TO_HOUSE = 'inventory_to_house'
    INVENTORY_FROM_HOUSE = 'inventory_from_house'


class LoginError(Exception):
    pass


class ValidationError(Exception):
    pass


class SearchQuery:
    def __init__(self, server_number: int, sort: Sort = Sort.DESC, player: Union[int, str] = '', min_period: str = '', max_period: str = '', types: list[Type] = [], ip: str = ''):
        self.server_number = server_number
        self.sort = sort
        self.player = player
        self.min_period = self._validate_period(min_period)
        self.max_period = self._validate_period(max_period)
        self.types = types
        self.ip = ip

    @staticmethod
    def _validate_period(period: str) -> str:
        if not period:
            return period

        if re.match(r'\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}:\d{2}', period):
            return period
        raise ValidationError(
            'Wrong period value! Must be "yyyy-mm-dd HH:MM:SS". Example: 2023-02-28 10:20:24')

    @property
    def dict(self) -> dict:
        params_dict = {key: value for key,
                       value in self.__dict__.items() if value and key != 'types'}
        if self.__dict__.get('types'):
            params_dict['type[]'] = self.__dict__.get('types')
        return params_dict


class ArizonaLogs:
    def __init__(self, username, password, secret) -> None:
        self.username = username
        self.password = password
        self.secret = secret
        self.cookies = None
        self.base_url = 'https://arizonarp.logsparser.info/'
        self.totp = pyotp.TOTP(secret)

    def __str__(self) -> str:
        return f'User ({self.username})'

    @staticmethod
    def _get_csrf(html: str) -> str:
        soup = BeautifulSoup(html, features="html.parser")
        csrf = soup.find('meta', {'name': 'csrf-token'}).attrs.get('content')
        return csrf

    async def alogin(self) -> None:
        """ Asynchronously logs in to the Arizona Logs website using the username, password, and secret provided during initialization.

            This method sends an HTTP GET request to the login page to retrieve the CSRF token. 
            It then sends an HTTP POST request with the login data and CSRF token to log in. 
            After logging in, it sends another HTTP POST request with the TOTP code to complete the authentication process. 
            The cookies from the response are saved for use in future requests.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url + 'login') as resp:
                html = await resp.text()
                csrf = self._get_csrf(html)
                if not csrf:
                    return

            login_data = {'name': self.username,
                          'password': self.password, '_token': csrf}
            async with session.post(self.base_url + 'login', data=login_data) as resp:
                html = await resp.text()
                if 'Неправильный логин или пароль' in html:
                    raise LoginError('Wrong login or password!')
                csrf = self._get_csrf(html)
                if not csrf:
                    return

            code = self.totp.now()
            async with session.post(self.base_url + 'authenticator', data={'_token': csrf, 'code': code}) as resp:
                html = await resp.text()
                if 'Неверный код' in html:
                    raise LoginError('Wrong google secret code!')
                self.cookies = resp.cookies

    def login(self) -> None:
        """ Logs in to the Arizona Logs website using the username, password, and secret provided during initialization.

            This method sends an HTTP GET request to the login page to retrieve the CSRF token. 
            It then sends an HTTP POST request with the login data and CSRF token to log in. 
            After logging in, it sends another HTTP POST request with the TOTP code to complete the authentication process. 
            The cookies from the response are saved for use in future requests.
        """
        return asyncio.run(self.alogin())

    async def asearch(self, query: SearchQuery) -> list[tuple[str, str]]:
        """ Asynchronously searches for logs using the given query and returns a list of tuples containing the log data.

            This method sends an HTTP GET request to the base URL with the query parameters specified in the `query` argument.
            The response HTML is parsed to extract the log data, which is returned as a list of tuples.
        """
        response_logs = list()
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, cookies=self.cookies, params=query.dict) as resp:
                self.cookies = resp.cookies
                html = await resp.text()
                soup = BeautifulSoup(html, features="html.parser")
                tbody = soup.find('tbody')
                tr_list = tbody.find_all('tr')
                for tr in tr_list:
                    td_list = tr.find_all('td')
                    response_logs.append(
                        (td_list[0].text.strip(), td_list[1].text.strip()))
                return response_logs

    def search(self, query: SearchQuery) -> list[tuple[str, str]]:
        """ Searches for logs using the given query and returns a list of tuples containing the log data.

            This method sends an HTTP GET request to the base URL with the query parameters specified in the `query` argument.
            The response HTML is parsed to extract the log data, which is returned as a list of tuples.
        """
        return asyncio.run(self.asearch(query))


__all__ = ['Sort', 'Limit', 'Type', 'SearchQuery',
           'ArizonaLogs', 'LoginError', 'ValidationError']
