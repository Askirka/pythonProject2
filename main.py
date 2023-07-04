from russian_names import RussianNames
from openpyxl import Workbook
def generate_person():
    names = RussianNames()
    surname = names.get_surname()
    first_name = names.get_first_name()
    patronymic = names.get_patronymic()
    return (surname, first_name, patronymic)



def write_to_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.append(["Номер", "Фамилия", "Имя", "Отчество"])
    for i, person in enumerate(data, start=1):
        ws.append([i] + list(person))
    wb.save("people.xlsx")

def main():
    num_people = int(input("Введите количество фейковых личностей: "))
    people = []
    for _ in range(num_people):
        person = generate_person()
        people.append(person)
    write_to_excel(people)

if __name__ == "__main__":
    main()
