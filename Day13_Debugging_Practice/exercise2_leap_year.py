# Exercise 2: Leap Year Check

# --- Buggy Version ---
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# --- Fixed Version ---
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:   # ✅ Corrected to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# --- Test Cases ---
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True
