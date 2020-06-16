
template <typename T>
class LinearSearch
{
    public:
        LinearSearch();
        ~LinearSearch();

        bool Search(T* arr, int arrSize, T& findElement, int& index);
};