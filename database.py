# ---- Database Documentation ----
"""
Module used to manage the data.
"""
# ---- End Database Documentation ----

# ---- Imports ----
import csv
import config
# ---- End Imports ----

class Client:

    def __init__(self, ssn, name, last_name):
        self.ssn = ssn
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"({self.ssn}) {self.name} {self.last_name}"

class Clients:

    l = []  # Client's list
    with open(config.DATABASE_PATH, newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        for ssn, name, last_name in reader:
            client = Client(ssn, name, last_name)
            l.append(client)

    @staticmethod
    def search(ssn):
        """
        This function receive a ssn, search in the
        list of clients in the class Clients and return
        that client if the ssn matches.
        :param ssn: social security number ()
        :return: Client Object
        """
        for client in Clients.l:
            if client.ssn == ssn:
                return client

    @staticmethod
    def create(ssn, name, last_name):
        """
        This function create a Client object with
        the received information and add it to the
        list in Clients (l).
        :param ssn: social security number ()
        :param name: name of the client string
        :param last_name: last name of the client string
        :return: The created Client object (client)
        """
        client = Client(ssn, name, last_name)
        Clients.l.append(client)
        Clients.save()
        return client

    @staticmethod
    def modify(ssn, name, last_name):
        """
        This function searches for a specific Client
        object based on the received ssn, and changes
        the parameter "first name" and "last name"
        with those received.
        :param ssn: social security number ()
        :param name: name of the client string
        :param last_name: last name of the client string
        :return: The updated Client object
        """
        for i,client in enumerate(Clients.l):
            if client.ssn == ssn:
                Clients.l[i].name = name
                Clients.l[i].last_name = last_name
                Clients.save()
                return Clients.l[i]

    @staticmethod
    def delete(ssn):
        """
        This function searches for a specific Client
        Object based on the received ssn, and delete
        that specific client. Then return it.
        :param ssn: social security number ()
        :return: The deleted Client Object
        """
        for i, client in enumerate(Clients.l):
            if client.ssn == ssn:
                dclient = Clients.l.pop(i)
                Clients.save()
                return dclient

    @staticmethod
    def save():
        with open(config.DATABASE_PATH, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')

            for client in Clients.l:
                writer.writerow( (client.ssn, client.name, client.last_name) )