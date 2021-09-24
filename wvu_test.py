from wvu import add, subtract, multi, div, root, exp

assert add(4,0b11) == 7, "Binary conversion did not work"
print("Binary conversion test completed successfully, no errors.")

assert add(4,0o3) == 7, "Octal converion did not work"
print("Addition test completed successfully, no errors.")

assert add(4,0x3) == 7, "Hex conversation did not work"
print("Hex conversation test completed successfully, no errors.")

assert add(4,3) == 7, "Addition did not work"
print("Addition test completed successfully, no errors.")

assert subtract(4,3) == 1, "Subtraction did not work"
print("Subtraction test completed successfully, no errors.")

assert multi(4,3) == 12, "Multiplication did not work"
print("Multiplication test completed successfully, no errors.")

assert div(6,3) == 2, "Division did not work"
print("Division test completed successfully, no errors.")

assert root(9,9) == (3, 3), "Square root did not work"
print("Square root test completed successfully, no errors.")

assert exp(4,3) == 64, "Expononent did not work"
print("Expononent test completed successfully, no errors.")
