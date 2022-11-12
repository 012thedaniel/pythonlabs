import json
from datetime import date, timedelta
import phonenumbers

ALL_TYPES_OF_TICKETS = ['RegularTicket', 'AdvancedTicket', 'LateTicket', 'StudentsTicket']
ADVANCED_PRICE = 0.6
LATE_PRICE = 1.1
STUDENTS_PRICE = 0.5
ADVANCED_TIME_DELTA = timedelta(days=60)
LATE_TIME_DELTA = timedelta(days=10)


def get_event_from_json(name_of_event):
    with open('it_events.json') as f:
        all_it_events = json.load(f)
        for event in all_it_events:
            if name_of_event == event["name"]:
                return event
        raise Exception(f'there is no event with this name in the nearest future')


class Event:
    def __init__(self, name_of_event):
        event = get_event_from_json(name_of_event)
        self.name = event["name"]
        self.date_of_event = event["date"]
        self.available_num_of_tickets = event["available_num_of_tickets"]
        self.price = event["price"]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise Exception(f'name of event value can\'t be empty')
        if not isinstance(value, str):
            raise Exception(f'name of event value must be a string')
        self.__name = value

    @property
    def date_of_event(self):
        return self.__date_of_event

    @date_of_event.setter
    def date_of_event(self, value):
        try:
            date_of_event = date.fromisoformat(value)
            if date_of_event < date.today():
                raise Exception(f'date of event can\'t be set in past')
            if date_of_event > date.today().replace(year=date.today().year+2):
                raise Exception(f'u can\'t create the event which will occur more than in 2 years')
            self.__date_of_event = date_of_event
        except TypeError:
            print(f'date of event value must be a string')
        except ValueError:
            print(f'the value u passed can\'t be the date of event')

    @property
    def available_num_of_tickets(self):
        return self.__available_num_of_tickets

    @available_num_of_tickets.setter
    def available_num_of_tickets(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u\'re trying to set as an available number of tickets'
                            f'must be an integer')
        if value < 0:
            raise Exception(f'the value, u\'re trying to set as an available number of tickets'
                            f'can\'t be negative')
        self.__available_num_of_tickets = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise Exception(f'price value must be a number')
        if value <= 0:
            raise Exception(f'price value can\'t be less or equal to zero')
        self.__price = value

    def __str__(self):
        return f'event: {self.name}  /  date: {self.date_of_event}\n' \
               f'regular price: {self.price}\n' \
               f'number of tickets that are still available to purchase: {self.available_num_of_tickets}'


class RegularCustomer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise Exception(f'name of the customer can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'name of the customer can\'t contain only 1 letter')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not value.isalpha():
            raise Exception(f'surname of the customer can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'surname of the customer can\'t contain only 1 letter')
        self.__surname = value

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not phonenumbers.is_possible_number(phonenumbers.parse(value)):
            raise Exception(f'invalid phone number was entered')
        self.__mobile_phone = value

    def __str__(self):
        return f'customer: {self.surname} {self.name}  /  cellphone: {self.mobile_phone}\n'


class StudentCustomer(RegularCustomer):
    __students_id = []

    def __init__(self, name, surname, mobile_phone, student_id):
        super().__init__(name, surname, mobile_phone)
        self.student_id = student_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if not str(value).isdigit():
            raise Exception(f'a value passed in the student_id attribute '
                            f'must only consist of digits')
        if not len(str(value)) == 8:
            raise Exception(f'a value passed in the student_id attribute'
                            f'must consist from 8 digits only')
        if value in StudentCustomer.__students_id:
            raise Exception(f'student\'s id must be unique. there can\'t be two students'
                            f'with the same student\'s id')
        else:
            if hasattr(self, "student_id"):
                StudentCustomer.__students_id.remove(self.student_id)
            self.__student_id = value
            StudentCustomer.__students_id.append(value)

    def __str__(self):
        return super().__str__() + f'student\'s id: {self.student_id}'


class Ticket:
    __last_id = 0

    def __init__(self, event, customer):
        if not isinstance(event, Event):
            raise Exception(f'The value u are passing as an event must be an instance of Event class')
        if not isinstance(customer, RegularCustomer | StudentCustomer):
            raise Exception(f'The value u are trying to pass as a customer must be'
                            f'an instance of class Customer or Student_Customer')
        self._name_of_event = event.name
        self._date_of_event = event.date_of_event
        self._price_of_ticket = event.price
        self._name_of_customer = customer.name
        self._surname_of_customer = customer.surname
        self._mobile_phone_of_customer = customer.mobile_phone
        self._ticket_unique_id = Ticket.__last_id
        Ticket.__last_id += 1

    @property
    def name_of_event(self):
        return self._name_of_event

    @property
    def date_of_event(self):
        return self._date_of_event

    @property
    def price_of_ticket(self):
        return self._price_of_ticket

    @property
    def name_of_customer(self):
        return self._name_of_customer

    @property
    def surname_of_customer(self):
        return self._surname_of_customer

    @property
    def mobile_phone_of_customer(self):
        return self._mobile_phone_of_customer

    @property
    def ticket_unique_id(self):
        return self._ticket_unique_id

    def __str__(self):
        return f'type of the ticket: {type(self).__name__}\n' \
               f'unique ticket number: {self.ticket_unique_id}\n' \
               f'price of the ticket: {self.price_of_ticket}\n' \
               f'name of the even: {self.name_of_event}\n' \
               f'date of the event: {self.date_of_event}\n' \
               f'name of the customer: {self.name_of_customer}\n' \
               f'surname of the customer: {self.surname_of_customer}\n' \
               f'mobile phone of the customer: {self.mobile_phone_of_customer}\n'


class RegularTicket(Ticket):
    def __init__(self, event, customer):
        super().__init__(event, customer)


class AdvancedTicket(Ticket):
    def __init__(self, event, customer):
        super().__init__(event, customer)
        self._price_of_ticket *= ADVANCED_PRICE


class LateTicket(Ticket):
    def __init__(self, event, customer):
        super().__init__(event, customer)
        self._price_of_ticket *= LATE_PRICE


class StudentsTicket(Ticket):
    def __init__(self, event, customer):
        super().__init__(event, customer)
        self._price_of_ticket *= STUDENTS_PRICE
        self._student_id = customer.student_id

    @property
    def student_id(self):
        return self._student_id

    def __str__(self):
        return super().__str__() + f'student\'s id: {self.student_id}\n'\



def buy_ticket(event, customer):
    if not isinstance(event, Event):
        raise Exception(f'when buying ticket, the value u pass as an event'
                        f'must be an instance of the class Event')
    if event.available_num_of_tickets == 0:
        raise Exception(f'unfortunately, all the tickets on this event are sold')
    if isinstance(customer, StudentCustomer):
        add_to_json(StudentsTicket(event, customer))
    elif isinstance(customer, RegularCustomer):
        time_before_event = event.date_of_event - date.today()
        if time_before_event > ADVANCED_TIME_DELTA:
            add_to_json(AdvancedTicket(event, customer))
        elif time_before_event < LATE_TIME_DELTA:
            add_to_json(LateTicket(event, customer))
        else:
            add_to_json(RegularTicket(event, customer))
    else:
        raise Exception(f'when buying ticket, the value u pass as a customer'
                        f'must be an instance of the class Customer or any derived class of it')
    event.available_num_of_tickets -= 1


def add_to_json(ticket):
    if not type(ticket).__name__ in ALL_TYPES_OF_TICKETS:
        raise Exception(f'u can only add to json instances of classes: {", ".join(map(str, ALL_TYPES_OF_TICKETS))} ')
    added_ticket_info_dict = {"type of the ticket": type(ticket).__name__,
                              "unique ticket number": ticket.ticket_unique_id,
                              "price of the ticket": ticket.price_of_ticket,
                              "name of the event": ticket.name_of_event,
                              "date of the event": str(ticket.date_of_event),
                              "name of the customer": ticket.name_of_customer,
                              "surname of the customer": ticket.surname_of_customer,
                              "mobile phone of the customer": ticket.mobile_phone_of_customer
                              }
    if type(ticket).__name__ == "StudentsTicket":
        added_ticket_info_dict["student id"] = ticket.student_id
    with open('sold_tickets.json', 'r+') as f:
        file_data = json.load(f)
        file_data["sold tickets"].append(added_ticket_info_dict)
        f.seek(0)
        json.dump(file_data, f, indent=4)


def return_ticket_dict_by_unique_number(unique_ticket_number):
    if not isinstance(unique_ticket_number, int):
        raise Exception(f'a value u passed as a unique ticket number must be an integer')
    if unique_ticket_number < 0:
        raise Exception(f'a value u passed as a unique ticket number can\'t be negative')
    with open('sold_tickets.json', 'r') as f:
        all_sold_tickets = json.load(f)
        for sold_ticket in all_sold_tickets["sold tickets"]:
            if unique_ticket_number == sold_ticket["unique ticket number"]:
                return sold_ticket
        raise Exception(f'there is no ticket with this unique ticket number that was purchased')


def refund_ticket(unique_ticket_number):
    ticket_to_refund = return_ticket_dict_by_unique_number(unique_ticket_number)
    with open('sold_tickets.json', 'r') as fr:
        all_sold_tickets = json.load(fr)
        all_sold_tickets["sold tickets"].remove(ticket_to_refund)
        with open('sold_tickets.json', 'w') as fw:
            json.dump(all_sold_tickets, fw, indent=4)
            return "-"*5 + "the ticket below was refunded" + "-"*5 + "\n" \
                   + "\n".join(map(lambda x, y: f'{x}: {y}', ticket_to_refund.keys(), ticket_to_refund.values())) + '\n'


def get_ticket_info(unique_ticket_number):
    searched_ticket = return_ticket_dict_by_unique_number(unique_ticket_number)
    return "-"*30 + "\n" + "\n".join(map(lambda x, y: f'{x}: {y}', searched_ticket.keys(), searched_ticket.values())) + '\n'


def get_price_of_the_ticket(unique_ticket_number):
    searched_ticket = return_ticket_dict_by_unique_number(unique_ticket_number)
    return f'\nprice of the ticket with the unique number "{unique_ticket_number}": ' \
           f'{searched_ticket["price of the ticket"]}'


def get_current_price_for_event(event):
    tmp = f'current price list: \n'
    time_before_event = event.date_of_event - date.today()
    if time_before_event > ADVANCED_TIME_DELTA:
        tmp += f'\tstandard ticket: {event.price * ADVANCED_PRICE} ' \
               f'({time_before_event.days} days before event)\n'
    elif time_before_event < LATE_TIME_DELTA:
        tmp += f'\tstandard ticket: {event.price * LATE_PRICE} ' \
               f'({time_before_event.days} days before event)\n'
    else:
        tmp += f'\tstandard ticket: {event.price} ' \
               f'({time_before_event.days} days before event)\n'
    tmp += f'\tstudent\'s ticket: {event.price * STUDENTS_PRICE}'
    return tmp


def clear_json():
    empty_json_with_sold_tickets = {"sold tickets": []}
    with open('sold_tickets.json', 'w') as fw:
        json.dump(empty_json_with_sold_tickets, fw, indent=4)


clear_json()
event1 = Event('European DDI User Conference')
event2 = Event('International Conference of Microreaction Technology')

customer1 = RegularCustomer('daniel', 'dziuban', '+380662350484')
customer2 = StudentCustomer('varvara', 'grebenetska', '+380682751113', 13181189)
customer3 = StudentCustomer('vlad', 'bilousov', '+380981481919', 87151634)

buy_ticket(event1, customer1)
buy_ticket(event1, customer3)
buy_ticket(event2, customer2)
buy_ticket(event2, customer3)
buy_ticket(event1, customer2)
buy_ticket(event1, customer1)
buy_ticket(event2, customer1)

print(get_ticket_info(0))
print(refund_ticket(0))
print(refund_ticket(4))
print(get_ticket_info(1))

print(get_current_price_for_event(event2))
print(get_price_of_the_ticket(5))
