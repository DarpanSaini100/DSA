class Solution {
public:
    static const long long LIM = 1000001;
    vector<int> primes;

    void sieve() {
        vector<bool> isPrime(5001, true);
        for (int i = 2; i <= 5000; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
                for (long long j = 1LL * i * i; j <= 5000; j += i)
                    isPrime[j] = false;
            }
        }
    }

    int factExp(int n, int p) {
        int e = 0;
        while (n) {
            n /= p;
            e += n;
        }
        return e;
    }

    long long multinomial(vector<int>& f) {
        int total = 0;
        for (int x : f) total += x;

        long long ans = 1;

        for (int p : primes) {
            int e = factExp(total, p);
            for (int x : f)
                e -= factExp(x, p);

            while (e--) {
                if (ans > LIM / p) return LIM;
                ans *= p;
            }
        }
        return min(ans, LIM);
    }

    string smallestPalindrome(string s, int k) {
        sieve();

        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;

        vector<int> half(26);
        char mid = 0;

        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2) mid = char('a' + i);
        }

        int m = s.size() / 2;
        string left;

        for (int pos = 0; pos < m; pos++) {
            bool found = false;

            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;

                half[c]--;
                long long ways = multinomial(half);

                if (ways >= k) {
                    left.push_back(char('a' + c));
                    found = true;
                    break;
                }

                k -= ways;
                half[c]++;
            }

            if (!found) return "";
        }

        string right = left;
        reverse(right.begin(), right.end());

        if (mid)
            return left + string(1, mid) + right;
        return left + right;
    }
};