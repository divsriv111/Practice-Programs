package queueByArray;

public class QueueArray {
    int[] arr;
    int topOfQueue;
    int beginningOfQueue;

    public QueueArray(int size){
        arr = new int[size];
        beginningOfQueue = -1;
        topOfQueue = -1;
        System.out.println("Queue successfully created with size " + size);
    }

    public boolean isFull(){
        return topOfQueue == arr.length - 1;
    }

    public boolean isEmpty(){
        return (beginningOfQueue == -1) || (beginningOfQueue == arr.length);
    }

    public void enQueue(int value){
        if(isFull()){
            System.out.println("Queue is full");
        } else if(isEmpty()) {
            beginningOfQueue = 0;
            topOfQueue++;
            arr[topOfQueue] = value;
            System.out.println("Successfully added value " + value + " to the queue");
        } else {
            topOfQueue++;
            arr[topOfQueue] = value;
            System.out.println("Successfully added value " + value + " to the queue");
        }
    }

    public int deQueue(){
        var result = -1;
        if(isEmpty()){
            System.out.println("Queue is Empty");
        } else {
            result = arr[beginningOfQueue];
            beginningOfQueue++;
            if(beginningOfQueue > topOfQueue){
                beginningOfQueue = topOfQueue = -1;
            }
        }
        return result;
    }

    public int peek(){
        if(!isEmpty()){
            return arr[beginningOfQueue];
        }
        System.out.println("Queue is Empty");
        return -1;
    }
    public void delete(){
        arr = null;
        System.out.println("Queue deleted successfully");
    }
}
