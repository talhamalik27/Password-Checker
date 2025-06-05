import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include uppercase letters.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include special characters.")

    # Final strength status
    if strength == 5:
        return "Strong ✅", feedback
    elif strength >= 3:
        return "Medium ⚠️", feedback
    else:
        return "Weak ❌", feedback

# Main Program
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result, suggestions = check_password_strength(user_password)

    print(f"Password Strength: {result}")
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")
