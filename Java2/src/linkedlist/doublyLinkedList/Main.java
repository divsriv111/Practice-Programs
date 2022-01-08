package linkedlist.doublyLinkedList;

public class Main {
    public static void main(String[] args) {
        var dll = new DoublyLinkedList();
        dll.createDLL(1);
        dll.insertDLL(2, 0);
        dll.insertDLL(3, 1);
        dll.insertDLL(4, 7);
        dll.traverseDLL();
        dll.reverseTraverseDLL();
        dll.searchNode(6);
        dll.searchNode(1);
    }
}
