class ProductCard:
    """Класс карточки товара."""

    def __init__(self, id: int, name: str, quantity: int, status: str,
                 supplier: str, manufacturer: str, price: float,
                 location: str, category: str, min_stock: int = 0) -> None:
        """Инициализация карточки товара.

        Args:
            id: Уникальный идентификатор.
            name: Наименование товара.
            quantity: Количество на складе.
            status: Статус товара.
            supplier: Поставщик.
            manufacturer: Производитель.
            price: Цена за единицу.
            location: Местоположение на складе.
            category: Категория товара.
            min_stock: Минимальный запас.
        """
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__status = status
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__category = category
        self.__min_stock = min_stock
        self.__note = ""

    def get_id(self) -> int:
        """Геттер для id."""
        return self.__id

    def get_name(self) -> str:
        """Геттер для наименования."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Сеттер для наименования.

        Args:
            name: Новое наименование.

        Raises:
            ValueError: Если имя пустое.
        """
        if not name or not name.strip():
            raise ValueError('наименование не может быть пустым')
        self.__name = name.strip()

    def get_quantity(self) -> int:
        """Геттер для количества."""
        return self.__quantity

    def set_quantity(self, quantity: int) -> None:
        """Сеттер для количества.

        Args:
            quantity: Новое количество.

        Raises:
            ValueError: Если количество отрицательное.
        """
        if quantity < 0:
            raise ValueError('количество не может быть отрицательным')
        self.__quantity = quantity

    def get_status(self) -> str:
        """Геттер для статуса."""
        return self.__status

    def set_status(self, status: str) -> None:
        """Сеттер для статуса.

        Args:
            status: Новый статус.

        Raises:
            ValueError: Если статус не из списка.
        """
        valid_statuses = {'черновик', 'ожидает', 'принято', 'списано', 'резерв'}
        if status not in valid_statuses:
            raise ValueError('статус должен быть: черновик, ожидает, принято, списано, резерв')
        self.__status = status

    def get_supplier(self) -> str:
        """Геттер для поставщика."""
        return self.__supplier

    def set_supplier(self, supplier: str) -> None:
        """Сеттер для поставщика.

        Args:
            supplier: Новый поставщик.

        Raises:
            ValueError: Если поставщик пустой.
        """
        if not supplier or not supplier.strip():
            raise ValueError('поставщик не может быть пустым')
        self.__supplier = supplier.strip()

    def get_manufacturer(self) -> str:
        """Геттер для производителя."""
        return self.__manufacturer

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для производителя.

        Args:
            manufacturer: Новый производитель.

        Raises:
            ValueError: Если производитель пустой.
        """
        if not manufacturer or not manufacturer.strip():
            raise ValueError('производитель не может быть пустым')
        self.__manufacturer = manufacturer.strip()

    def get_price(self) -> float:
        """Геттер для цены."""
        return self.__price

    def set_price(self, price: float) -> None:
        """Сеттер для цены.

        Args:
            price: Новая цена.

        Raises:
            ValueError: Если цена отрицательная.
        """
        if price < 0:
            raise ValueError('цена не может быть отрицательной')
        self.__price = price

    def get_location(self) -> str:
        """Геттер для местоположения."""
        return self.__location

    def set_location(self, location: str) -> None:
        """Сеттер для местоположения.

        Args:
            location: Новое местоположение.

        Raises:
            ValueError: Если местоположение пустое.
        """
        if not location or not location.strip():
            raise ValueError('местоположение не может быть пустым')
        self.__location = location.strip()

    def get_category(self) -> str:
        """Геттер для категории."""
        return self.__category

    def set_category(self, category: str) -> None:
        """Сеттер для категории.

        Args:
            category: Новая категория.

        Raises:
            ValueError: Если категория пустая.
        """
        if not category or not category.strip():
            raise ValueError('категория не может быть пустой')
        self.__category = category.strip()

    def get_min_stock(self) -> int:
        """Геттер для минимального запаса."""
        return self.__min_stock

    def set_min_stock(self, min_stock: int) -> None:
        """Сеттер для минимального запаса.

        Args:
            min_stock: Новый минимальный запас.

        Raises:
            ValueError: Если запас отрицательный.
        """
        if min_stock < 0:
            raise ValueError('минимальный запас не может быть отрицательным')
        self.__min_stock = min_stock

    def get_note(self) -> str:
        """Геттер для заметки."""
        return self.__note

    def set_note(self, note: str) -> None:
        """Сеттер для заметки."""
        self.__note = note.strip()

    def write_off(self, reason: str = "") -> None:
        """Списать товар.

        Args:
            reason: Причина списания.

        Raises:
            ValueError: Если статус товара не 'принято'.
        """
        if self.__status != 'принято':
            raise ValueError('списать можно только товар со статусом принято')

        self.__status = 'списано'
        self.__quantity = 0
        self.__note = f"Списано: {reason}" if reason else "Списано"

    def reserve(self, amount: int) -> None:
        """Зарезервировать товар.

        Args:
            amount: Количество для резерва.

        Raises:
            ValueError: Если товар не принят или недостаточно.
        """
        if self.__status != 'принято':
            raise ValueError('резервировать можно только принятые товары')
        if amount <= 0:
            raise ValueError('количество должно быть положительным')
        if amount > self.__quantity:
            raise ValueError(f'недостаточно товара, доступно {self.__quantity}')

        self.__quantity -= amount
        self.__status = 'резерв'
        self.__note = f"Зарезервировано {amount} шт."

    def to_dict(self) -> dict:
        """Преобразовать в словарь."""
        return {
            'id': self.__id,
            'name': self.__name,
            'quantity': self.__quantity,
            'status': self.__status,
            'supplier': self.__supplier,
            'manufacturer': self.__manufacturer,
            'price': self.__price,
            'location': self.__location,
            'category': self.__category,
            'min_stock': self.__min_stock,
            'note': self.__note
        }

    def show(self) -> None:
        """Показать карточку."""
        print(f'ID: {self.__id}')
        print(f'Наименование: {self.__name}')
        print(f'Количество: {self.__quantity}')
        print(f'Статус: {self.__status}')
        print(f'Поставщик: {self.__supplier}')
        print(f'Производитель: {self.__manufacturer}')
        print(f'Цена: {self.__price:.2f} руб.')
        print(f'Местоположение: {self.__location}')
        print(f'Категория: {self.__category}')
        print(f'Мин. запас: {self.__min_stock}')
        if self.__note:
            print(f'Заметка: {self.__note}')
        print('-' * 40)


# Хранилище
products = []
next_id = 1


def create_card() -> None:
    """Создание новой карточки."""
    global next_id
    print('\n--- Новая карточка ---')
    try:
        name = input('Наименование: ').strip()
        if not name:
            raise ValueError('наименование обязательно')

        quantity = int(input('Количество: '))
        supplier = input('Поставщик: ').strip()
        if not supplier:
            raise ValueError('поставщик обязателен')

        manufacturer = input('Производитель: ').strip()
        if not manufacturer:
            raise ValueError('производитель обязателен')

        price = float(input('Цена: '))
        location = input('Местоположение: ').strip()
        if not location:
            raise ValueError('местоположение обязательно')

        category = input('Категория: ').strip()
        if not category:
            raise ValueError('категория обязательна')

        min_stock = input('Мин. запас (Enter - 0): ').strip()
        min_stock = int(min_stock) if min_stock else 0

        card = ProductCard(
            id=next_id,
            name=name,
            quantity=quantity,
            status='черновик',
            supplier=supplier,
            manufacturer=manufacturer,
            price=price,
            location=location,
            category=category,
            min_stock=min_stock
        )

        products.append(card)
        print(f'Карточка создана с id {next_id}')
        next_id += 1

    except ValueError as e:
        print(f'Ошибка: {e}')


def show_all() -> None:
    """Показать все карточки."""
    if not products:
        print('\nКарточек нет')
        return

    print('\n--- Все карточки ---')
    for card in products:
        print(f'[{card.get_id()}] {card.get_name()} | {card.get_quantity()} шт | {card.get_status()}')


def find_card() -> ProductCard | None:
    """Найти карточку по id."""
    try:
        id = int(input('Введите id карточки: '))
        for card in products:
            if card.get_id() == id:
                return card
        print('Карточка не найдена')
        return None
    except ValueError:
        print('Ошибка: id должно быть числом')
        return None


def show_card() -> None:
    """Показать карточку."""
    card = find_card()
    if card:
        card.show()


def edit_card() -> None:
    """Редактирование карточки."""
    card = find_card()
    if not card:
        return

    if card.get_status() == 'списано':
        print('Нельзя редактировать списанный товар')
        return

    print('Enter - оставить без изменений')

    fields = [
        ('наименование', card.get_name(), str, card.set_name),
        ('количество', card.get_quantity(), int, card.set_quantity),
        ('статус', card.get_status(), str, card.set_status),
        ('поставщик', card.get_supplier(), str, card.set_supplier),
        ('производитель', card.get_manufacturer(), str, card.set_manufacturer),
        ('цена', card.get_price(), float, card.set_price),
        ('местоположение', card.get_location(), str, card.set_location),
        ('категория', card.get_category(), str, card.set_category),
        ('мин запас', card.get_min_stock(), int, card.set_min_stock),
        ('заметка', card.get_note(), str, card.set_note),
    ]

    try:
        for name, old, typ, setter in fields:
            val = input(f'{name} ({old}): ').strip()
            if val:
                if typ is int:
                    setter(int(val))
                elif typ is float:
                    setter(float(val))
                else:
                    setter(val)
        print('Данные обновлены')
    except ValueError as e:
        print(f'Ошибка: {e}')


def accept_card() -> None:
    """Принять товар на учёт."""
    card = find_card()
    if not card:
        return

    try:
        if card.get_status() == 'списано':
            print('Нельзя принять списанный товар')
            return

        card.set_status('принято')
        print('Товар принят на учёт')
    except ValueError as e:
        print(f'Ошибка: {e}')


def reserve_card() -> None:
    """Зарезервировать товар."""
    card = find_card()
    if not card:
        return

    try:
        amount = int(input('Сколько зарезервировать: '))
        card.reserve(amount)
        print('Товар зарезервирован')
    except ValueError as e:
        print(f'Ошибка: {e}')


def write_off_card() -> None:
    """Списать товар."""
    card = find_card()
    if not card:
        return

    try:
        reason = input('Причина списания (Enter - без причины): ').strip()
        card.write_off(reason)
        print('Товар списан')
    except ValueError as e:
        print(f'Ошибка: {e}')


def search_by_category() -> None:
    """Поиск по категории."""
    cat = input('Введите категорию: ').strip().lower()
    found = []

    for card in products:
        if cat in card.get_category().lower():
            found.append(card)

    if not found:
        print('Товары не найдены')
        return

    print(f'\nНайдено {len(found)} товаров:')
    for card in found:
        print(f'[{card.get_id()}] {card.get_name()} | {card.get_quantity()} шт | {card.get_price():.2f} руб.')


def check_min_stock() -> None:
    """Проверить минимальный запас."""
    print('\nТовары с недостатком:')
    found = False

    for card in products:
        if card.get_status() == 'принято' and card.get_quantity() < card.get_min_stock():
            print(f'[{card.get_id()}] {card.get_name()} - {card.get_quantity()} шт (мин. {card.get_min_stock()})')
            found = True

    if not found:
        print('Всех товаров достаточно')


def delete_card() -> None:
    """Удалить карточку."""
    card = find_card()
    if not card:
        return

    print(f'\nУдалить товар: {card.get_name()}?')
    confirm = input('Введите "ДА" для подтверждения: ').strip()

    if confirm == 'ДА':
        products.remove(card)
        print('Карточка удалена')
    else:
        print('Удаление отменено')


def main() -> None:
    """Главное меню."""
    while True:
        print('\n=== Учёт товаров ===')
        print('1. Создать карточку')
        print('2. Показать все')
        print('3. Показать карточку')
        print('4. Редактировать')
        print('5. Принять на учёт')
        print('6. Зарезервировать')
        print('7. Списать товар')
        print('8. Поиск по категории')
        print('9. Проверить запас')
        print('10. Удалить карточку')
        print('0. Выход')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            create_card()
        elif choice == '2':
            show_all()
        elif choice == '3':
            show_card()
        elif choice == '4':
            edit_card()
        elif choice == '5':
            accept_card()
        elif choice == '6':
            reserve_card()
        elif choice == '7':
            write_off_card()
        elif choice == '8':
            search_by_category()
        elif choice == '9':
            check_min_stock()
        elif choice == '10':
            delete_card()
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неверный ввод')


if __name__ == '__main__':
    main()