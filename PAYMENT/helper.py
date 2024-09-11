
def format_amount(s):
    s = str(s)  # Explicitly convert to string
    if len(s) <= 3:
        return s + ".00"
    else:
        # Reverse the string
        reversed_s = s[::-1]
        # Insert commas every 3 characters
        formatted_reversed_s = ','.join(reversed_s[i:i+3] for i in range(0, len(reversed_s), 3))
        # Reverse it back to the original order
        formatted_s = formatted_reversed_s[::-1]
        return formatted_s
