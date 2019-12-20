clients = 'Pablo,Ricardo'


def list_clients():
    global clients

    print('Clients list: ',clients)


def create_client(client_name):
    global clients

    if client_name not in clients:
        _add_trailing_comma()
        clients+=client_name
        print('*'*50)
        print(client_name,'added to database')
    else:
        print(client_name+' already in database')

    print('*'*50)




def _add_trailing_comma():
    global clients

    clients+=','


def print_welcome():
    print('Welcome to my store')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == "__main__":
    print_welcome()

    command = input()

    if command=='C':
        client_name=input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command=='D':
        pass
    else:
        print('Command is invalid')
