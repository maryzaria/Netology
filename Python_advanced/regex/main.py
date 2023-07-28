import re
import csv


def new_name(lastname, firstname, surname):
    fio = ' '.join([lastname, firstname, surname])
    return re.split(r'\s*[ ]\s*', fio)


def new_phone(string):
    pattern = r'\+?[7-8]\s?[(]?(\d{3})[)]?[ -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})\s?[(]?(доб.)?\s?(\d{4})?[)]?'
    res = re.findall(pattern, string)[0]
    phone = f"+7({res[0]}){res[1]}-{res[2]}-{res[3]}"
    if res[4]:
        phone += f" доб.{res[5]}"
    return phone


def remove_duplicates(data):
    res = []
    for i, contact in enumerate(data):
        for contact2 in data[i + 1:]:
            if contact['firstname'] == contact2['firstname'] and contact['lastname'] == contact2['lastname']:
                for key in contact:
                    contact[key] = contact2[key] if not contact[key] else contact[key]
                res.append(contact2)

    for contact in res:
        data.remove(contact)


def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        contacts_list = list(csv.DictReader(f, delimiter=","))

    for contact in contacts_list:
        contact['lastname'], contact['firstname'], contact['surname'], *_ = \
            new_name(contact['lastname'], contact['firstname'], contact['surname'])
        contact['phone'] = new_phone(contact['phone']) if contact['phone'] else ''
    remove_duplicates(contacts_list)

    with open("phonebook.csv", "w", newline='') as f:
        fieldnames = 'lastname,firstname,surname,organization,position,phone,email'.split(',')
        datawriter = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        datawriter.writeheader()
        datawriter.writerows(contacts_list)

    # with open("phonebook.csv", "r") as f:
    #     contacts_list = list(csv.reader(f, delimiter=","))
    #     print(contacts_list)


if __name__ == '__main__':
    main()
