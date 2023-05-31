from utilities.utilities import Utilities


class Phones:
    ut = Utilities()

    def find_phone(self):
        apple_phones = []
        phones = self.ut.gets_data_from_json_file('phones.json')
        for data in phones['phones']:
            list_of_phones = data['list_of_phones']
            for phone in list_of_phones:
                if 'Apple' in phone:
                    apple_phones.append(phone)
            print(apple_phones)


p = Phones()
p.find_phone()
