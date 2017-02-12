#coding=utf-8

class antpedia_json(object):

    def antpedia_json(self, json_data, json_key):
        re_dict = {}

        key_list = []
        re_list = self.key_list(json_key, key_list)
        data = json_data
        for char in re_list:
            char = self.islist_index(char)
            data = data[char]
        return data

    def key_list(self, key, para_list):
        if key.find(".") != -1:
            count = key.find(".")
            para_list.append(key[:count])
            self.key_list(key[count+1:], para_list)
        else:
            para_list.append(key)
        return para_list

    def islist_index(self, char):
        re_char = char
        if char[:1] == "[" and char[-1:] == "]":
            re_char = int(char[1:-1])
        return re_char