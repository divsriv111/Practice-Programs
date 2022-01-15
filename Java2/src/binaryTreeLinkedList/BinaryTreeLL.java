package binaryTreeLinkedList;

import java.util.LinkedList;
import java.util.Queue;

public class BinaryTreeLL {
    BinaryNode root;

    public BinaryTreeLL(){
        root = null;
    }

    public void preOrder(BinaryNode node){
        if(node == null)
            return;
        System.out.print(node.value + "->");
        preOrder(node.left);
        preOrder(node.right);
    }

    public void inOrder(BinaryNode node){
        if(node == null)
            return;

        inOrder(node.left);
        System.out.print(node.value + "->");
        inOrder(node.right);
    }

    public void postOrder(BinaryNode node){
        if(node == null)
            return;

        postOrder(node.left);
        postOrder(node.right);
        System.out.print(node.value + "->");
    }

    public void levelOrder(){
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);
        while(!queue.isEmpty()){
            var presentNode = queue.remove();
            System.out.print(presentNode.value + "->");

            if (presentNode.left != null)
                queue.add(presentNode.left);

            if (presentNode.right != null)
                queue.add(presentNode.right);
        }
    }

    public void search(String value){
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);
        while(!queue.isEmpty()){
            var presentNode = queue.remove();
            if(presentNode.value == value){
                System.out.println("\nValue found");
                return;
            }


            if (presentNode.left != null)
                queue.add(presentNode.left);

            if (presentNode.right != null)
                queue.add(presentNode.right);
        }
        System.out.println("Value not found");
    }
}
