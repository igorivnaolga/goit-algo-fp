class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("No previous Node")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list


    def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def merge_sorted_lists(self, other_list):
        merged = LinkedList()
        merged.head = self.sorted_merge(self.head, other_list.head)
        return merged
        

if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert_at_end(10)
    list1.insert_at_end(5)
    list1.insert_at_end(20)
    list1.insert_at_end(15)

    print("Original list:")
    list1.print_list()

    list1.reverse()
    print("Reversed list:")
    list1.print_list()

    list1.head = list1.merge_sort(list1.head)
    print("Sorted list:")
    list1.print_list()

    list2 = LinkedList()
    list2.insert_at_end(38)
    list2.insert_at_end(22)
    list2.insert_at_end(2)
    list2.head = list2.merge_sort(list2.head)

    merged_list = list1.merge_sorted_lists(list2)
    print("Merged sorted list:")
    merged_list.print_list()

