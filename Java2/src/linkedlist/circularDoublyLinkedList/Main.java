package linkedlist.circularDoublyLinkedList;

public class Main {
    public static void main(String[] args) {
        var cDLL = new CircularDoublyLinkedList();
        cDLL.createCDLL(4);
        System.out.println(cDLL.head.value);
    }
}
