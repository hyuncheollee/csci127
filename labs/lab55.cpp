//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program will convert temperature

#include <iostream>
using namespace std;

int main() {
    double celsius;
    cout << "Lemme get the celsius" << endl;
    cin >> celsius;
    
    double nF = 9.0 / 5.0;
    double farenheit = nF * celsius + 32;
    cout << "It's " << farenheit << " degrees out." << endl;
}