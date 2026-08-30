class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1 = []
        list2 = []
        num1 = ""
        num2 = ""
        result = 0
        currentL1 = l1
        currentL2 = l2
        while currentL1:
            list1.insert(0, currentL1.val)

            currentL1 = currentL1.next
        while currentL2:
            list2.insert(0, currentL2.val)

            currentL2 = currentL2.next    
        for i in range(0, len(list1)):
            num1 = num1 + str(list1[i])
        for i in range(0, len(list2)):
            num2 = num2 + str(list2[i])
        result ="".join( reversed(str(int(num1) + int(num2))))
        print(result)
        dummy = ListNode(0)
        current=dummy
        for i in range(0, len(result)):
            node=ListNode(int(result[ i]))
            current.next=node
            current=current.next
        
            
        return(dummy.next)
