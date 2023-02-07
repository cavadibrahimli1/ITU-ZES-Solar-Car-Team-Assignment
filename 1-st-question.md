# Question 1
## Hey Çetino

```bash
#include <iostream>
#include <vector>

using namespace std;

double sum1(vector<double> a){
    double res = 0;
    for (auto v : a) {
        res += v;
    }
    return res;
}

double sum2(const vector<double>& a) {
    double res = 0;
    for (auto v : a) {
        res += v;
    }
    return res;
}

int main() {
    vector<double> x;
    for (int i = 0; i < 100000000; i++) {
        x.push_back(i);
    }
    double res1 = sum1(x);
    double res2 = sum2(x);
    return 0;
}
```

Hey, you! Cetino! Can you explain the difference between sum1 and sum2
functions in the code above. (For example, explain efficiencies of sum1 and
sum2 functions, why they are different, etc.)

## Solution:

The code defines two functions, sum1 and sum2, that each take a vector of doubles as an input and compute the sum of all the
elements in the vector. The “sum1” function makes a copy of the input vector, while “sum2” works directly on the original vector
without making a copy. Both functions use a for loop to add up the elements of the vector and return the result. In the main function,
a vector named x is created and filled with 100000000 elements. The sum1 function is called with x as an input and the result is
stored in a variable named “res1”. The sum2 function is also called with x as an input and the result is stored in a variable named
“res2”. The program then finishes by returning 0.



```bash
#include <iostream> // include necessary libraries
#include <vector>

using namespace std; // use the standard namespace

// define function sum1 which takes a vector of doubles as an argument
// and returns the sum of all the elements in the vector
double sum1(vector<double> a){
    double res = 0; // initialize running total to 0
    for (auto v : a) { // loop through each element in the vector
        res += v; // add the element to the running total
    }
    return res; // return the final sum
}

// define function sum2 which takes a vector of doubles as a reference
// and returns the sum of all the elements in the vector
double sum2(const vector<double>& a) {
    double res = 0; // initialize running total to 0
    for (auto v : a) { // loop through each element in the vector
        res += v; // add the element to the running total
    }
    return res; // return the final sum
}

int main() {
    vector<double> x; // create an empty vector
    for (int i = 0; i < 100000000; i++) { // fill the vector with 100000000 elements
        x.push_back(i);
    }
    double res1 = sum1(x); // call sum1 function and store result in res1
    double res2 = sum2(x); // call sum2 function and store result in res2
    return 0;
}
```

DIFFERENCES:
1. The sum1 and sum2 functions have different ways of handling the input vector. The sum1 function makes a copy of the vector,
while the sum2 function uses the original vector without making a copy.

2. The sum2 function is also declared with the "const" keyword, which means it cannot modify the original vector.

2. Both functions have a similar structure, using a loop to sum the elements of the vector and return the result.


