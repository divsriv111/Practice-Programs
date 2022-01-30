package binaryTreeArray;

public class BinaryTree {
    String[] arr;
    int lastUsedIndex;

    public BinaryTree(int size){
        arr = new String[size + 1];
        lastUsedIndex = 0;
        System.out.println("Blank Tree of size " + size + " has been created");
    }

    // isFull
    boolean isFull(){
        return arr.length - 1 == lastUsedIndex;
    }

    public void insert(String value){
        if (!isFull()){
            arr[lastUsedIndex + 1] = value;
            lastUsedIndex ++;
            System.out.println("The value of "+ value + "has been inserted");
        } else{
            System.out.println("The BT is full");
        }
    }

   public void preOrder(int index){
        if (index > lastUsedIndex){
            return;
        }
       System.out.print(arr[index] + " ");
        preOrder(index * 2);    //left child
       preOrder(index * 2 + 1); //right child
    }
}
