def count_marks(class_register: dict) -> dict:
    # write your code here
    mark_dict = {}
    for k, v in class_register.items():
        mark_dict[v] += 1
        print(mark_dict)


class_register = {
    "Sergey": 8,
    "Maria": 12,
    "Daria": 11,
    "Oleg": 5,
    "Victor": 8,
    "Alexandr": 11,
}

count_marks(class_register)
