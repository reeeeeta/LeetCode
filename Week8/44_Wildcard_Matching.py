class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        s_tmp_idx = -1

        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1
            elif star_idx != -1:
                p_ptr = star_idx + 1 # 回到 * 的下一個位置
                s_tmp_idx += 1 # 讓 * 多吃掉一個 s 的字元
                s_ptr = s_tmp_idx
            else:
                return False
        return all(x == '*' for x in p[p_ptr:])
