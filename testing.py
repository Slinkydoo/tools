import random
import time
import mathematics
import sorting


def instance_input(data_type, data_type_2=""):
    max_value = 100
    # Setting the seed to make sure that the same random list is generated every time with the same parameters
    random.seed(124)
    number_of_trials = 5000
    if data_type == "int":
        return [int(random.random() * max_value) for i in range(number_of_trials)]
    elif data_type == "list" and data_type_2 == "int":
        return [[int(random.random() * max_value) for i in range(number_of_trials)] for i in range(number_of_trials)]
    elif data_type == "str" and data_type_2 == "order":
        return [random.choice(["asc", "desc"]) for i in range(number_of_trials)]


def time_test(file_name, function_name):
    number_of_trials = 10  # you can change this number to make the testing faster.
    number_of_trials_per_input = 10

    if file_name == "mathematics" and function_name == "is_prime":

        print("Instancing input...")
        input_list = instance_input("int")
        print("Input instanced.")
        print(function_name, "time trials start:")

        total_time_taken = 0
        for item in input_list:  # run for all the input
            total_time_taken_current_trial = 0
            for trial in range(number_of_trials_per_input):  # now run multiple times for every input
                start_time = time.time()
                mathematics.is_prime(item)
                end_time = time.time()
                time_taken_current_trial = end_time - start_time
                total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
            total_time_taken = total_time_taken + total_time_taken_current_trial
        print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
        return print(function_name, "time trials end.")

    elif file_name == "helpers" and function_name == "my_sum":
        print("Instancing input...")
        input_list = instance_input("list", "int")
        print("Input instanced.")
        print(function_name, "time trials start:")

        total_time_taken = 0
        for item in input_list:  # run for all the input
            total_time_taken_current_trial = 0
            for trial in range(number_of_trials_per_input):  # now run multiple times for every input
                start_time = time.time()
                mathematics.my_sum(item)
                end_time = time.time()
                time_taken_current_trial = end_time - start_time
                total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
            total_time_taken = total_time_taken + total_time_taken_current_trial
        print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
        return print(function_name, "time trials end.")

    elif file_name == "sorting" and function_name == "sort":
        print("Instancing input...")
        input_list = instance_input("list", "int")
        input_list_order = [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
        print("Input instanced.")
        print(function_name, "time trials with random lists start:")

        total_time_taken = 0
        for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
            total_time_taken_current_trial = 0
            for trial in range(number_of_trials_per_input):  # now run multiple times for every input
                start_time = time.time()
                sorting.merge_sort(item_list, item_order)
                end_time = time.time()
                time_taken_current_trial = end_time - start_time
                total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
            total_time_taken = total_time_taken + total_time_taken_current_trial

        print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)

    elif file_name == "sorting" and function_name == "sort_using_min_max":
        print("Instancing input...")
        input_list = instance_input("list", "int")
        input_list_order = [random.choice(["asc", "desc"]) for i in range(number_of_trials)]
        print("Input instanced.")
        print(function_name, "time trials with random lists start:")

        total_time_taken = 0
        for item_list, item_order in zip(input_list, input_list_order):  # run for all the input
            total_time_taken_current_trial = 0
            for trial in range(number_of_trials_per_input):  # now run multiple times for every input
                start_time = time.time()
                sorting.sort_using_min_max(item_list, item_order)
                end_time = time.time()
                time_taken_current_trial = end_time - start_time
                total_time_taken_current_trial = total_time_taken_current_trial + time_taken_current_trial
            total_time_taken = total_time_taken + total_time_taken_current_trial

        print('Average time taken by', str(function_name) + ":", total_time_taken / number_of_trials)
