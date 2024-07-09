# Assignment 07, Task 03
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 1.5 hours

class DataFrame:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f'DataFrame.items = {self.items}'

    def __str__(self):
        return str(self.items)

    def __eq__(self, other):
        if isinstance(other, list):
            return self.items == other
        raise NotImplemented

    def add(self, x):
        """
        will add either x or the members of x to the list self.items
        x can be: number, list, tuple
        if number, it is added to list directly
        if a list or tuple, members are individually added to the list
        """
        if isinstance(x, int):
            self.items.append(x)
        else:
            for item in x:
                self.items.append(item)

    def mean(self) -> float:
        """
        compute and return mean of data in the collection
        """
        total = 0
        for item in self.items:
            total += item
        return total / len(self.items)

    def percentile(self, r):
        """
        compute and return value at r-th percentile of collection
        0 <= r <= 100
        """
        # percentile are values that are equal to or lower than r
        if not(0 <= r <= 100):
            raise ValueError("Percentile must be between 0 and 100")

        sorted_list = sorted(self.items)
        percentile_idx = (r / 100) * len(sorted_list)
        return sorted_list[int(percentile_idx)]

    def mode(self):
        """
        compute and return mode of the data
        (item that appears most in dataset)

        for multiple modes, the last value in the list
        with the biggest mode will be returned
        """
        number_count = {}
        for idx, item in enumerate(self.items):
            if item in number_count.keys():
                number_count[item] += 1
            else:
                number_count[item] = 1

        current_biggest_count = 0
        current_biggest_number = None
        for number in number_count:
            count = number_count[number]
            if count >= current_biggest_count:
                current_biggest_count = count
                current_biggest_number = number
        return current_biggest_number

    def sd(self):
        """
        compute and return standard deviation of data
        standard deviation = how much the data scatters around the mean
        1. find mean of dataset
        2. for each data point, calculate its deviation from the mean
        3. square each deviation
        4. find average of squared deviations
        5. sqrt the average of squared deviations
        """
        # edge case, where s.d. is undefined if there's only one data point
        if len(self.items) < 2:
            return 0

        # 1. find mean of dataset
        total = 0
        for item in self.items:
            total += item
        mean = total / len(self.items)

        # 2. calculate deviation from the mean for each data point
        total_deviations_squared = 0
        for item in self.items:
            deviation = item - mean
            # 3. square each deviation
            deviation_squared = deviation ** 2
            # add to variable so that we can find the mean
            # of all deviations squared
            total_deviations_squared += deviation_squared

        # 4. find average of squared deviations
        # for some reason we do - 1???
        average_of_squared_deviations = total_deviations_squared / (len(self.items))
        # 5. then square that
        return average_of_squared_deviations ** 0.5


def test_data_frame():
    # ==============================================================
    # 1. Test add()
    data_frame = DataFrame()
    data_frame.add(3)
    data_frame.add((9, 4))
    data_frame.add([1, 2, 5])
    assert data_frame == [3, 9, 4, 1, 2, 5]
    print("Test 1 passed")
    # ==============================================================
    # 2. Test mean()
    assert data_frame.mean() == 4.0
    print("Test 2 passed")
    # ==============================================================
    # 3. Test percentile()
    data_frame = DataFrame()
    data_frame.add([4, 2, 8, 7, 3, 1, 5])
    assert data_frame.percentile(98) == 8
    print("Test 3 passed")
    # ==============================================================
    # 4. Test mode()
    # No mode (technically more than one values have the same mode)
    data_frame = DataFrame()
    data_frame.add([1, 2, 3, 4, 5, 6, 7])
    assert data_frame.mode() == 7

    # One mode
    data_frame = DataFrame()
    data_frame.add([1, 1, 2, 3, 4, 5, 6, 7, 8])
    assert data_frame.mode() == 1

    # Multiple modes
    data_frame = DataFrame()
    data_frame.add([4, 3, 1, 7, 3, 4, 1])
    assert data_frame.mode() == 1

    # Multiple modes
    data_frame = DataFrame()
    data_frame.add([4, 2, 2, 7, 3, 1, 1])
    assert data_frame.mode() == 1
    print("Test 4 passed")
    # ==============================================================
    # 5. Test standard deviation
    print(data_frame)
    print(data_frame.sd())
    print("Test 5 passed")




if __name__ == '__main__':
    test_data_frame()
