import threading
import random
import time
from statistics import mean
#task1
numbers = []
user_input = input("Enter numbers separated by spaces: ")
input_numbers = user_input.split()

for number in input_numbers:
    numbers.append(int(number))

def find_minimum():
    print("Minimum:", min(numbers))

def find_maximum():
    print("Maximum:", max(numbers))

min_thread = threading.Thread(target=find_minimum)
max_thread = threading.Thread(target=find_maximum)

min_thread.start()
max_thread.start()

min_thread.join()
max_thread.join()

#task2
numbers = []
user_input = input("Enter numbers separated by spaces: ")
input_numbers = user_input.split()

for number in input_numbers:
    numbers.append(int(number))

def calculate_sum():
    print("Sum:", sum(numbers))

def calculate_average():
    print("Average:", mean(numbers))

sum_thread = threading.Thread(target=calculate_sum)
average_thread = threading.Thread(target=calculate_average)

sum_thread.start()
average_thread.start()

sum_thread.join()
average_thread.join()

#task3
file_path = input("Enter the file path: ")
def process_even_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = file.read()
            numbers_list = map(int, numbers.split())

        with open("even_numbers.txt", "w") as even_file:
            for number in numbers_list:
                if number % 2 == 0:
                    even_file.write(f"{number}\n")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def process_odd_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = file.read()
            numbers_list = map(int, numbers.split())

        with open("odd_numbers.txt", "w") as odd_file:
            for number in numbers_list:
                if number % 2 != 0:
                    odd_file.write(f"{number}\n")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


even_thread = threading.Thread(target=process_even_numbers, args=(file_path,))
odd_thread = threading.Thread(target=process_odd_numbers, args=(file_path,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Process complete!")

#task4
import threading

def read_and_search(file_path, search_word, start_pos, end_pos):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.seek(start_pos)
            content = file.read(end_pos - start_pos)
            if search_word in content:
                print(f"Found the word: {search_word}")
            else:
                print("Word not found in this part of the file.")
    except Exception as e:
        print(f"Problem: {e}")

def main():
    file_path = input("Enter the path to your file: ")
    search_word = input("Enter the word to find: ")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.seek(0, 2)
            file_size = file.tell()
            mid_point = file_size // 2
    except Exception as e:
        print(f"Problem: {e}")
        return

    thread1 = threading.Thread(target=read_and_search, args=(file_path, search_word, 0, mid_point))
    thread2 = threading.Thread(target=read_and_search, args=(file_path, search_word, mid_point, file_size))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Search completed.")

main()

#HW
#task1HW
numbers = []
list_filled = threading.Event()

def fill_list():
    global numbers
    for _ in range(10):
        numbers.append(random.randint(1, 100))
        time.sleep(0.5)
    list_filled.set()

def calculate_sum():
    list_filled.wait()
    total_sum = sum(numbers)
    print(f"Сумма елементів списку: {total_sum}")
def calculate_average():
    list_filled.wait()
    average = mean(numbers)
    print(f"Середнє арифметичне: {average}")

thread1 = threading.Thread(target=fill_list)
thread2 = threading.Thread(target=calculate_sum)
thread3 = threading.Thread(target=calculate_average)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f"Заповнений список: {numbers}")

#task2HW

primes_file = "primes.txt"
factorials_file = "factorials.txt"
file_filled = threading.Event()

def fill_file(path):
    with open(path, 'w') as f:
        for _ in range(10):
            f.write(f"{random.randint(1, 100)}\n")
            time.sleep(0.5)
    file_filled.set()

def find_primes(path):
    file_filled.wait()
    with open(path, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    primes = [num for num in numbers if is_prime(num)]

    with open(primes_file, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")

    print(f"Знайдені прості числа: {primes}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorials(path):
    file_filled.wait()
    with open(path, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    factorials = [factorial(num) for num in numbers]

    with open(factorials_file, 'w') as f:
        for fact in factorials:
            f.write(f"{fact}\n")

    print(f"Факторіали: {factorials}")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

file_path = input("Enter the file path: ")

thread1 = threading.Thread(target=fill_file, args=(file_path,))
thread2 = threading.Thread(target=find_primes, args=(file_path,))
thread3 = threading.Thread(target=calculate_factorials, args=(file_path,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

#task3HW
def fill_file_with_numbers(file_path):
    try:
        with open(file_path, "w") as f:
            for _ in range(100):
                f.write(f"{random.randint(1, 100)}\n")
        print(f"Файл {file_path} заповнений.")
    except Exception as e:
        print(f"Помилка: {e}")

def find_prime_numbers(file_path, event):
    try:
        with open(file_path, "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]

        primes = [n for n in numbers if is_prime(n)]

        with open("prime_numbers.txt", "w") as out_file:
            for prime in primes:
                out_file.write(f"{prime}\n")

        print(f"Прості числа записані в prime_numbers.txt.")
        event.set()
    except Exception as e:
        print(f"Помилка: {e}")

def find_factorial_numbers(file_path, event):
    try:
        event.wait()
        with open(file_path, "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]

        factorials = [factorial(n) for n in numbers]

        with open("factorial_numbers.txt", "w") as out_file:
            for fact in factorials:
                out_file.write(f"{fact}\n")

        print(f"Факториали записані в factorial_numbers.txt.")
    except Exception as e:
        print(f"Помилка: {e}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    file_path = input("Введіть шлях до файлу: ")

    fill_thread = threading.Thread(target=fill_file_with_numbers, args=(file_path,))
    prime_thread = threading.Thread(target=find_prime_numbers, args=(file_path, file_filled))
    factorial_thread = threading.Thread(target=find_factorial_numbers, args=(file_path, file_filled))

    fill_thread.start()
    prime_thread.start()
    factorial_thread.start()

    fill_thread.join()
    prime_thread.join()
    factorial_thread.join()

    print("Операції завершені.")

main()

#task4HW
def find_files_with_word(src_dir, search_word, output_file):
    try:
        files = [file for file in os.listdir(src_dir) if file.endswith(".txt")]

        with open(output_file, "w", encoding="utf-8") as out_file:
            for file in files:
                file_path = f"{src_dir}/{file}"
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if search_word in content:
                        out_file.write(content + "\n")
        print(f"Файли з словом '{search_word}' злиті в {output_file}")
    except Exception as e:
        print(f"Помилка при пошуку: {e}")

def remove_prohibited_words(output_file, banned_words_file):
    try:
        with open(banned_words_file, "r", encoding="utf-8") as banned_file:
            banned_words = set(banned_file.read().splitlines())

        with open(output_file, "r", encoding="utf-8") as in_file:
            content = in_file.read()

        for word in banned_words:
            content = content.replace(word, "")

        with open(output_file, "w", encoding="utf-8") as out_file:
            out_file.write(content)

        print(f"Заборонені слова видалені з {output_file}")
    except Exception as e:
        print(f"Помилка при видаленні заборонених слів: {e}")

def main():
    src_dir = input("Введіть шлях до директорії: ")
    search_word = input("Введіть слово для пошуку: ")
    output_file = "merged_output.txt"
    banned_words_file = input("Введіть шлях до файлу з забороненими словами: ")

    search_thread = threading.Thread(target=find_files_with_word, args=(src_dir, search_word, output_file))
    remove_thread = threading.Thread(target=remove_prohibited_words, args=(output_file, banned_words_file))

    search_thread.start()
    search_thread.join()

    remove_thread.start()
    remove_thread.join()

    print("Статистика: Пошук і обробка файлів завершено.")

main()
