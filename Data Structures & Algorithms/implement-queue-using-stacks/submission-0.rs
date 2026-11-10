struct MyQueue {
    s1: Vec<i32>,
    s2: Vec<i32>,
}

impl MyQueue {
    pub fn new() -> Self {
        MyQueue{
            s1: Vec::new(),
            s2: Vec::new(),
        }
    }

    pub fn push(&mut self, x: i32) {
        self.s1.push(x);
    }

    pub fn pop(&mut self) -> i32 {
        if self.s2.is_empty(){
            while let Some(val)=self.s1.pop(){
                self.s2.push(val);
            }
        }
        self.s2.pop().unwrap()
    }

    pub fn peek(&self) -> i32 {
        if self.s2.is_empty(){
            while let Some(val)= self.s1.pop(){
                self.s2.push(val);
            }
        }
        self.s2.last().unwrap()
    }

    pub fn empty(&self) -> bool {
        self.s1.is_empty() && self.s2.is_empty()
    }
}

// Your MyQueue object will be instantiated and called as such:
// let obj = MyQueue::new();
// obj.push(x);
// let ret_2: i32 = obj.pop();
// let ret_3: i32 = obj.peek();
// let ret_4: bool = obj.empty();
