

# Завдання 1
def total_salary(path: str) -> tuple:
    try:
        total = 0
        with open(path, "r", encoding = "utf-8") as fh:
            lines = fh.readlines()
            if len(lines) == 0:
                return (0, 0) 
            for item in lines:
                _, salary = item.split(",")
                total += int(salary)
            return (total, total / len(lines)) 
    except Exception as e:
        print(f"Error occurred: {e}")
        return (0, 0) 

total, average = total_salary("salary_file.txt")
#print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Завдання 2
def get_cats_info(path: str) -> list:
    try:
        result = []
        with open(path, "r", encoding = "utf-8") as fh:
            lines = fh.readlines()
            for item in lines:
                id, name, age = item.strip().split(",")
                result.append({"id": id, "name": name, "age": age})
            return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    
cats_info = get_cats_info("cats_file.txt")
#print(*cats_info, sep='\n')
