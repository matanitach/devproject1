from typing import List, Optional

"""
     ממיין את המערך, מוחק כפילויות וממלא מקומות ריקים ב-"_"
     מחזיר את אורך המערך החדש ללא כפילויות
     שומר על האורך המקורי של המערך
     """


#
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:  # מקבלת טיפוס מסוג ליסט מחזירה אינטיגר
#
#         if not nums:  # אם המערך רק
#             return 0
#
#         original_length = len(nums)  # שומרים את האורך המקורי
#
#         # ממיינים את המערך במקום
#         nums.sort()
#
#         # משתמשים בשני מצביעים
#         # slow מצביע למקום שבו נכניס את הערך הבא הייחודי
#         # fast עובר על כל המערך
#         slow = 1  # מתחילים מאינדקס 1 כי האלמנט הראשון תמיד ייחודי
#
#         for fast in range(1, original_length):
#             # אם האלמנט הנוכחי שונה מהקודם
#             if nums[fast] != nums[fast - 1]:
#                 nums[slow] = nums[fast]  # מעתיקים אותו למקום הנכון
#                 slow += 1
#
#         # ממלאים את השאר ב-"_"
#         for i in range(slow, original_length):
#             nums[i] = "_"
#
#         return slow  # מחזירים את אורך המערך החדש (ללא ה-"_")
#
#
# # דוגמת שימוש
# if __name__ == "__main__":
#     sol = Solution()
#
#     # דוגמה 1 - כמו בדוגמה שלך
#     nums1 = [1, 1, 2, 3]
#     print(f"לפני: {nums1}")
#     new_length1 = sol.removeDuplicates(nums1)
#     print(f"אחרי: {nums1}, אורך ייחודי: {new_length1}")
#     print()
#
#     # דוגמה 2 - מערך לא ממוין עם כפילויות רבות
#     nums2 = [3, 1, 2, 3, 1, 4, 2]
#     print(f"before:{nums2}")
#     new_length2 = sol.removeDuplicates(nums2)
#     print(f"after:{nums2}, len {new_length2}")
#     print()
#
#     # דוגמה 3 - כפילויות רבות
#     nums3 = [5, 5, 5, 1, 1, 2]
#     print(f"לפני: {nums3}")
#     new_length3 = sol.removeDuplicates(nums3)
#     print(f"אחרי: {nums3}, אורך ייחודי: {new_length3}")
#     print()
#
#     # דוגמה 4 - מערך ללא כפילויות
#     nums4 = [1, 2, 3, 4]
#     print(f"לפני: {nums4}")
#     new_length4 = sol.removeDuplicates(nums4)
#     print(f"אחרי: {nums4}, אורך ייחודי: {new_length4}")

###########################################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:  # אם המערך רק
#             return 0
#         l = []
#         for i in range(len(prices) - 1):
#             delta = prices[i + 1] - prices[i]
#             if delta > 0:
#                 l.append(delta)
#         return sum(l)
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     prices1 = [3, 1, 5, 4, 6]
#     print(sol.maxProfit(prices1))

###########################################################################

# class Solution:
#     def rotate_method1_new_array(self, nums: List[int], k: int) -> None:
#         """
#         שיטה 1: יצירת מערך חדש
#         הכי פשוטה להבנה - O(n) space, O(n) time
#         """
#         n = len(nums)
#         k = k % n
#
#         if k == 0:
#             return
#
#         # יוצרים מערך חדש
#         result = [0] * n
#
#         # כל אלמנט במקום i יעבור למקום (i + k) % n
#         for i in range(n):
#             result[(i + k) % n] = nums[i]
#
#         # מעתיקים בחזרה למערך המקורי
#         nums[:] = result
#         print(nums)
# # הדגמה מפורטת של האלגוריתם
# if __name__ == "__main__":
#     sol = Solution()
#
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     print(sol.rotate_method1_new_array(nums,k))


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     return False
#         return True
#
# if __name__ == "__main__":
#     sol = Solution()
#     nums = [1,2,3,1]
#     print(sol.containsDuplicate(nums))


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = 0
#         for num in nums:
#             result ^= num
#         return result
#
#     #אינדקסולוגיה לא עובד עם מספרים שליליים!
#     # def singleNumber(self, nums: List[int]) -> int:
#     #     arr=[0]*len(nums)
#     #     for i in range(len(nums)):
#     #         arr[nums[i]]+=1
#     #     for i in range(len(nums)):
#     #         if arr[i]==1:
#     #             return i
#         #return arr.index(1)
#
# if __name__ == "__main__":
#     sol = Solution()
#     nums = [1,3,4,1,3,5,5]
#     print(sol.singleNumber(nums))

########################################################
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#     # שלב 1: ספירת תווים
#         char_count = {}
#         for char in s:
#             char_count[char] = char_count.get(char, 0) + 1
#
#     # שלב 2: מציאת הראשון הייחודי
#         for i, char in enumerate(s):
#             if char_count[char] == 1:
#                 return i
#
#         return -1


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     s = "anagrama"
#     t = "nagaram"
#     print(sol.isAnagram(s,t))


#####################################################
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         only_letters = re.sub(r'[^A-Za-z]', '', s)
#         only_letters = only_letters.lower()
#         l1 = list(only_letters)[::-1]
#         only_letters=list(only_letters)
#         if l1 == only_letters:
#             return True
#         else:
#             return False
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     s = "A man, a plan, a canal: Panama"
#     print(sol.isPalindrome(s))

###################################################################
# import re
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = s.lstrip()  # הסר רווחים בתחילת המחרוזת
#
#         if not s:
#             return 0
#
#         sign = 1
#         if s[0] == '-':
#             sign = -1
#             s = s[1:]
#         elif s[0] == '+':
#             s = s[1:]
#
#         # השתמש ב-regex כדי למצוא רצף ספרות בתחילת המחרוזת
#         match = re.match(r'\d+', s)
#         if not match:
#             return 0
#
#         num_str = match.group()
#         num = sign * int(num_str)
#
#         INT_MIN = -2 ** 31
#         INT_MAX = 2 ** 31 - 1
#
#         if num < INT_MIN:
#             return INT_MIN
#         if num > INT_MAX:
#             return INT_MAX
#
#         return num
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     s = "-63541337c0d3"
#     print(sol.myAtoi(s))

###################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def deleteNode(self, node):
        """
        מחיקת נוד ברשימה מקושרת - ללא גישה לראש!

        הרעיון המרכזי:
        מכיוון שאין לנו גישה לנוד הקודם, לא יכולים "לדלג" על הנוד.
        במקום זה, נעתיק את הערך מהנוד הבא ונמחק את הנוד הבא!

        Time: O(1), Space: O(1)
        """
        # העתק את הערך מהנוד הבא
        node.val = node.next.val

        # "מחק" את הנוד הבא על ידי דילוג עליו
        node.next = node.next.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head


def create_linked_list(values):
    """יוצר רשימה מקושרת מרשימת ערכים"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def find_node_with_value(head, target_value):
    """מוצא נוד עם ערך מסוים"""
    current = head
    while current:
        if current.val == target_value:
            return current
        current = current.next
    return None


def print_linked_list(head):
    """מדפיס רשימה מקושרת בצורה יפה"""
    if not head:
        return "Empty list"

    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next

    return " -> ".join(values) + " -> None"




if __name__ == "__main__":
    sol = Solution()
    # יצירת רשימה מקושרת: 4 -> 5 -> 1 -> 9 -> None
    values = [1,2,3,4,5]
    n=2
    head = create_linked_list(values)
    sol.removeNthFromEnd(head,n)
    print(f"רשימה מקורית: {print_linked_list(head)}")

    # מציאת הנוד עם הערך 5
    target_value = 5
    node_to_delete = find_node_with_value(head, target_value)

    if not node_to_delete:
        print(f"נוד עם ערך {target_value} לא נמצא!")
    else:
        print(f"נוד למחיקה: {node_to_delete.val}")

        # ביצוע המחיקה
        sol = Solution()
        sol.deleteNode(node_to_delete)

        print(f"רשימה אחרי מחיקה: {print_linked_list(head)}")
        print("\nהמחיקה הושלמה בהצלחה! ✅")

    print("\n" + "=" * 50)

