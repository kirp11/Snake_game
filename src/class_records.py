

class Records:
    def __init__(self):
        self.__result = ""
        self.__records = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
        self.__name = ""


    def get_result(self):
        return self.__result

    def get_records(self):
        return self.__records

    def get_name(self):
        return self.__name

    def set_result(self, result: int):
        self.__result = result

    def set_records(self, records:list):
        self.__records = records

    def set_name(self, name:str):
        self.__name = name

    def check_on_record(self):
        if self.__result!= 0:
            i = 0
            if self.__records[i][1] == "":
                return True
            while self.__records[i][1] != "":
                if self.__records[i][1] < self.__result:
                    return True
                i += 1
            return False


    def add_result(self, name):
        if self.__result!= 0:
            if self.__records[0][1] == "":
                self.__records[0][1] = self.__result
                self.__records[0][0] = name
                return
            for i in range(0, 5, 1):

                if self.__records[i][1] < self.__result or self.__records[i][1] == "":
                    self.__records.insert(i, [name, self.__result])
                    self.__records = self.__records[:-1]
                    self.__result = 0
                    return
