class Warehouses:
    def __init__(self, warehouse, product, quantity):
        self.warehouse = warehouse
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return (f"Склад {self.warehouse}: Продукты: {self.product}, Количество: {self.quantity}")


warehouses = [
    Warehouses(1, ["Молоко", "Каша", "Бананы"], [10, 50, 30]),
    Warehouses(2, ["Помидоры", "Огурцы", "Бананы"], [30, 60, 30]),
    Warehouses(3, ["Чеснок", "Яблоки", "Груши"], [10, 20, 35])
]


def show_menu():
    print("\nМеню:")
    print("1. Добавить склад")
    print("2. Вывести список складов")
    print("3. Изменить текущий склад")
    print("4. Выйти")


def add_warehouse():
    warehouse_number = len(warehouses) + 1
    new_products = input("Введите продукты через запятую: ").split(',')
    new_quantities = list(map(int, input("Введите новое количество через запятую: ").split(',')))

    # Исправлено: используем new_products и new_quantities
    warehouses.append(Warehouses(warehouse_number, new_products, new_quantities))
    print(f"Склад {warehouse_number} добавлен.")


def list_warehouses():
    for warehouse in warehouses:
        print(warehouse)


def edit_warehouse():
    try:
        warehouse_number = int(input("Выберите номер склада для изменения: "))
        warehouse = next((w for w in warehouses if w.warehouse == warehouse_number), None)

        if not warehouse:
            print("Склад с таким номером не найден.")
            return

        print("Текущая информация о складе: ")
        print(warehouse)

        new_products = input("Введите новые продукты через запятую (оставьте пустым для сохранения текущих): ").strip()
        new_quantities = input(
            "Введите новое количество через запятую (оставьте пустым для сохранения текущих): ").strip()

        if new_products:
            warehouse.product = new_products.split(',')
        if new_quantities:
            warehouse.quantity = list(map(int, new_quantities.split(',')))

        print("Информация о складе обновлена.")

    except ValueError:
        print("Ошибка ввода. Убедитесь, что вы вводите корректные данные.")


def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            add_warehouse()
        elif choice == "2":
            list_warehouses()
        elif choice == "3":
            edit_warehouse()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()