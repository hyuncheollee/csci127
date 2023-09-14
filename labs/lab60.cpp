//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program will print out binary

#include <iostream>
using namespace std;

string converted(string input) {
    string result = "";
    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '1') {
            result += "0";
        }
        else {
            result += "1";
        }
    }
    return result;
}

int main() {
    int number;
    string binary = "";
    bool negative;
    cout << "Enter an int in [-128, 127]: ";
    cin >> number;

    if (number < 0) {
        number *= -1;
        number--;
        negative = true;
    }

    for (int i = 128; i > 0; i /= 2) {
        if (number >= i) {
            number %= i;
            binary += "1";
        }
        else {
            binary += "0";
        }
    }

    if (negative) {
        cout << converted(binary);
    }
    else {
        cout << binary;
    }

    cout << endl;
}