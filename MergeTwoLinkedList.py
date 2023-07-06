import ListNode
class MergeTwoLinkedList:
    
    def mergeTwoLinkedList(num1 : ListNode, num2 :ListNode):
        head = ListNode()
        current = head

        while num1 and num2:
            if num1 < num2 :
                current.next = num1
                num1 = num1.next
            else:
                current.next = num2
                num2 = num2.next

        current.next  = num1 or num2

        return head.next

    print(mergeTwoLinkedList([1,2,4], [1,3,4]))

            

        