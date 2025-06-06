"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    

baza=[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


for slov in baza:
    

    print(slov['product'],"всего продано: ", (sum(slov['items_sold'])))
    print(slov['product'],"в среднем продано: ", (sum(slov['items_sold'])/len(slov['items_sold'])))

mylist=[]
for slov in baza:
    mylist.append(sum(slov['items_sold']))
print('Всего телефонов продано: ', sum(mylist))

mylist=[]
for slov in baza:
    mylist.append(sum(slov['items_sold'])/len(slov['items_sold']))
print("Среднее количество продаж всех телефонов: ", sum(mylist))






    





   

    #print(len(slov['items_sold']))


#print(sum(baza[0]['items_sold']))
    
if __name__ == "__main__":
    main()
