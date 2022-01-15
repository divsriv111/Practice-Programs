package queueByArray;

public class Main {
    public static void main(String[] args) {
        var queue = new QueueArray(3);
        //System.out.println(queue.isFull());
        //System.out.println(queue.isEmpty());
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);
        queue.enQueue(4);
        //System.out.println(queue.isFull());
        //System.out.println(queue.isEmpty());
        System.out.println(queue.deQueue());
        System.out.println(queue.peek());
        System.out.println(queue.peek());
    }
}
