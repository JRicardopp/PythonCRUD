import sys

clients = ['pablo', 'ricardo']

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
    else:
        print(' Client alredy is  in the client\'s list')

def list_client():
    for idx, client in enumerate(clients):
        print ('{}: {}'.format(idx, client))

def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        index =  clients.index(client_name)
        clients[index] = update_client_name     
    else:
        _not_client_list()


def delete_client(cleint_name):
    global clients
    
    if client_name in clients:
        clients.remove(cleint_name)
    else:
        _not_client_list()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue ## no ejecuetes nadamas hasta la siguiente la iteracion
        else:
            return True
            

def _print_welcome():
    print('Welcome To Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]eate client')
    print('[L]ist client')
    print('[U]pdate.client')
    print('[D]elete client')
    print('[S]earch client')
    

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the clien name? ')
        
        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()
    
    return client_name

def _not_client_list():
    return input('Clients is not in clients list')


if __name__ == '__main__':
    _print_welcome()
    command= input()
    command = command.upper()
    list_client()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_client()
    elif command == 'L':
        list_client()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f'The client {client_name} is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('Invalid command')