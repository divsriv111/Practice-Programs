public class Shuffle_String {
    public static void main(String[] args) {
        String s = "codeleet";
        int[] indices = { 4, 5, 6, 7, 0, 2, 1, 3 };

        var str = s.toCharArray();
        var ans = new char[s.length()];
        for (var i = 0; i < s.length(); i++) {
            ans[indices[i]] = str[i];
        }
        var res = new String(ans);
        // return res;
        System.out.println(res);
    }

}
