# def display_speed_information(speed):


# if speed <= 50:
#     print('Thank you, your speed is ok! :)')
# else:
#     print('Slow down! :(')
#     if speed > 50:
#         print('slow down! :(')
#     else:
#         print('Thank you, your speed is below limit! :)')
#
# if __name__ == '__main__':
#     display_speed_information(50)
#     display_speed_information(49)
#     display_speed_information(51)

# def check_temp_pressure(temp, pressure):
#     if temp == 0 and pressure == 1013:
#         print(True)
#     else:
#         print(False)


# def calculate_fine_amount(speed):
#     return 500 + (speed - 50) * 10
#
#
# def print_the_value_of_speeding_fine_in_build_up_area(speed):
#     print('Your speed was', speed)
#     if speed > 100:
#         print('You just lost your driving license :(')
#     elif speed > 50:
#         print(f'You just got a fine! Fine amount {calculate_fine_amount(speed)} :(')
#     else:
#         print('Thank you, your speed is fine')


# if __name__ == '__main__':
# check_temp_pressure(0, 1013)
# check_temp_pressure(1, 1013)
# check_temp_pressure(0, 1014)
# check_temp_pressure(1, 1014)

# print_the_value_of_speeding_fine_in_build_up_area(101)
# print_the_value_of_speeding_fine_in_build_up_area(100)
# print_the_value_of_speeding_fine_in_build_up_area(50)
# print_the_value_of_speeding_fine_in_build_up_area(49)
# print_the_value_of_speeding_fine_in_build_up_area(51)


def grades_in_school(grade):
    # if not (isinstance(grade, float) or isinstance(grade, int)):
    #     return 'N/A'

    if grade < 2 or grade > 5:
        return 'N/A'
    elif grade >= 4.5:
        return 'bardzo dobry'
    elif grade >= 4:
        return 'dobry'
    elif grade >= 3:
        return 'dostateczny'
    elif grade >= 2:
        return 'niedostateczny'


print(grades_in_school(grade=5))
print(grades_in_school(grade=4.5))
print(grades_in_school(grade=4))
print(grades_in_school(grade=3))
print(grades_in_school(grade=2))
print(grades_in_school(grade=1))
print(grades_in_school(grade=6))
