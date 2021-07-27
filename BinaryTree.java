import org.graalvm.compiler.replacements.nodes.arithmetic.IntegerMulExactNode;

class Node{
    int key;
    Node left,right;

    public Node(int item){
        key = item;
        left=right=null;
    }
}

