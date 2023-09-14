//Name: Hyuncheol Lee
//Email: hyuncheol.lee47@myhunter.cuny.edu
//Date: November 21, 2022
//This program print out your budget // expense sheet

#include <iostream>
using namespace std;

int main() {
    double budget, expense;
    bool lowBudget;
    cout << "Input your annual budget: ";
    cin >> budget;
    cout << "Input your month expense: ";
    cin >> expense;

    for(int i = 1; i < 13; i++) {
        if (i == 7) {
            expense *= 1.15;
        }
        budget -= expense;
        printf("%5d\t%7.2f\t%27.2f\n", i, expense, budget);
    }   
    
    if (budget < 0) {
        lowBudget = true;
    }

    if (lowBudget) {
        cout << "need higher budget" << endl;
    }
}