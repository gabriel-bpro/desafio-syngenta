# -*- coding: utf-8 -*-

# Dicionário para mapeamento dos dias da semana em weekday/weekend
WEEK = {
    'mon':  'wd',
    'tues': 'wd',
    'wed':  'wd',
    'thur': 'wd',
    'fri':  'wd',
    'sat':  'we',
    'sun':  'we'
}


class Hotel:
    '''
        Classe Hotel, possuindo como atributos o nome, a avaliação e os respectivos preços das diárias para
        tipos de cliente diferentes (Regular ou Rewards).
        Possui os métodos set_price e get_price, nos quais: 
            - set_price: se encarrega de alterar o preço das diárias, recebendo como parâmetro 
            o tipo do cliente e o tipo do dia (se é dia da semana ou final de semana)

            - get_price: método para obter o preço total de um determinado agendamento, levando em consideração
            o tipo do cliente e os dias considerados
    '''
    def __init__(self, name, rating, regular_wd_price, regular_we_price, rewards_wd_price, rewards_we_price):
        self.name = name
        self.rating = rating
        self.prices = {
            'Regular': {'wd': regular_wd_price, 'we': regular_we_price},
            'Rewards': {'wd': rewards_wd_price, 'we': rewards_we_price}
        }

    def set_price(self, client_type, day_type, price):
        self.prices[client_type][day_type] = price

    def get_price(self, client_type, booking):
        total_price = 0

        for day_type in booking:
            total_price += self.prices[client_type][day_type]
        
        return total_price


def get_info(schedule):
    '''
        Função de processamento da entrada:
        Recebe schedule como parâmetro e retorna o tipo do cliente e a lista de dias agendados,
        onde os dias são mapeados ou como weekday ou como weekend
    '''

    split_info = schedule.split(':')
    
    client_type = split_info[0]

    date_list = split_info[1].split(',')
    day_list = []

    for date in date_list:
        day = date[date.find('(')+1:-1]
        day_list.append(WEEK[day])
    
    return client_type, day_list


def get_cheapest_hotel(schedule):   #DO NOT change the function's name

    network = [Hotel("Lakewood", 3, 110, 90, 80, 80), Hotel("Bridgewood", 4, 160, 60, 110, 50), Hotel("Ridgewood", 5, 220, 150, 100, 40)]

    client_type, booking = get_info(schedule)

    budget_list = [(hotel.name, hotel.rating, hotel.get_price(client_type, booking)) for hotel in network]

    # Primeiramente, ordena pela avaliacao do hotel; posteriormente, ordena 
    # pelo preço de maneira decrescente, tal que a ultima posiçao de budget_list
    # possui o hotel com o menor preço e melhor avaliaçao
    sortby_rating = sorted(budget_list, key=lambda budget: budget[1])
    sortby_price = sorted(sortby_rating, key=lambda budget: budget[2], reverse=True)

    cheapest_hotel = sortby_price[-1][0]
    return cheapest_hotel