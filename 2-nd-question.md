# Question 1
## Jarbay’s Dilemma




```bash
#include <iostream>
#include <vector>

double sum(std::vector<int> a) {
    double res = 0;

    for (auto v : a) {
        res += v;
    }
    return res;
}

double sum(std::vector<double> a) {
    double res = 0;

for (auto v : a) {
    res += v;
}
return res;
}

int main() {
  double res = sum({1, 2, 3, 4, 5});
  std::cout << res << std::endl;
}

```
Jarbay wrote this code, but this code gives compile time error. Jarbay has
enough knowledge to find the error, however he has no time to solve this
error due to ITU’s goddamn homeworks. Can you help Jarbay to solve this
error and explain why it gives error to Jarbay? But while you are helping
him, you are allowed to change only the main function. Jarbay is not allowed
to change the overloaded sum function.

## Solution:

An error occurs during the compilation process due to the presence of two functions with the same name, "sum," but with different
types of parameters - one taking a vector of integers and the other taking a vector of doubles. This is called function overloading and
is not permitted in C++ because the compiler is unable to determine which of the two functions should be used when they are called.
It causes a problem called function overloading ambiguity. To fix this error, Jarbay can either alter the name of one of the
functions or modify the types of the parameters for the two functions. For instance, he could change the parameter type of the first
sum function to a vector of doubles and leave the second sum function unchanged.

The code includes two versions of the sum function, one for int vectors and one for double vectors. The main function creates a
double vector and uses the sum function for double vectors to find the total of the elements in the vector. The final result is
displayed on the console using std::cout .

Here is the modified main function:




```bash
int main() {
    // Create a vector of doubles
    std::vector<double> a = {1, 2, 3, 4, 5};
    // Calculate the sum of the elements in the vector
    double res = sum(a);
    // Print the result to the console
    std::cout << res << std::endl;
}
```





