package stackByLinkedList;

public class Stack {
    LinkedList linkedList;

    public Stack(){
        linkedList = new LinkedList();
    }

    public void push(int value){
        linkedList.insertInLinkedList(value, 0);
        System.out.println("Inserted " + value + " in the Stack");
    }

    public boolean isEmpty(){
        return linkedList.head == null;
    }

    public int pop(){
        int result = -1;
        if(isEmpty()){
            System.out.println("Stack is Empty");
        } else {
            result = linkedList.head.value;
            linkedList.deletionOfNode(0);
        }
        return result;
    }

    public int peek(){
        if (isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        return linkedList.head.value;
    }

    public void deleteStack(){
        linkedList.deleteSLL();
        System.out.println("Stack deleted successfully");
    }
}
