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

    if client_name in clients:
        clients=clients.replace(client_name+',',updated_client_name+',')
        list_clients()
    else:
        print('Client is not in the clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients=clients.replace(client_name+',','')
        list_clients()
    else:
        print('Client is not in the clients list')



def _add_trailing_comma():
    global clients

    clients+=','


def print_welcome():
    print('Welcome to my store')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead [L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == "__main__":
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
    else:
        print('Command is invalid')
