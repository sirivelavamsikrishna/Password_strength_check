# Password Strength Checker

## Overview
The Password Strength Checker is a command-line tool that evaluates the strength of a user-provided password. It categorizes passwords into weak, moderate, or strong based on their length and character composition. Additionally, it provides suggestions to enhance password security and offers the option to generate a strong password.

## Features
- Checks if a password is commonly used and suggests avoiding it.
- Categorizes passwords as **Weak**, **Moderate**, or **Strong** based on:
  - Length
  - Inclusion of numbers, letters, and special characters
- Provides suggestions for improving password strength.
- Offers an option to generate a strong password based on user-defined length.

## Installation
1. Clone the repository or download the script.
   ```sh
   git clone <repository-url>
   cd password_strength_checker
   ```
2. Ensure you have Python installed (Python 3.x recommended).
3. No external libraries are required as it uses built-in Python modules.

## Usage
Run the script using Python:
```sh
python password_strength_checker.py
```

### Example Interaction
```
Enter your password: password123
Strength: Weak
Suggestion: Try adding more special characters to make it stronger!

Do you want a strong password suggestion? (Yes/No): Yes
Strong Password: A3$xPz&9Qm
```

## Error Handling
- Ensures passwords are not empty.
- Checks against commonly used passwords.
- Provides user-friendly error messages and suggestions.

## Future Improvements
- Implement a graphical user interface (GUI) version.
- Store and manage generated passwords securely.
- Add an API version for web applications.

## License
This project is open-source and available under the MIT License.

## Contributors
Developed by Vamsi Krishna Sirivela. Contributions are welcome!


