// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
// which means that 28 is a perfect number.

// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

//     As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#include <cmath>
#include <iostream>
#include <vector>
#include <utility>

std::vector<int> primes_up_to(int n) {
    std::vector<int> result;
    result.push_back(2);
    result.push_back(3);
    for (auto possible_prime = 5; possible_prime < n; possible_prime += 2) {
	bool is_prime = true;
	for (auto prime = result.begin(); prime != result.end(); ++prime) {
	    if (possible_prime % *prime == 0) {
		// not a prime
		is_prime = false;
		break;
	    }
	}
	if (is_prime) {
	    result.push_back(possible_prime);
	}
    }
    return result;
}

std::vector<std::pair<int, int> > prime_factorization_of(int n, std::vector<int>& primes) {
    std::vector<std::pair<int, int> > result;
    for (auto prime : primes) {
	if (n == 1) {
	    break;
	}
	auto cur_count = 0;
	while (n % prime == 0) {
	    cur_count += 1;
	    n /= prime;
	}
	if (cur_count > 0) {
	    auto prime_factor = std::make_pair(prime, cur_count);
	    result.push_back(prime_factor);
	}
    }
    return result;
}

std::vector<int> proper_factors_of(int n, std::vector<int>& primes) {
    //int sqrt_n = (int)sqrt(n);
    //auto primes = primes_up_to(sqrt_n);
    std::vector<int> result{1};
    for (auto prime = primes.begin(); prime != primes.end(); ++prime) {
	if (n <= *prime) {
	    break;
	}
	if (n % *prime == 0) {

	    result.push_back(*prime);
	    int reciprocal = n / *prime;
	    if (reciprocal != *prime)
	    result.push_back(n / *prime);
	}
    }
    return result;
}

// std::vector<int> abundant_nums_up_to(int n) {
//     int sqrt_n = (int)sqrt(n);
//     auto primes = primes_up_to(sqrt_n);
//     std::vector<int> result;
//     for (int possible_abundant = 2; possible_abundant < n; ++possible_abundant) {
// 	auto factors = prime_factors_of(possible_abundant, primes);
// 	int sum = 0;
// 	for (auto factor : factors) {
// 	    sum += factor;
// 	}
// 	std::cout << "POS ABUND: " << possible_abundant << std::endl;
// 	std::cout << "SUM: " << sum << std::endl;
// 	if (sum > possible_abundant) {
// 	    result.push_back(possible_abundant);
// 	}
//     }
//     return result;
// }

int main() {
    auto primes = primes_up_to(100);
    auto factorization = prime_factorization_of(50, primes);
    for (auto factor : factorization) {
	std::cout << "Prime: " << std::get<0>(factor) << std::endl;
	std::cout << "Power:: " << std::get<1>(factor) << std::endl;
	std::cout << std::endl;
    }
}
