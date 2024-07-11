import pytest


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        return self.averageWaitingTime_simple(customers)

    @staticmethod
    def averageWaitingTime_simple(customers: list[list[int]]) -> float:
        cur_time, wait_time = 0, 0
        for arrival, prep_time in customers:
            if arrival > cur_time:
                cur_time = arrival
            cur_time += prep_time
            wait_time += cur_time - arrival
        return wait_time / len(customers)

    @staticmethod
    def averageWaitingTime_mine(customers: list[list[int]]) -> float:
        n: int = len(customers)
        time_waiting: int = customers[0][1]
        finished_prev = customers[0][0] + customers[0][1]

        for customer_ind in range(1, n, 1):
            times: list[int] = customers[customer_ind]
            arrive: int = times[0]

            # chef starts cook this as soon as he finished last dish or customer arrived
            start_cook: int = max(arrive, finished_prev)
            end_time: int = start_cook + times[1]
            finished_prev: int = end_time
            time_waiting += end_time - arrive

        return time_waiting / n


@pytest.mark.parametrize(
    "customers, expected",
    [
        ([[1, 2], [2, 5], [4, 3]], 5.00000),
        ([[5, 2], [5, 4], [10, 3], [20, 1]], 3.25000),
    ],
)
def test_averageWaitingTime(customers, expected):
    assert Solution().averageWaitingTime(customers) == expected
