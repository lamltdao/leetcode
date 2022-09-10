from collections import deque

class TextEditor:

    def __init__(self):
        self.before_cursor = deque()
        self.after_cursor = deque()

    def addText(self, text: str) -> None:
        for i in range(len(text)):
            self.before_cursor.append(text[i])

    def deleteText(self, k: int) -> int:
        num_del = min(len(self.before_cursor), k)
        for i in range(num_del):
            self.before_cursor.pop()
        return num_del

    def cursorLeft(self, k: int) -> str:
        # move chars from before_cursor to after_cursor
        num_char_moved = min(k, len(self.before_cursor))
        for i in range(num_char_moved):
            self.after_cursor.appendleft(self.before_cursor.pop())
        # return chars to the left of cursor
        left_chars = [] 
        num_chars_returned = min(10, len(self.before_cursor))
        for i in range(num_chars_returned):
            left_chars.append(self.before_cursor[len(self.before_cursor)-num_chars_returned+i])
        return ''.join(left_chars)
        
    def cursorRight(self, k: int) -> str:
        # move chars from after_cursor to before_cursor
        num_char_moved = min(k, len(self.after_cursor))
        for i in range(num_char_moved):
            self.before_cursor.append(self.after_cursor.popleft())
        # return chars to the left of cursor
        left_chars = [] 
        num_chars_returned = min(10, len(self.before_cursor))
        for i in range(num_chars_returned):
            left_chars.append(self.before_cursor[len(self.before_cursor)-num_chars_returned+i])
        return ''.join(left_chars)


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)