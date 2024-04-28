from subtask_01 import minimal_travel_time


def test_minimal_travel_time():
    # Test case 1: Minimal travel time
    flights1 = ["SOF,IST", "IST,CMB", "CMB,MLE"]
    expected_output1 = 3
    actual_output1 = minimal_travel_time(flights1, "SOF", "MLE")
    print("Test case 1:")
    print("Expected output:", expected_output1)
    print("Actual output:", actual_output1)
    assert actual_output1 == expected_output1

    # Test case 2: Direct flight available
    flights2 = ["SOF,MLE"]
    expected_output2 = 1
    actual_output2 = minimal_travel_time(flights2, "SOF", "MLE")
    print("Test case 2:")
    print("Expected output:", expected_output2)
    print("Actual output:", actual_output2)
    assert actual_output2 == expected_output2

    # Test case 3: Unreachable destination
    flights3 = ["SOF,LON", "LON,PAR"]
    expected_output3 = 0
    actual_output3 = minimal_travel_time(flights3, "SOF", "MLE")
    print("Test case 3:")
    print("Expected output:", expected_output3)
    print("Actual output:", actual_output3)
    assert actual_output3 == expected_output3

    # Test case 4: Multiple paths available
    flights4 = ["SOF,IST", "SOF,PAR", "IST,CMB", "CMB,MLE", "PAR,MLE"]
    expected_output4 = 2
    actual_output4 = minimal_travel_time(flights4, "SOF", "MLE")
    print("Test case 4:")
    print("Expected output:", expected_output4)
    print("Actual output:", actual_output4)
    assert actual_output4 == expected_output4

    # Test case 5: Loopback to origin
    flights5 = ["SOF,SOF", "SOF,MLE"]
    expected_output5 = 1
    actual_output5 = minimal_travel_time(flights5, "SOF", "MLE")
    print("Test case 5:")
    print("Expected output:", expected_output5)
    print("Actual output:", actual_output5)
    assert actual_output5 == expected_output5

    # Test case 6: Empty flight list
    flights6 = []
    expected_output6 = 0
    actual_output6 = minimal_travel_time(flights6, "SOF", "MLE")
    print("Test case 6:")
    print("Expected output:", expected_output6)
    print("Actual output:", actual_output6)
    assert actual_output6 == expected_output6

    # Test case 7: Invalid city code in flights
    flights7 = ["SOF,IST", "IST,CMB", "CMB,123"]
    try:
        minimal_travel_time(flights7, "SOF", "MLE")
    except ValueError as e:
        expected_error_message = "Invalid city code: 123"
        actual_error_message = str(e)
        print("Test case 7:")
        print("Expected error message:", expected_error_message)
        print("Actual error message:", actual_error_message)
        assert actual_error_message == expected_error_message

    print("All test cases passed for Subtask 2.")


test_minimal_travel_time()
