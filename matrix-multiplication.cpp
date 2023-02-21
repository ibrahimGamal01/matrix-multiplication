#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int main()
{
    // int r1;
    // cout << "enter array1 row size " <<endl;
    // cin >> r1;
    // int *rr1 = new int(r1);

    // int c1;
    // cout << "enter array1 col size " << endl;
    // cin >> c1;
    // int *cc1 = new int(c1);

    // int r2;
    // cout << "enter array2 row size " <<endl;
    // cin >> r2;
    // int *rr2 = new int(r2);

    // int c2;
    // cout << "enter array2 col size " <<endl;
    // cin >> c2;
    // int *cc2 = new int(c2);

    // cout << "enter array1 row size ";
    // cin >> r1;
    // cout << "enter array1 col size ";
    // cin >> c1;
    // cout << "enter array2 row size ";
    // cin >> r2;
    // cout << "enter array2 col size ";
    // cin >> c2;

    int r1 = 3;
    int c1 = 3;
    int r2 = 3;
    int c2 = 3;
    int arr1[r1][c1];
    int arr2[r2][c2];
    int ansArr[r1][c2];

    for (int i = 0; i < r1; i++)
    {
        for (int j = 0; j < c1; j++)
        {
            arr1[i][j] = i + j;
        }
        for (int i = 0; i < r2; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                arr2[i][j] = i * j;
            }
        }

        for (int i = 0; i < r1; i++) // iterate over the arr
        {
            for (int j = 0; j < c2; j++)
            {

                for (int k = 0; k < c1; k++)
                {
                    ansArr[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }
        for (int i = 0; i < r1; i++) // iterate over the arr
        {
            for (int j = 0; j < c2; j++)
            {

                cout << ansArr[i][j] << ", ";
            }
        }
    }
    //     // get a specific element from the location
    //     int a = 0;
    //     int b = 0;
    //     cout << "enter ans element location" << endl;
    //     cin >> a >> b;
    //     for (int)
    //

    return 0;
}
