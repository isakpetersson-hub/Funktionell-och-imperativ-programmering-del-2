# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.
    store_test_case(
        test_cases,
        2,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["08:00-21:00"],
    )  # Testar för en tom dag
    store_test_case(
        test_cases,
        3,
        start_str="09:00",  # Search interval starts
        end_str="14:00",  # Search interval ends
        booking_data=["08:00-12:00"],  # This day's appointments
        exp_result=["12:00-14:00"],
    )  # Testar för starttid mitt i en appointment
    store_test_case(
        test_cases,
        4,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["08:00-21:00"],  # This day's appointments
        exp_result=[],
    )  # Testar för en full bokad dag
    store_test_case(
        test_cases,
        5,
        start_str="12:00",  # Search interval starts
        end_str="18:00",  # Search interval ends
        booking_data=["16:00-19:00"],  # This day's appointments
        exp_result=["12:00-16:00"],
    )  # Testar fö sluttid i mitten av en appointment
    store_test_case(
        test_cases,
        6,
        start_str="08:00",  # Search interval starts
        end_str="08:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=[],
    )  # Testar för start och sluttid samma
    store_test_case(
        test_cases,
        7,
        start_str="09:00",  # Search interval starts
        end_str="08:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=[],
    )  # Testar för starttid efter sluttiden
    print("Test cases generated.")
    return test_cases

if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
