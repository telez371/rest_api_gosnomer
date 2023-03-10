from random import randint
from random import choice
import json

class RegistrationMarkGenerator:
    valid_registration_mark_letters = 'АВЕКМНОРСТУХ'
    valid_region = ['01', '02', '03', '04', '05', '06', '07', '08',
                    '09', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24',
                    '25', '26', '27', '28', '29', '30', '31', '32',
                    '33', '34', '35', '36', '37', '38', '39', '40',
                    '41', '42', '43', '44', '45', '46', '47', '48',
                    '49', '50', '51', '52', '53', '54', '55', '56',
                    '57', '58', '59', '60', '61', '62', '63', '64',
                    '65', '66', '67', '68', '69', '70', '71', '72',
                    '73', '74', '75', '76', '77', '78', '79', '80',
                    '81', '82', '83', '84', '85', '86', '87', '88',
                    '89', '90', '91', '92', '93', '94', '95', '96',
                    '97', '98', '99', '102', '113', '116', '121',
                    '122', '123', '124', '125', '126', '134', '136',
                    '138', '142', '147', '150', '152', '154', '156',
                    '159', '161', '163', '164', '173', '174', '177',
                    '178', '186', '190', '193', '196', '197', '198',
                    '199', '702', '750', '716', '761', '763', '774',
                    '777', '790', '797', '799']
    def generate_car_number(self):
        first_registration_letter = choice(self.valid_registration_mark_letters)
        first_tree_registration_numbers = str(randint(1001, 1999))[1:]
        last_too_registration_letters = choice(self.valid_registration_mark_letters) + choice(self.valid_registration_mark_letters)
        registration_region = choice(self.valid_region)
        return first_registration_letter  + first_tree_registration_numbers + last_too_registration_letters + registration_region



