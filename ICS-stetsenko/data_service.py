"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""


def get_clients():
    """ Довідник показників рядків балансу

    Returns:
        client_list: список клієнтів 
    """    

    from_file = [
        "120; Залишкова вартість МБП",
        "170; Витрати обігу на залишок товарів",
        "200; За товари, роботи, послуги",
        "210; З персоналом",
        "230; З бюджетом",
        "240; З персоналом по іншим операціям",
        "290; Каса",
        "300; Розрахунковий рахунок",
        "310; Валютний рахунок",
        "160; Купівельна вартість товарів",
        "320; Інші грошові кошти"
    ]

    # накопичувач клієнтів
    clients_list = []

    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)
    
    return clients_list

def show_clients(clients):
    """виводить на екран список клієнтів заданого діапазона

    Args:
        clients ([list]): список клієнтів
    """

    client_code_from = input("З якого кода? ")
    client_code_to   = input("По який код? ") 

    for client in clients:
        if  client_code_from <= client[0] <= client_code_to: 
            print("код: {:4} назва: {:17} адреса: {:20}".format(client[0], client[1], client[2]))



clients = get_clients()
show_clients(clients)
