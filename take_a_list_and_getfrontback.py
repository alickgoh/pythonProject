def list_end(self):
    user_list = self.split()
    print([user_list[0], user_list[-1]])


list_end(input('Enter elements of a list separated by space: '))
