from pytest import raises
from stack import Stack, StackError


class SetupTeardownMixin:
    def setup_method(self):
        self.test_stack = Stack(size=5)

        self.test_stack.push(42)
        self.test_stack.push(20)
        self.test_stack.push(33)
        self.test_stack.push([1, 2, 3])
        self.test_stack.push('Data')


class TestStack(SetupTeardownMixin):
    def test_empty(self):
        while not self.test_stack.is_empty():
            self.test_stack.pop()

        assert len(self.test_stack) == 0
        assert self.test_stack.is_empty()

        with raises(StackError) as stack_exception:
            self.test_stack.pop()

        assert str(stack_exception.value) == "Stack Underflow!"

    def test_fool(self):
        assert self.test_stack.is_full()

        with raises(StackError) as stack_exception:
            self.test_stack.push('Extra data')

        assert str(stack_exception.value) == "Stack Overflow!"

    def test_push_pop(self):
        assert self.test_stack.pop() == 'Data'
        assert self.test_stack.pop() == [1, 2, 3]
        assert len(self.test_stack) == 3
        assert self.test_stack.peek() == 33


