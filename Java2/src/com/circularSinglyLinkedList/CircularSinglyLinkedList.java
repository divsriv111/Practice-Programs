package com.circularSinglyLinkedList;

public class CircularSinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    public Node createCSLL(int nodeValue){
        var node = new Node();
        node.value = nodeValue;
        node.next = node;
        head = tail = node;
        size = 1;
        return head;
    }
}
