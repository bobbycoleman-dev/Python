class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head != None:
            runner = self.head
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
        return self

    def remove_val(self, val):
        # If val does not exist check
        nodes = []
        val_is_valid = False
        current = self.head
        while current.next != None:
            nodes.append(current)
            current = current.next
        nodes.append(current)

        for node in nodes:
            if node.value == val:
                val_is_valid = True
                continue

        if val_is_valid:
            runner = self.head
            # First value
            if runner.value == val and runner == self.head:
                self.remove_from_front()
            while runner.value != val:
                runner = runner.next
            # Last value
            if runner.next == None:
                self.remove_from_back()
            # Middle Values
            else:
                placeholder = runner
                runner = self.head
                while runner.next != None:
                    if runner.next == placeholder:
                        runner.next = placeholder.next
                    else:
                        runner = runner.next
        else:
            print("Value does not exist in Singly List")
        return self

    def insert_at(self, val, n):
        list_length = 0
        insert_at = 0
        runner = self.head
        list_length += 1
        while runner.next != None:
            list_length += 1
            runner = runner.next
        # First value in list
        if n == 1 or n == 0:
            self.add_to_front(val)
        # Middle values in list
        if n > 0 and n <= list_length:
            new_node = SLNode(val)
            current = self.head
            insert_at += 1
            while insert_at != n:
                insert_at += 1
                if insert_at == n:
                    new_node.next = current.next
                    current.next = new_node
                else:
                    current = current.next
            return self
        # Last value in list
        if n > list_length:
            self.add_to_back(val)

        return self


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


my_list = SList()
my_list.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").add_to_back(
    "E"
)

my_list.remove_val("Bob").print_values()
