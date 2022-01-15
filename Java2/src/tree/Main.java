package tree;

public class Main {
    public static void main(String[] args) {
        //Root
        var drinks = new TreeNode("Drinks");
        //Node 1
        var hot = new TreeNode("Hot");
        var cold = new TreeNode("Cold");

        //Node 2
        var tea = new TreeNode("Tea");
        var coffee = new TreeNode("Coffee");
        var wine = new TreeNode("Wine");
        var beer = new TreeNode("Beer");

        drinks.addChild(hot);
        drinks.addChild(cold);
        hot.addChild(tea);
        hot.addChild(coffee);
        cold.addChild(wine);
        cold.addChild(beer);

        System.out.println(drinks.print(0));
    }
}
