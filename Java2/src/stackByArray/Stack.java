package stackByArray;

public class Stack {
    int[] arr;
    int topOfStack;

    public Stack(int size){
        arr = new int[size];
        topOfStack = -1;

        System.out.println("The stack is created with the size " + size);
    }

    public boolean isEmpty(){
        return topOfStack == -1;
    }

    public boolean isFull(){
        return topOfStack == arr.length - 1;
    }

    public void push(int value){
        if(isFull()){
            System.out.println("Stack is full");
        } else{
            arr[topOfStack + 1] = value;
            topOfStack++;
            System.out.println("The value is inserted successfully");
        }
    }

    public int pop(){
        if (isEmpty()){
            System.out.println("Stack is Empty");
            return -1;
        } else {
            var topValue = arr[topOfStack];
            topOfStack--;
            return topValue;
        }
    }

    public int peek(){
        if(isEmpty()){
            System.out.println("Stack is Empty");
            return -1;
        } else {
            return arr[topOfStack];
        }
    }

    public void deleteStack(){
        arr = null;
        topOfStack = -1;
        System.out.println("Stack successfully deleted");
    }

}
