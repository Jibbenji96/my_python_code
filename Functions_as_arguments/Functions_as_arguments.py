# def as_sun_lover(temperature):
#     return "Great!" if temperature >= 25 else "Not great!"

# def as_snow_lover(temperature):
#     return "Great!" if temperature <= 0 else "Not great!"

# def report_weather(temperature, weather_function):
#     weather = weather_function(temperature)
#     return weather

# # print(report_weather(-90, as_sun_lover))

# ========== Practice Exercise ============

# passwords = [
#     {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
#     {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
#     {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '21/03/22'}
# ]

# ========== For loop method ============

# def are_all_passwords_long_enough(passwords):
#     for password in passwords:
#         if len(password['password']) < 8:
#             return False
#     return True

# print(are_all_passwords_long_enough(passwords))


# ========== filter() method for lists ============

# def is_shorter_than_8(password):
#     return len(password['password']) < 8

# def are_all_passwords_long_enough(passwords):
#     return len(
#         list(
#             filter(
#                 is_shorter_than_8,
#                 passwords
#             )
#         )
#     ) == 0 

# print(are_all_passwords_long_enough(passwords))

# This returns whether, when applying the function is_shorter_than_8,
# the length of the list of passwords that are shorter than 8.
# If this list is of length 0, then it will return True, meaning all pw are 
# long enough. 


# ============ lambda method for lists ============

# def are_all_passwords_long_enough(passwords):
#     return list(
#         filter(
#             lambda password: len(password['password']) < 8,
#             passwords
#         )
#     ) == []

# print(are_all_passwords_long_enough(passwords))


# ============ List comprehension method ============

# def are_all_passwords_long_enough(passwords):
#     return len(
#         [ 
#             password
#             for password
#             in passwords
#             if len(password['password']) < 8
#         ]
#     ) == 0

# print(are_all_passwords_long_enough(passwords))


# =========== Exercise ===========

# Write a function that checks whether any passwords were added on 21/03/22
# Write a function that returns a list of all passwords added on 22/03/22


# =========== For Loop ===========

# def was_added_on_21(passwords):
#     for password in passwords:
#         if password['added_on'] == "22/03/22":
#             return True
#     return False

# print(was_added_on_21(passwords))


# =========== Filter Method ===========

# def was_added_on_21(password):
#     if password['added_on'] == "22/03/22":
#         return True
#     return False

# def are_any_passwords_from_21(passwords):
#     return len(
#         list(
#             filter(
#                 was_added_on_21, 
#                 passwords)
#         )
#     ) > 0

# print(are_any_passwords_from_21(passwords))


# =========== Lambda method ===========

# def are_any_passwords_from_21(passwords):   
#     return any(password['added_on'] == "21/03/22" for password in passwords)


# print(are_any_passwords_from_21(passwords))

# def return_passwords_from_22(passwords):   
#     matching_list = list(filter(lambda password: password['added_on'] == "22/03/22", passwords))
#     return matching_list

# print(return_passwords_from_22(passwords))


# ========== List Comprehension exampl ============

# new_list = [password["added_on"] == "22/03/22" for password in passwords]
# print(new_list)


# ========== Mapping example ============

# result = map(lambda number: number * 2, [1, 2, 3, 4])
# print(list(result))

# ========== For Loop alternative example ============

# numbers = [1, 2, 3 ,4]
# doubled_list = []

# for number in numbers:
#     doubled_list.append(number * 2)

# print(doubled_list)

# ========== Optimal For Loop List Comprehension example ============

# doubled_list = [num * 2 for num in numbers]
# print(doubled_list)

