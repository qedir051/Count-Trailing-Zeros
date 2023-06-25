# Count Trailing Zeros

This Python code counts the number of trailing zeros in an input number.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `count_zeros.py` file.
3. Open a terminal or command prompt and navigate to the directory where the `count_zeros.py` file is located.
4. Run the script by executing the following command:

python main.py

5. Enter a number when prompted and press Enter.
6. The program will calculate and display the number of trailing zeros in the input number.

## Example

Enter number: 1204000
Output: 3


## How it Works

The code takes a user input number and counts the number of trailing zeros by repeatedly dividing the number by 10 and checking if the remainder is 0. The count is incremented for each zero encountered until a non-zero digit is reached.

The code has been structured as a function, `count_zeros()`, for reusability. The main part of the code prompts the user for input, calls the `count_zeros()` function, and displays the result.

## Contributing

Contributions to this code are welcome. If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

