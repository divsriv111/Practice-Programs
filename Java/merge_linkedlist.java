class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode ans = new ListNode();
        ListNode i = list1.next, j = list2.next, ansHead = new ListNode();
        var k = 0;

        while (i != null && j != null) {
            if (i.val > j.val) {
                ans = new ListNode(j.val, new ListNode());
                j = j.next;
            } else {
                ans = new ListNode(i.val, new ListNode());
                i = i.next;
            }
            if (k == 0)
                ansHead = ans;
            k++;
            ans = ans.next;
        }

        while (i != null) {
            ans = new ListNode(i.val, new ListNode());
            ans = ans.next;
            i = i.next;
        }

        while (j != null) {
            ans = new ListNode(j.val, new ListNode());
            ans = ans.next;
            j = j.next;
        }

        return ansHead;
    }

    public void Display(ListNode l) {
        while (l != null) {
            System.out.println(l.val);
            l = l.next;
        }
    }
}

public class merge_linkedlist {
    public static void main(String[] args) {
        var list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(3);

        var list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        // ==============================
        var obj = new Solution();
        var a = obj.mergeTwoLists(list1, list2);
        obj.Display(a);
    }
}
