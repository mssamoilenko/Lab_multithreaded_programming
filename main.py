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