package com.doublyLinkedList;

public class DoublyLinkedList {
    public DoublyNode head;
    public DoublyNode tail;
    public int size;

    public DoublyNode createDLL(int nodeValue){
        var node = new DoublyNode();
        node.value = nodeValue;
        node.prev = node.next = null;
        head = tail = node;
        size = 1;
        return head;
    }
}
