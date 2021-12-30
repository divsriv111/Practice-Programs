package com.circularSinglyLinkedList;

public class Main {
    public static void main(String[] args) {
        var cSLL = new CircularSinglyLinkedList();
        cSLL.createCSLL(5);
        System.out.println(cSLL.head.value);
        System.out.println(cSLL.head.next.value);
    }
}
