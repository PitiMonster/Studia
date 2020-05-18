public class Drzewo {
    public static void main(String[] args){
        Tree<String> d = new Tree<>();
        Tree<Integer> i = new Tree<>();

//        d.insert("bbbb");
//        d.insert("www");
//        d.insert("w");
//        d.insert("ww");
//        d.insert("a");
        i.insert(10);
        i.insert(5);
        i.insert(8);
        i.insert(7);
        i.insert(6);
        i.insert(3);
        i.insert(2);
        i.insert(4);
        i.insert(20);
        System.out.println(i.toString());
        //System.out.println(i.toString());
        //System.out.println(d.isElement("a"));
        i.delete(10);
        System.out.println(i.toString());
    }
}
