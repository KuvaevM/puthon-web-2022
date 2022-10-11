# Сравнение баз данных

##  Описание бизнес сценария 

Приложение для интернет магазина. У пользователя есть корзина, в которой лежат отобранные вещи, их можно добавлять и 
удалять. Есть список вещей с определенными характеристиками (цена, название, id, описание). Хочется, чтобы можно было 
делать выборку по предметам на основании определенных критериев (диапазон цены, подстрока в названии или 
описании и тому подобное). Также есть различные подборки (вещи с акциями, вещи для определенного времени года, тому подобное).

## Описание структур данных

* Пользователи. Храним некоторую личную информацию (имя, id, дополнительная информация). Все это изменяем редко. 
У каждого есть список вещей, которые лежат в корзине. Можно добавлять и удалять вещи из корзины (а вот это уже частые действия). 
* Вещи: для каждой вещи храним цену, id, доплнительную информацию (редко изменяем, часто обращаемся). Хотим уметь делать выборку по вещам (достаточно частое действие).
* Подборки: различные выборки вещей (в том числе и пользовательские). Часто изменяем, часто обращаемся.

## Сравнение структур данных

### Redis
Плюсы
* Лицензия BSD
* Высокопроизводительна

Минусы
* Размер БД ограничен доступной памятью
* Отсутствует контроль доступа
* Энергозависима

### MongoDB
Плюсы
* Opensource
* Популярна, есть хорошая документация
* Есть индексация, можно создать индексы для улучшения производительности поиска.
* Хорошо расширяема
* Сохраняет данные в виде документов

Минусы
* Нельзя объединять таблицы
* Медленней, чем предыдущий аналог

### PostgreSQL 

Плюсы
* Opensource
* Популярная, есть много фичей
* Обработка большого объема данных, хорошо расширяема
* Поддержка пользовательских структур данных
* Изначально не была распределенной, но есть поддержка
* Надежная

Минусы
* Медленная (большинство аналогов быстрее).

Исходя из вышенаписанного, для нашей задачи подойдет MongoDB. Мы можем хранить большие объемы данных (так что не подходит Redis), 
но при этом, нам также важна скорость, так что отпадает PostgreSQL. Отметим также, что каталоги товаров удобно хранить в формате таблиц, это еще раз доказывает, что MongoDB подходит.