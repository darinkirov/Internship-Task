from subtask_03 import minimal_travel_time_with_capacity


def test_minimal_travel_time_with_capacity():
    # Test case 1: Minimal travel time with capacity
    expected_output1 = 2
    actual_output1 = minimal_travel_time_with_capacity(["SOF,MLE,2", "SOF,LON,3", "LON,MLE,4"], "SOF", "MLE", 3)
    print("Test case 1:")
    print("Expected output:", expected_output1)
    print("Actual output:", actual_output1)
    assert actual_output1 == expected_output1

    # Test case 2: Destination unreachable due to capacity limit
    expected_output2 = 0
    actual_output2 = minimal_travel_time_with_capacity(["SOF,MLE,2", "SOF,LON,3", "LON,MLE,4"], "SOF", "MLE", 5)
    print("Test case 2:")
    print("Expected output:", expected_output2)
    print("Actual output:", actual_output2)
    assert actual_output2 == expected_output2

    # Test case 3: Single flight with exact capacity
    expected_output3 = 1
    actual_output3 = minimal_travel_time_with_capacity(["SOF,MLE,3"], "SOF", "MLE", 3)
    print("Test case 3:")
    print("Expected output:", expected_output3)
    print("Actual output:", actual_output3)
    assert actual_output3 == expected_output3

    # Test case 4: Single flight with insufficient capacity
    expected_output4 = 0
    actual_output4 = minimal_travel_time_with_capacity(["SOF,MLE,2"], "SOF", "MLE", 3)
    print("Test case 4:")
    print("Expected output:", expected_output4)
    print("Actual output:", actual_output4)
    assert actual_output4 == expected_output4

    # Test case 5: No available flights
    expected_output5 = 0
    actual_output5 = minimal_travel_time_with_capacity([], "SOF", "MLE", 3)
    print("Test case 5:")
    print("Expected output:", expected_output5)
    print("Actual output:", actual_output5)
    assert actual_output5 == expected_output5

    # Test case 6: Origin same as destination
    expected_output6 = 0
    actual_output6 = minimal_travel_time_with_capacity(["SOF,MLE,2", "SOF,LON,3", "LON,MLE,4"], "SOF", "SOF", 3)
    print("Test case 6:")
    print("Expected output:", expected_output6)
    print("Actual output:", actual_output6)
    assert actual_output6 == expected_output6

    # Test case 7: Multiple possible flights
    expected_output7 = 1
    actual_output7 = minimal_travel_time_with_capacity(["SOF,LON,3", "LON,MLE,3", "SOF,MLE,4"], "SOF", "MLE", 3)
    print("Test case 7:")
    print("Expected output:", expected_output7)
    print("Actual output:", actual_output7)
    assert actual_output7 == expected_output7

    # Test case 8: Group size exceeding maximum capacity
    flights8 = ["SOF,MLE,2", "SOF,LON,3"]
    origin8 = "SOF"
    destination8 = "MLE"
    group_size8 = 4
    expected_output8 = 0  # No flight with capacity for all members
    actual_output8 = minimal_travel_time_with_capacity(flights8, origin8, destination8, group_size8)
    print("Test case 8:")
    print("Expected output:", expected_output8)
    print("Actual output:", actual_output8)
    assert actual_output8 == expected_output8

    # Test case 9: Capacity constraint on intermediate flights
    flights9 = ["SOF,PAR,2", "PAR,MLE,4"]
    origin9 = "SOF"
    destination9 = "MLE"
    group_size9 = 3
    expected_output9 = 0  # Route: SOF -> PAR -> MLE (capacity 4)
    actual_output9 = minimal_travel_time_with_capacity(flights9, origin9, destination9, group_size9)
    print("Test case 9:")
    print("Expected output:", expected_output9)
    print("Actual output:", actual_output9)
    assert actual_output9 == expected_output9

    # Test case 10: Circular routes
    flights10 = ["SOF,PAR,3", "PAR,SOF,3"]
    origin10 = "SOF"
    destination10 = "SOF"
    group_size10 = 3
    expected_output10 = 0  # Route: SOF -> PAR -> SOF
    actual_output10 = minimal_travel_time_with_capacity(flights10, origin10, destination10, group_size10)
    print("Test case 10:")
    print("Expected output:", expected_output10)
    print("Actual output:", actual_output10)
    assert actual_output10 == expected_output10

    # Test case 11: Invalid flight capacities
    flights11 = ["SOF,MLE,-2", "SOF,LON,3", "LON,MLE,4"]
    origin11 = "SOF"
    destination11 = "MLE"
    group_size11 = 3
    try:
        minimal_travel_time_with_capacity(flights11, origin11, destination11, group_size11)
    except ValueError as e:
        expected_error_message = "Invalid capacity: -2"
        actual_error_message = str(e)
        print("Test case 11:")
        print("Expected error message:", expected_error_message)
        print("Actual error message:", actual_error_message)
        assert expected_error_message == actual_error_message

    print("All test cases passed for Subtask 3.")


if __name__ == "__main__":
    test_minimal_travel_time_with_capacity()