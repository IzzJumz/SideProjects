def largest_product(series: str, length: int) -> int:
    # Validate inputs
    if not series and length == 0:
        return 1  # Edge case per some test cases
    
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    if length < 0:
        raise ValueError("length must not be negative")
    
    if length > len(series):
        raise ValueError("length must be smaller than string length")
    
    if length == 0:
        return 1  # Product of empty series is 1
    
    max_product = 0
    for i in range(len(series) - length + 1):
        substring = series[i:i+length]
        product = 1
        for digit in substring:
            product *= int(digit)
        if product > max_product:
            max_product = product
    
    return max_product

# Bonus: User input
if __name__ == "__main__":
    print("Bank Robber Signal Analyzer")
    print("--------------------------")
    
    while True:
        try:
            series_input = input("Enter the digit sequence (or 'quit' to exit): ").strip()
            if series_input.lower() == 'quit':
                break
                
            length_input = input("Enter the series length: ").strip()
            
            # Validate length is a number
            if not length_input.isdigit():
                print("Error: Length must be a positive integer\n")
                continue
                
            length = int(length_input)
            result = largest_product(series_input, length)
            
            print(f"The largest product for length {length} is: {result}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")