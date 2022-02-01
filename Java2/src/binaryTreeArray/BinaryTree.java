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

    public void inOrder(int index){
        if (index > lastUsedIndex){
            return;
        }
        inOrder(index * 2);    //left child
        System.out.print(arr[index] + " ");
        inOrder(index * 2 + 1); //right child
    }

    public void postOrder(int index){
        if (index > lastUsedIndex){
            return;
        }
        postOrder(index * 2);    //left child
        postOrder(index * 2 + 1); //right child
        System.out.print(arr[index] + " ");
    }

    public void levelOrder(){
        for(var i = 1; i <= lastUsedIndex; i++){
            System.out.print(arr[i] + " ");
        }
    }

    public int search(String key){
        for(var i = 1; i <= lastUsedIndex; i++){
            if (arr[i] == key){
                System.out.print("Value exist in tree at location " + i);
                return i;
            }
        }
        System.out.print("Value do not found");
        return -1;
    }
}
