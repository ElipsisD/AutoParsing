from autodoc_search import autodoc_parse
import db


def main():
    part_number = input('Введите номер запчасти:\n')  # W7008  2074151  92101-4X000
    if not db.availability(part_number):
        price, partname, manufacturer, source = autodoc_parse(part_number)
        db.insert_partname(part_number, partname, manufacturer)
    else:
        partname, manufacturer = db.get_partname(part_number)
        price, partname, manufacturer, source = autodoc_parse(part_number, partname, manufacturer)
    db.insert_request(part_number, price, source)
    print('В базу внесена запись:\n'
          f'{part_number} {partname} {price} р.')


if __name__ == "__main__":
    main()
