package linkedlist.singlylinkedlist;

public class Main {

    public static void main(String[] args) {
        var sList = new SinglyLinkedList();
        sList.createSinglyLinkedList(1);
        sList.insertInLinkedList(2,1);
        sList.insertInLinkedList(3,2);
        sList.insertInLinkedList(4,3);
        sList.insertInLinkedList(5,4);
        sList.insertInLinkedList(9,0);

        sList.traverseSinglyLinkedList();

        //sList.searchNode(4);
        //sList.searchNode(99);

        sList.deletionOfNode(3);
        sList.deletionOfNode(0);

        sList.traverseSinglyLinkedList();
    }
}
