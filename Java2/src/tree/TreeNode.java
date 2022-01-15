package tree;

import java.util.ArrayList;

public class TreeNode {
    String data;
    ArrayList<TreeNode> children;

    public TreeNode(String value){
        data = value;
        children = new ArrayList<>();
    }

    public void addChild(TreeNode node){
        children.add(node);
    }

    public String print(int level){
        String ret = "  ".repeat(level) + data + "\n";
        for(var node : children){
            ret += node.print(level + 1);
        }
        return ret;
    }

}
