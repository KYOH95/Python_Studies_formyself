#include <sys/types.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int y = 20;
    cout << "I am still only one process." << endl;
    pid_t returnedValue = fork();
    if(returnedValue < 0){
        // still only one process
        perror("error forking"); // report the error
        return -1;
    }
    else if (returnedValue > 0) {
    // this must be the parent process
        //cout << "I am the parent process; my child’s ID is " << returnedValue << "." << endl;
        cout << "I am the parent process. y is " << x << endl;
        sleep(1);
    } 
    else if (returnedValue == 0){ 
    // this must be the child process
        pid_t returnedValueChild = fork(); //forking child process to break parent and child
        if(returnedValueChild < 0){
            perror("error forking");
            return -1;
        }
        else if(returnedValueChild > 0){
            //parent of child process
            cout << "I am the parent of child process. y is " << y << endl;
            sleep(1); // wait a second before repeating
        }
        else{
            //child of child process
            cout << "I am the child of child process. y^2 is " << y*y << endl;
            sleep(1);
        }
    } 
    return 0;
}