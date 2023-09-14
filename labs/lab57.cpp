//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program will find your grade

#include <iostream>
using namespace std;

int main() {
    int credits;
    cout << "Enter number of credit hours taken: ";
    cin >> credits;

    if (credits < 28) {
        cout << "freshman" << endl;
    }
    else if (credits > 27 && credits < 61) {
        cout << "sophomore" << endl;
    }
    else if (credits > 60 && credits < 94) {
        cout << "junior" << endl;
    }
    else if (credits > 93) {
        cout << "senior" << endl;
    }
}