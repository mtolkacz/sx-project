import hashlib

from ..exceptions import DataListNotFound, DatalistKeyError


class JsonShaDataListMixin(object):
    data_list = None
    result = None

    def get_datalist_parameter(self):
        data_list = self.request.data.get("data_list", "")

        if not data_list:
            raise DataListNotFound

        return data_list

    def set_datalist(self):
        self.data_list = self.get_datalist_parameter()

    def get_sorted_datalist(self):
        try:
            sorted_list = sorted(self.data_list, key=lambda row: (row['second_name'], row['first_name']))
        except KeyError as ex:
            raise DatalistKeyError
        return sorted_list

    def set_result(self):
        self.result = self.get_sorted_datalist()
        self.encrypt_result()

    @staticmethod
    def encrypt_string(string):
        return hashlib.sha256(string.encode()).hexdigest()

    def encrypt_result(self):
        for row in self.result:
            to_encrypt = row['first_name'] + row['second_name'] + row['birth_date']
            row['sha256'] = self.encrypt_string(to_encrypt)
