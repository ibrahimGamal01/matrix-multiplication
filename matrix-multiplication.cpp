#include <iostream>
#include <string>
#include <string.h>
#include <cstdlib>

using namespace std;

int main()
{
    int r1, c1, r2, c2;

    cout << "Enter matrix 1 dimensions (rows columns): ";
    cin >> r1 >> c1;
    int **arr1 = new int *[r1];
    for (int i = 0; i < r1; i++)
    {
        arr1[i] = new int[c1];
    }

    cout << "Enter matrix 2 dimensions (rows columns): ";
    cin >> r2 >> c2;
    int **arr2 = new int *[r2];
    for (int i = 0; i < r2; i++)
    {
        arr2[i] = new int[c2];
    }
    if (c2 == r1) // c1 should = r2 to prefrom matrix multiplication
    {
        // intialize the array
        int **ansArr = new int *[r1];
        for (int i = 0; i < r1; i++)
        {
            ansArr[i] = new int[c2];
        }

        /////////////insert random values in matrix 1,2
        // insert in mat1
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c1; j++)
            {
                arr1[i][j] = i + j + (rand() % 10);
            }
        }

        // insert in mat2
        for (int i = 0; i < r2; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                arr2[i][j] = i - j + (rand() % 10);
            }
        }

        // multiply * values of matrix 1, 2
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++)
            {

                for (int k = 0; k < c1; k++)
                {
                    ansArr[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }

        /////////// print matrices
        // print matrix 1
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c1; j++)
            {
                cout << arr1[i][j] << " ";
            }
            cout << endl;
        }

        cout << endl
             << "||*************************||" << endl;

        // print matrix 2
        for (int i = 0; i < r2; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                cout << arr2[i][j] << " ";
            }
            cout << endl;
        }

        cout << endl
             << "||=========================||" << endl
             << endl;

        // print answer
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++)
            {
                cout << ansArr[i][j] << " ";
            }
            cout << endl;
        }
    }
    else
    {
        // c1 should = r2
        cout << endl
             << "First matrix must have the same number of columns as the second matrix has rows" << endl;
    }
////////////////////////////////////////////////

    // find a specific element of the multiplication directly
    // ask user for row and column indices
    int row, col;
    cout << "Enter row and column indices (zero-based) of element to find: ";
    cin >> row >> col;

    if (row >= r1 || col >= c2 || row < 0 || col < 0) // dimentions of ansArr
    {
        cout << "Error: invalid row or column index\n";
        return 1;
    }

    // find element value
    int element = 0;
    for (int k = 0; k < c1; k++)
    {
        element += arr1[row][k] * arr2[k][col];
    }

    cout << "Element (" << row << "," << col << ") = " << element << endl;

    return 0;
}
