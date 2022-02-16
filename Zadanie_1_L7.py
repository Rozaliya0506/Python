class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        clas_matr = ""
        for el in range(len(self.list)):
            for i in range(len(self.list[el])):
                clas_matr += f'{self.list[el][i]:3}'
            clas_matr +='\n'
        return clas_matr


    def __add__(self, other):
        list = []
        for el in range(len(self.list)):
            new_matr = []
            for i in range(len(self.list[el])):
                new_el = self.list[el][i] + other.list[el][i]
                new_matr.append(new_el)
            list.append(new_matr)
        return Matrix(list)


my_list_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_list_2 = Matrix([[7, 3, 5], [1, 9, 8], [2, 6, 4]])
print(my_list_1.__str__())
print(my_list_1 + my_list_2)
