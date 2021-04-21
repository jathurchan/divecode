class ZeroEvenOdd(object):
    """
    1116. Print Zero Even Odd

    Suppose you are given the following code:
    class ZeroEvenOdd {
        public ZeroEvenOdd(int n) { ... }      // constructor
        public void zero(printNumber) { ... }  // only output 0's
        public void even(printNumber) { ... }  // only output even numbers
        public void odd(printNumber) { ... }   // only output odd numbers
    }
    The same instance of ZeroEvenOdd will be passed to three different threads:
    Thread A will call zero() which should only output 0's.
    Thread B will call even() which should only ouput even numbers.
    Thread C will call odd() which should only output odd numbers.
    Each of the threads is given a printNumber method to output an integer. Modify
    the given program to output the series 010203040506... where the length of the series must be 2n.
    """

    def __init__(self, n):
        self.n = n
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        
        
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        
        
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        
        