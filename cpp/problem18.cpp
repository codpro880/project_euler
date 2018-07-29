#include <algorithm>
#include <iostream>
#include <vector>

int sum_triangle() {
    std::vector<std::vector<int> > triangle {
	{75},
	    {95, 64},
		{17, 47, 82},
{18, 35, 87, 10},
{20, 4, 82, 47, 65},
{19, 1, 23, 75, 3, 34},
{88, 2, 77, 73, 7, 63, 67},
{99, 65, 4, 28, 6, 16, 70, 92},
{41, 41, 26, 56, 83, 40, 80, 70, 33},
{41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
{53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
{70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
{91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
{63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
{04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23} };
    //std::vector<std::vector<int> > triangle { {75}, {95, 64}, {17, 47, 82} };

    // Take bottom row, take max, sum upward.
    std::vector<int> cur_row_maxes;
    for (auto i = triangle.size() - 1; i >= 1; --i) {
	for (auto cur = triangle[i].begin(); cur != triangle[i].end()-1; cur++) {
	    cur_row_maxes.push_back(std::max(*cur, *(cur + 1)));
	}
	for (auto j = 0; j < cur_row_maxes.size(); ++j) {
	    triangle[i-1][j] += cur_row_maxes[j];
	}
	cur_row_maxes.clear();
    }
    return triangle[0][0];
}

int main() {
    std::cout << "Largest sum: " << sum_triangle() << std::endl;
}
