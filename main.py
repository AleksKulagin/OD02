# Реализация стека с помощью списка
class Stack:
    def __init__(self):
        # Инициализация пустого списка для хранения элементов стека
        self.items = []

    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.items) == 0

    def push(self, item):
        # Добавление элемента в стек (в конец списка)
        self.items.append(item)

    def pop(self):
        # Удаление и возврат последнего элемента стека (последнего элемента списка)
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.items.pop()

    def peek(self):
        # Возврат последнего элемента стека без его удаления
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент в пустом стеке")
        return self.items[-1]

    def size(self):
        # Возврат текущего размера стека
        return len(self.items)

    def __str__(self):
        # Возврат строкового представления стека для удобства вывода
        return str(self.items)


# Реализация очереди с помощью списка
class Queue:
    def __init__(self):
        # Инициализация пустого списка для хранения элементов очереди
        self.items = []

    def is_empty(self):
        # Проверка, пуста ли очередь
        return len(self.items) == 0

    def enqueue(self, item):
        # Добавление элемента в очередь (в конец списка)
        self.items.append(item)

    def dequeue(self):
        # Удаление и возврат первого элемента очереди (первого элемента списка)
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустой очереди")
        return self.items.pop(0)

    def peek(self):
        # Возврат первого элемента очереди без его удаления
        if self.is_empty():
            raise IndexError("Попытка посмотреть элемент в пустой очереди")
        return self.items[0]

    def size(self):
        # Возврат текущего размера очереди
        return len(self.items)

    def __str__(self):
        # Возврат строкового представления очереди для удобства вывода
        return str(self.items)


# Реализация бинарного дерева
class TreeNode:
    def __init__(self, value):
        # Инициализация узла дерева с значением и ссылками на левого и правого потомков
        self.value = value
        self.left = None
        self.right = None


# Реализация графа с использованием списка смежности
class Graph:
    def __init__(self):
        # Инициализация графа как словаря, где ключи — вершины, а значения — списки смежных вершин
        self.graph = {}

    def add_vertex(self, vertex):
        # Добавление новой вершины в граф
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Добавление ребра между двумя вершинами
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def __str__(self):
        # Возврат строкового представления графа
        return "\n".join([f"{vertex}: {neighbors}" for vertex, neighbors in self.graph.items()])


# Функция для демонстрации работы стека
def demonstrate_stack():
    stack = Stack()
    print("\nДемонстрация работы стека.")
    while True:
        print("\nТекущий стек:", stack)
        action = input("Введите команду (push, pop, peek, size, exit): ").strip().lower()
        if action == "push":
            item = input("Введите элемент для добавления в стек: ")
            stack.push(item)
        elif action == "pop":
            try:
                print("Извлеченный элемент:", stack.pop())
            except IndexError as e:
                print(e)
        elif action == "peek":
            try:
                print("Верхний элемент стека:", stack.peek())
            except IndexError as e:
                print(e)
        elif action == "size":
            print("Размер стека:", stack.size())
        elif action == "exit":
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")


# Функция для демонстрации работы очереди
def demonstrate_queue():
    queue = Queue()
    print("\nДемонстрация работы очереди.")
    while True:
        print("\nТекущая очередь:", queue)
        action = input("Введите команду (enqueue, dequeue, peek, size, exit): ").strip().lower()
        if action == "enqueue":
            item = input("Введите элемент для добавления в очередь: ")
            queue.enqueue(item)
        elif action == "dequeue":
            try:
                print("Извлеченный элемент:", queue.dequeue())
            except IndexError as e:
                print(e)
        elif action == "peek":
            try:
                print("Первый элемент очереди:", queue.peek())
            except IndexError as e:
                print(e)
        elif action == "size":
            print("Размер очереди:", queue.size())
        elif action == "exit":
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")


# Функция для демонстрации работы бинарного дерева
def demonstrate_tree():
    print("\nДемонстрация работы бинарного дерева.")
    root = TreeNode(1)  # Создаем корень дерева
    root.left = TreeNode(2)  # Левый потомок корня
    root.right = TreeNode(3)  # Правый потомок корня
    root.left.left = TreeNode(4)  # Левый потомок левого потомка
    root.left.right = TreeNode(5)  # Правый потомок левого потомка

    print("Структура дерева:")
    print(f"        {root.value}")
    print(f"      /   \\")
    print(f"    {root.left.value}       {root.right.value}")
    print(f"  /   \\")
    print(f"{root.left.left.value}       {root.left.right.value}")


# Функция для демонстрации работы графа
def demonstrate_graph():
    graph = Graph()
    print("\nДемонстрация работы графа.")
    while True:
        print("\nТекущий граф:")
        print(graph)
        action = input("Введите команду (add_vertex, add_edge, exit): ").strip().lower()
        if action == "add_vertex":
            vertex = input("Введите вершину для добавления: ")
            graph.add_vertex(vertex)
        elif action == "add_edge":
            vertex1 = input("Введите первую вершину: ")
            vertex2 = input("Введите вторую вершину: ")
            graph.add_edge(vertex1, vertex2)
        elif action == "exit":
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")


# Основное меню для выбора структуры данных
def main():
    while True:
        print("\nВыберите структуру данных для демонстрации:")
        print("1. Стек")
        print("2. Очередь")
        print("3. Бинарное дерево")
        print("4. Граф")
        print("5. Выход")
        choice = input("Введите номер: ").strip()
        if choice == "1":
            demonstrate_stack()
        elif choice == "2":
            demonstrate_queue()
        elif choice == "3":
            demonstrate_tree()
        elif choice == "4":
            demonstrate_graph()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()