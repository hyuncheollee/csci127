//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program will print a triangle

#include <iostream>
using namespace std;

int main() {
    int dimensions, start;
    char symbol;
    cout << "Enter an int: ";
    cin >> dimensions;
    cout << "Enter a symbol other than space: ";
    cin >> symbol;
    start = dimensions - 1;

    for (int i = 0; i < dimensions; i++) {
        for (int j = 0; j < dimensions; j++) {
            if (j >= start) {
                cout << symbol;
            }
            else {
                cout << " ";
            }
        }
        start--;
        cout << endl;
    }
}