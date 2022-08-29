import enum
import os
import csv
import sys

CLIENT_TABLE = '.clients.csv' # los archivos con punto inicial, hacen referencia a un archivo oculto.
CLIENT_SCHEMA = ['name', 'company', 'email', 'position'] # es una lista de las llaves que a a utilizar CSV para contruir diccionaris 
clients = []

def _initialize_client_form_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)#parametrofielname una lista para crear las llaves de el diccionario 
        for row in reader:
           clients.append(row)
            
            
def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w')as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)#rows cuando son 2 y row 1 
        
        os.remove(CLIENT_TABLE) #permite manipular el sistema operativo
    os.rename(tmp_table_name, CLIENT_TABLE)# para que se borre y se remplace cada vez que se utilice


def create_client(client):
    global clients 
    
    if client not in clients:
        clients.append(client)
        
        print(' Client alredy is  in the client\'s list')

def list_client():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
        uid=idx, 
        name=client['name'], 
        company=client['company'], 
        email=client['email'], 
        
        position=client['position']))

def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _not_client_list()


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
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


def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client 


def _not_client_list():
    return input('Clients is not in clients list')


if __name__ == '__main__':
    _initialize_client_form_storage()
    
    _print_welcome()
    command= input()
    command = command.upper()
    list_client()
    
    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        
    elif command == 'L':
         list_client()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
        
_save_clients_to_storage()
    