package linkedlist.circularDoublyLinkedList;

public class CircularDoublyLinkedList {
    public DoublyNode head;
    public DoublyNode tail;
    public int size;

    //create CDLL
    public DoublyNode createCDLL(int nodeValue){
        var node = new DoublyNode();
        node.value = nodeValue;
        node.prev = node.next = node;
        head = tail = node;
        size = 1;
        return head;
    }
}
