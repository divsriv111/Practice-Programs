package com.circularSinglyLinkedList;

public class Main {
    public static void main(String[] args) {
        var cSLL = new CircularSinglyLinkedList();
        cSLL.createCSLL(5);

        System.out.println(cSLL.head.next.value);
        cSLL.insertCSLL(4, 0);
        cSLL.insertCSLL(1, 1);
        cSLL.insertCSLL(8, 2);
        cSLL.insertCSLL(9, 99);

        cSLL.traverseCSLL();
    }
}
