class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

快慢指针，我其实用的不是很好，我觉得我需要学习一下双指针
破解push pull困局
再次提交一个新信息
我好像快明白add . commit -m" shsidhis" push pull 的关系了
jcihixh\jixixh
jixu1
jixu1