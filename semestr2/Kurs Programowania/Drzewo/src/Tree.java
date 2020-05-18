// element drzewa
class TreeElem<T extends Comparable<T>> {

    final T elem;

    TreeElem<T> left;

    TreeElem<T> right;

    TreeElem(T elem)
    {

        this.elem = elem;

        left = null;

        right = null;

    }

    public String toString() { return elem.toString(); }

}

public class Tree<T extends Comparable<T>> {

    private TreeElem<T> root;

    // tworzenie nowego drewa
    public Tree() { root = null; }


    // wstawianie wartosci do drzewa
    public void insert(T elem) { root = ins(elem, root); }


    private TreeElem<T> ins(T elem, TreeElem<T> w) {

        if( w==null ) return new TreeElem<T>(elem);

        if( elem.compareTo(w.elem)<0 )
            w.left = ins(elem, w.left);

        else if( elem.compareTo(w.elem)>0)
            w.right = ins(elem, w.right);
        return w;
    }


    // wyszukiwanie elementu true jesli jest w tablicy false jesli nie ma go
    public boolean isElement(T elem) { return isElem(elem,root); }

    // sprawdzenie czy element istnieje
    private boolean isElem(T elem, TreeElem<T> w) {

        if( w==null ) return false;

        if( elem.compareTo(w.elem)==0 ) return true;

        if( elem.compareTo(w.elem)<0)
            return isElem(elem, w.left);

        else
            return isElem(elem, w.right);
    }

    // znalezienie konkretnego elementu i zwrocenie go
    private TreeElem<T> isElemReturn(T elem, TreeElem<T> w) {

        if( w==null ) return null;

        if( elem.compareTo(w.elem)==0 ) return w;

        if( elem.compareTo(w.elem)<0)
            return isElemReturn(elem, w.left);

        else
            return isElemReturn(elem, w.right);
    }

    private TreeElem<T> findParent(T elem, TreeElem<T> w, TreeElem<T> parent){



        if( w==null ) return null;

        if( elem.compareTo(w.elem)==0 ) return parent;

        if( elem.compareTo(w.elem)<0)
            return findParent(elem, w.left, w);

        else
            return findParent(elem, w.right, w);
    }

    // wypisywanie drzewa
    public String toString() { return toS(root); }

    private String toS(TreeElem<T> w) {

        if( w!=null )
            return toS(w.left)+" "+w.elem+" "+toS(w.right);

        return "";
    }

    public void delete(T elem) {dElem(elem);}

    private void dElem(T elem){
        TreeElem<T> w = isElemReturn(elem, root);
        TreeElem<T> parent = findParent(elem, root, null);
        TreeElem<T> temp;
        if(w.equals(null) == false){
            if(w.left == null && w.right == null){
                if(elem.compareTo(parent.elem) < 0) parent.left = null;
                else parent.right = null;
            }
            else if(w.left == null && w.right != null){
                if(elem.compareTo(parent.elem) < 0) parent.left = w.right;
                else parent.right = w.right;
            }
            else if(w.left != null && w.right == null){
                if(elem.compareTo(parent.elem) < 0) parent.left = w.left;
                else parent.right = w.left;
            }
            else {
                // jesli usuwamy glowny korzen drzewa to nie ma on parenta wiec taki maly exepcion w postaci zgrabnego ifa
                if (parent == null) {
                    temp = w.right;
                    // przeniesienie prawych dzieci lewego dziecka usuwanego elementu na lewe dzieci prawego dziecka usuwanego elementu
                    if (w.left.right != null && temp.left != null) {
                        // dojscie do ostatniego najmniejszego elementu - prawego dziecka - usuwanego elmentu
                        while (temp.left != null) temp = temp.left;
                    }
                    if(w.left.right != null) temp.left = w.left.right;
                    w.left.right = w.right;
                    root = w.left;
                }
                else {
                    System.out.println("a");
                    if (elem.compareTo(parent.elem) < 0) {
                        temp = w.right;
                        // przeniesienie prawych dzieci lewego dziecka usuwanego elementu na lewe dzieci prawego dziecka usuwanego elementu
                        if (w.left.right != null && temp.left != null) {
                            // dojscie do ostatniego najmniejszego elementu - prawego dziecka - usuwanego elmentu
                            while (temp.left != null) temp = temp.left;

                        }
                        temp.left = w.left.right;
                        parent.left = w.left;
                        w.left.right = w.right;
                    } else {
                        temp = w.right;
                        // przeniesienie prawych dzieci lewego dziecka usuwanego elementu na lewe dzieci prawego dziecka usuwanego elementu
                        if (w.left.right != null && temp.left != null) {
                            // dojscie do ostatniego najmniejszego elementu - prawego dziecka - usuwanego elmentu
                            while (temp.left != null) temp = temp.left;
                        }
                        temp.left = w.left.right;
                        parent.right = w.left;
                        w.left.right = w.right;
                    }
                }
            }
        }
    }
}
