//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program will find even numbers

#include <iostream>
using namespace std;

int main() {
    int start, end;
    cout << "Enter start: ";
    cin >> start;
    cout << "Enter end: ";
    cin >> end;

    for (int i = start; i <= end; i++) {
        if (i % 2 == 0) {
            cout << i << endl;
        }
    }
}