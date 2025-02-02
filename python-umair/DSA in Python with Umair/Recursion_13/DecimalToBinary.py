'''
### Method 1: Division by 2 Method
To convert a decimal number to its binary representation, you can use the division by 2 method. Here are the steps:

1. **Divide** the decimal number by 2.
2. **Write down** the remainder (binary digit).
3. **Repeat** with the quotient from the previous step until the quotient is zero.
4. **Read the remainders** from bottom to top to get the binary representation.

### Example:
Let's convert the decimal number **15** to binary using this method.

1. **First Division:**
   - 15 ÷ 2 = 7, remainder **1**

2. **Second Division:**
   - 7 ÷ 2 = 3, remainder **1**

3. **Third Division:**
   - 3 ÷ 2 = 1, remainder **1**

4. **Fourth Division:**
   - 1 ÷ 2 = 0, remainder **1**

Now, read the remainders from bottom to top:
**1111**

So, **15** in decimal is **1111** in binary.

### Step-by-Step Explanation
1. **Start with the decimal number:** Let's say we want to convert 15.
2. **Divide by 2 and note the remainder:**
   - 15 ÷ 2 = 7, remainder **1**
3. **Take the quotient and repeat:**
   - 7 ÷ 2 = 3, remainder **1**
4. **Continue until the quotient is zero:**
   - 3 ÷ 2 = 1, remainder **1**
   - 1 ÷ 2 = 0, remainder **1**
5. **Read the remainders from last to first:** The binary number is **1111**.

### Summary
The division by 2 method involves repeatedly dividing the decimal number by 2 and noting the remainders until the quotient becomes zero. The binary representation
is obtained by reading the remainders from bottom to top.
''' 

def DecToBin(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*DecToBin(int(n/2))

print(DecToBin(13))
