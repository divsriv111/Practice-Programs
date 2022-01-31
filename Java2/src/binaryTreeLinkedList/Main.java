package binaryTreeLinkedList;

public class Main {
    public static void main(String[] args) {
        var binaryTree = new BinaryTreeLL();
        /*
        var N1 = new BinaryNode("N1");
        var N2 = new BinaryNode("N2");
        var N3 = new BinaryNode("N3");
        var N4 = new BinaryNode("N4");
        var N5 = new BinaryNode("N5");
        var N6 = new BinaryNode("N6");
        var N7 = new BinaryNode("N7");
        var N8 = new BinaryNode("N8");
        var N9 = new BinaryNode("N9");

        N1.left = N2;
        N1.right = N3;

        N2.left = N4;
        N2.right = N5;

        N3.left = N6;
        N3.right = N7;

        N4.left = N8;
        N4.right = N9;

        binaryTree.root = N1;

        System.out.println("Pre order");
        binaryTree.preOrder(binaryTree.root);
        System.out.println("\nIn order");
        binaryTree.inOrder(binaryTree.root);
        System.out.println("\nPost order");
        binaryTree.postOrder(binaryTree.root);
        System.out.println("\nLevel order");
        binaryTree.levelOrder();

        binaryTree.search("N5");
        binaryTree.search("N99");
        */
        binaryTree.insert("N1");
        binaryTree.insert("N2");
        binaryTree.insert("N3");
        binaryTree.insert("N4");
        binaryTree.insert("N5");
        binaryTree.insert("N6");
        binaryTree.levelOrder();
    }
}
