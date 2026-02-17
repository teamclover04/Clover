def sanitize_email(raw_input: str) -> str:
    if not isinstance(raw_input, str):
        return "Invalid Email"
    if len(raw_input) < 1 or len(raw_input) > 254:
        return "Invalid Email"
    cleaned = raw_input.strip().lower()
    if cleaned == "":
        return "Invalid Email"
    if cleaned.count("@") != 1:
        return "Invalid Email"
    return cleaned
x= input("Enter your email Address:")
if len(x)<= 500:
    print(sanitize_email(x))
else:
    print("Charecter limit exceeded")
