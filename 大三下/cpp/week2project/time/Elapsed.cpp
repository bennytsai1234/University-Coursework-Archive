#include <iostream>
#include <sys/time.h>
using std::cout;
int main() {
    struct timeval start_time, end_time;
    double elapsed_seconds, elapsed_microseconds;

    // Get start time
    gettimeofday(&start_time, nullptr);

    // Perform the task (e.g., calculation test of 10 multiplications)
    for (int i = 0; i < 10; ++i) {
        // Your task goes here
        cout<<i<<std::endl;
    }

    // Get end time
    gettimeofday(&end_time, nullptr);

    // Calculate elapsed time
    elapsed_seconds = end_time.tv_sec - start_time.tv_sec;
    elapsed_microseconds = end_time.tv_usec - start_time.tv_usec;
    if (elapsed_microseconds < 0) {
        elapsed_seconds -= 1;
        elapsed_microseconds += 1000000;
    }
    
    // Output elapsed time
    std::cout << "Elapsed time: " << elapsed_seconds << " seconds and " << elapsed_microseconds << " microseconds." << std::endl;

    return 0;
}
