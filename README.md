

# Transport Company Routing Problem

This project implements a solution for a transport company that needs to deliver goods between cities while adhering to specific travel constraints. The driver can only drive for a maximum of 10 hours per day, and the delivery route must include stays at designated hotels.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to find the minimum number of hotel stays required for a driver to travel from a starting city to a destination city. The driver must stay overnight at hotels and can only drive for a maximum of 10 hours (600 minutes) between hotels or to the destination.

## Installation

To run this project, you need Python 3.x installed on your system. You can check your Python version by running:

```bash
python --version
```

### Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/esmail-sarhadi/Minimum-Hotel-Stays.git
cd transport-routing
```

### Run the Code

You can run the code directly in a Python environment. Make sure you have `heapq` module (it is part of the standard library).

## Usage

The program can be run in two modes: 

1. **User Input Mode**: Allows you to enter cities, hotels, and roads manually.
2. **Test Case Mode**: Runs predefined test cases to validate the implementation.

### User Input

To use the user input mode, simply run the script and choose option `1`:

```bash
python transport_routing.py
```

You will be prompted to enter the following:

- The number of cities.
- A list of hotel city indices (separated by spaces).
- The number of roads.
- Details for each road (starting city, ending city, travel time).

### Example Input

```
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
```

### Test Case Mode

To run predefined test cases, choose option `2`:

```bash
Choose (1) User Input or (2) Run Test Cases: 2
```

The results will display the minimum hotel stays required for each test case.

## Algorithm Explanation

The solution uses Dijkstra's algorithm to find the shortest path while considering the constraints of hotel stays and driving time.

1. **Graph Representation**: Cities and roads are represented using an adjacency list.
2. **Priority Queue**: A min-heap (priority queue) is employed to always explore the city with the least accumulated travel time.
3. **Hotel Handling**: When a city with a hotel is reached, the driver is allowed to reset the travel time and increment the hotel stay count.
4. **Output**: The function returns the minimum number of hotel stays needed to reach the destination city or `-1` if no valid path exists.

## Test Cases

Several test cases are included to validate the implementation. These test cases can be found within the code. Each test case consists of:

- A set number of cities.
- A list of cities with hotels.
- A set of roads connecting the cities with travel times.

### Sample Test Cases

```python
(6, [2, 5, 3], [(1, 2, 400), (3, 2, 80), (3, 4, 301), (4, 5, 290), (5, 6, 139), (1, 3, 375), (2, 5, 462), (4, 6, 300)])
(5, [3, 2], [(1, 2, 400), (1, 3, 350), (2, 3, 200), (2, 4, 300), (3, 4, 500), (4, 5, 200)])
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



Feel free to modify the README file according to your project structure or specific requirements. This template provides a comprehensive overview and will help users understand how to interact with the program effectively.

<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
    </a>
