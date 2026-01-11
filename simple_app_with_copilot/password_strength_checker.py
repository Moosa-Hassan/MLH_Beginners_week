import re

"""
Docstring for simple_app_with_copilot.password_strength_checker
This is a command line tool to check stregth of a passowrd input.

Program Steps:
1. Takes input
2. Checks strength
3. Outputs Strength + explainiation

Stregth depends on Combination of upper and lowercase alphabets with special characters and digits.

"""
# Updated strength criteria for password strength checker
def check_password_strength(password):
    """
    Check the strength of a password based on character combinations.
    Returns a tuple of (strength_level, explanation)
    """
    score = -1
    explanation = []
    
    if len(password) >= 8:  # Increased minimum length
        score += 1
    else:
        explanation.append("Password should be at least 8 characters long")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        explanation.append("Add lowercase letters")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        explanation.append("Add uppercase letters")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        explanation.append("Add digits")
    
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};:',.<>?/\\|`~]", password):
        score += 1
    else:
        explanation.append("Add special characters")
    
    if re.search(r"(.)\1{2,}", password):  # Check for repeated characters
        explanation.append("Avoid using repeated characters")
    
    strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    strength = strength_levels[score]
    
    return strength, explanation

def main():
    password = input("Enter a password to check: ")
    strength, explanation = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    if explanation:
        print("Suggestions:")
        for suggestion in explanation:
            print(f"  - {suggestion}")
    else:
        print("Your password is excellent!")

if __name__ == "__main__":
    main()