import sys
import csv
import os

CLIENT_TABLE='.clients.csv'
CLIENT_SCHEMA=['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    temp_table_name='{}.tmp'.format(CLIENT_TABLE)
    with open(temp_table_name,mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(temp_table_name,CLIENT_TABLE)



def list_clients():
    global clients

    for idx, client in enumerate(clients):

        print('{idx}: {name}, {position} at {company}'.format(
            idx=idx, 
            name=client['name'], 
            position=client['position'], 
            company=client['company'],
        ))

        # print('{idx}: {name}, {company} {position} {email}'.format(
        #     idx=idx, 
        #     name=client['name'], 
        #     company=client['company'],
        #     email=client['email'], 
        #     position=client['position'], 
        # ))




def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print(client_name+' already in database')

    print('*'*50)


def update_client(client_name,updated_client):
    global clients

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            clients[idx]=updated_client
        _client_not_found(client_name)


def delete_client(client_name):
    global clients
    print('delete_clients')

    for idx, client in enumerate(clients):
        if clients[idx]['name'] == client_name:
            popped = clients.pop(idx)
            print('found client ', popped)
        else:
            _client_not_found(client_name)


def search_client(client_name):
    global clients

    for idx, client in enumerate(clients):
        if clients[idx]['name'] == client_name:
            return True        
    return False


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}? '.format(field_name))
    return field


def _get_client():

    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _get_client_name():
    client_name=None
    while not client_name:
        client_name = input('What is the client name? ')
    return client_name


def _client_not_found(client_name):
    if client_name:
        print('Client '+client_name+' is not in the clients list')
    else:
        print('Client is not in clients list')



def print_welcome():
    print('\n'*3)
    print('Welcome to my store')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead [L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[Q]uit')
    print('')


if __name__ == "__main__":

    _initialize_clients_from_storage()

    command=False
    while not command:

        print_welcome()
        
        command = input()
        command = command.upper()

    if command=='C':
        create_client( _get_client() )
    elif command=='L' or command=='R':
        list_clients()
    elif command=='U':
        client_name=_get_client_field('name')
        updated_client=_get_client()
        update_client(client_name,updated_client)
    elif command=='D':
        client_name=_get_client_name()
        delete_client(client_name)
    elif command=='S':
        client_name=_get_client_name()
        found=search_client(client_name)

        if found:
            print('Client '+client_name+' is in the client list')
        else:
            print('Client {} is not in the client\s list'.format(client_name))

    elif command=='Q':
        print('Thank you for your time, please come back later')
    else:
        print('Command is invalid')

    _save_clients_to_storage()
