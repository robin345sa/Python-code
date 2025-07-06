import re

def check_password_strength(password):
    strength_score = 0
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special_char': bool(re.search(r'[@$!%*?&#]', password))
    }
    
    strength_score = sum(criteria.values())
    
    if strength_score == 5:
        return "Very Strong"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
