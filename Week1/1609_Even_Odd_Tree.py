class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root] if root else []

        def is_odd(x):
            return x % 2 == 1
        def is_even(x):
            return x % 2 == 0
        
        level = 0

        while queue:
            next_queue = []
            prev_value = None
            even_level = True if is_even(level) else False

            for idx, node in enumerate(queue):
                if even_level and not is_odd(node.val):
                    return False
                if not even_level and is_odd(node.val):
                    return False

                if idx == 0:
                    if even_level:
                        prev_value = float('-inf')
                    else:
                        prev_value = float('inf')
                else:
                    if is_even(level) and prev_value >= node.val:
                        return False
                    elif is_odd(level) and prev_value <= node.val:
                        return False
                prev_value = node.val

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue
            level += 1
        return True
