#include "LinearSearch.h"

using namespace std;

template <typename T>
LinearSearch<T>::LinearSearch()
{
}

template <typename T>
LinearSearch<T>::~LinearSearch()
{
}

template <typename T>
bool LinearSearch<T>::Search(T* arr, int arrSize, T& findElement, int& findIndex)
{
    findIndex = -1;

    for (int idx = 0; idx < arrSize; ++idx)
    {
        if (arr[idx] == findElement)
        {
            findIndex = idx;
            return true;
        }
    }

    return false;
}