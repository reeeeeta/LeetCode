class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        swaps = 0

        pos = [0] * n
        for i in range(n):
            pos[row[i]] = i

        for i in range(0,n,2):
            person1 = row[i]
            partner = person1 ^ 1

            if row[i+1] != partner:
                swaps += 1
                curr_partner_idx = pos[partner]
                person_to_move = row[i+1]

                row[i+1], row[curr_partner_idx] = row[curr_partner_idx], row[i+1]
                pos[person_to_move] = curr_partner_idx #更新被換走的人在 pos 陣列中的位置
        return swaps
