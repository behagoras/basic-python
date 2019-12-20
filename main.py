clients = 'Pablo,Ricardo,'


def list_clients():
    global clients

    print('Clients list: ',clients)


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients+=client_name
        _add_trailing_comma()
        print('*'*50)
        print(client_name,'added to database')
    else:
        print(client_name+' already in database')

    print('*'*50)


def update_client(client_name,updated_client_name):
    global clients

    if client_name.upper() in clients.upper():
        clients=clients.replace(client_name+',',updated_client_name+',')
        list_clients()
    else:
        _client_not_found(client_name)


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients=clients.replace(client_name+',','')
        list_clients()
    else:
        _client_not_found(client_name)


def search_client(client_name):
    global clients

    clients_list = clients.split(',')

    for client in clients_list:
        if client.upper() == client_name.upper():
            return True

    return False
    # return client_name in clients # This line does the same


def _add_trailing_comma():
    global clients

    clients+=','


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

    while True:

        command=False
        while not command:

            print_welcome()
            
            command = input()
            command = command.upper()

        if command=='C':
            client_name=_get_client_name()
            create_client(client_name)
            list_clients()
        elif command=='R':
            list_clients()
        elif command=='L':
            list_clients()
        elif command=='U':
            client_name=_get_client_name()
            updated_client_name=input('What is the updated client name? ')
            update_client(client_name,updated_client_name)
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
            break
        else:
            print('Command is invalid')
