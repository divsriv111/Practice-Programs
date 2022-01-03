package com.doublyLinkedList;

public class Main {
    public static void main(String[] args) {
        var dll = new DoublyLinkedList();
        dll.createDLL(5);
        System.out.println(dll.head.value);
    }
}
