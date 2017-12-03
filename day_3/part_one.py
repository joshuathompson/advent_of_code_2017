import math

number_to_find_distance_to = 312051
number_of_spirals = math.ceil(number_to_find_distance_to / 8) + 1

for i in range(number_of_spirals):

    if i == 0 and number_to_find_distance_to == 0:
        print(0)
    else:
        n = 1 + (i * 2)
        prev_n = 1 + ((i - 1) * 2)
        number_range = [val for val in range((prev_n**2)+1, (n**2)+1)]

        if number_to_find_distance_to in number_range:
            minimum_distance = i

            step_distance = int(len(number_range)/4)
            cross_numbers = [number_range[step+(i-1)] for step in range(0, len(number_range), step_distance)]
            distance_to_cross_numbers = [int(math.fabs(cross_number-number_to_find_distance_to)) for cross_number in cross_numbers]
            minimum_cross_distance = min(distance_to_cross_numbers)

            print(minimum_distance + minimum_cross_distance)

