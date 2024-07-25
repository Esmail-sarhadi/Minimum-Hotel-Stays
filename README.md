# Minimum Hotel Stays

This project provides a solution to find the minimum number of hotel stays required to travel from the first city to the last city, given a maximum driving time limit per day. The solution uses Dijkstra's algorithm with a priority queue to efficiently compute the shortest paths considering hotel stays.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Algorithm Explanation](#algorithm-explanation)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python 3.x installed. The project does not require any additional libraries beyond Python's standard library.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/minimum-hotel-stays.git
    ```
2. Navigate to the project directory:
    ```bash
    cd minimum-hotel-stays
    ```
3. Run the script:
    ```bash
    python minimum_hotel_stays.py
    ```

The script will prompt you to choose between user input or running predefined test cases.

### User Input

If you choose to enter user input, you will be prompted to provide:
- The number of cities.
- The list of hotel city indices (separated by spaces).
- The number of roads.
- The details of each road (starting city, ending city, travel time).

### Example

```plaintext
Choose (1) User Input or (2) Run Test Cases: 1
Enter the number of cities: 6
Enter the list of hotel city indices (separated by spaces): 2 5 3
Enter the number of roads: 8
Enter road details (starting city, ending city, travel time): 1 2 400
Enter road details (starting city, ending city, travel time): 3 2 80
Enter road details (starting city, ending city, travel time): 3 4 301
Enter road details (starting city, ending city, travel time): 4 5 290
Enter road details (starting city, ending city, travel time): 5 6 139
Enter road details (starting city, ending city, travel time): 1 3 375
Enter road details (starting city, ending city, travel time): 2 5 462
Enter road details (starting city, ending city, travel time): 4 6 300
Minimum hotel stays: 2
```

### Running Test Cases

If you choose to run the predefined test cases, the script will automatically execute the test cases and display the results.

## Project Structure

- `minimum_hotel_stays.py`: Main script containing the code for calculating the minimum hotel stays.
- `README.md`: Project documentation.

## Algorithm Explanation

The algorithm uses Dijkstra's algorithm with a priority queue to efficiently find the shortest paths. The key aspects include:
- Considering hotel stays to reset the travel time counter.
- Updating the number of hotel stays when reaching a city that has a hotel.
- Ensuring the total travel time does not exceed the maximum allowed driving time (600 minutes).

## Test Cases

The script includes several test cases to validate the correctness of the solution. Here are some example test cases:

```plaintext
Test Case: n = 6, hotels = [2, 5, 3], roads = [(1, 2, 400), (3, 2, 80), (3, 4, 301), (4, 5, 290), (5, 6, 139), (1, 3, 375), (2, 5, 462), (4, 6, 300)]
Minimum hotel stays: 2

Test Case: n = 5, hotels = [3, 2], roads = [(1, 2, 400), (1, 3, 350), (2, 3, 200), (2, 4, 300), (3, 4, 500), (4, 5, 200)]
Minimum hotel stays: 2
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Description

This project aims to solve the problem of finding the minimum number of hotel stays required to travel between cities, considering a daily driving time limit. It uses an efficient graph traversal algorithm and includes both user input functionality and predefined test cases for validation.


<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
    </a>
