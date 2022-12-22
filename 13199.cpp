#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	int t, p, m, f, c;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> p >> m >> f >> c;
        int s = 0;
        int d = 0;
        d = (m/p) + ((m/p)*c)/f;
        s = m/p;
        int rest = (m/p)*c;
        if (rest >= f) {
            s += ((rest-f)/(f-c))+1;
        }
        cout << s-d << "\n";
    }
}

// 최종적으로 얻은 쿠폰으로 치킨을 다시 구매할때, 치킨을 구매한 만큼 쿠폰이 새로 나온다. 가지고 있는 쿠폰을 total 이라 하면, 치킨 1개를 쿠폰으로 구매 -> total -= f, total += c 가 된다. 
// 이과정을 단순히 생각하면, f만큼 빼고 c만큼 더해지므로, 결국 total에서 (f-c)만큼을 빼주면 된다. 
// 즉, 치킨을 하나 구매할때마다. f-c만큼의 쿠폰이 없어진다. 따라서, 추가로 구매할 수 있는 치킨의 수는 (total-f) / (f-c) 라 할 수 있다. 여기서 주의해야 할점이 있다. 
// 만약, total = 6, f = 3, c = 2이라 하면, (total-f) / (f-c) = 3 / 1 = 3로 3마리를 먹을 수 있다는 결과가 나온다.
// 하지만, 차례대로 계산을 해보면 총 4마리를 먹을 수 있다.
// 따라서, total에서 쿠폰으로 이미 한마리를 먹은 것으로 하고, 남은 쿠폰의 감소량이 (f-c)라 생각하면 다음과 같이 식을 표현할 수 있다. 
// (total - f) / (f - c) + 1 여기서, +1은 이미 한마리를 먹은 것으로 생각하기 때문에 +1을 해준다.

