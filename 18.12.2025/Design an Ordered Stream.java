class OrderedStream {
    private String[] stream;
    private int ptr;
    public OrderedStream(int n) {
        stream = new String[n];
                ptr = 0;
    }
    public List<String> insert(int idKey, String value) {
        int index = idKey - 1;
        stream[index] = value;
        List<String> res = new ArrayList<>();
        while(ptr < stream.length && stream[ptr] != null){
            res.add(stream[ptr]);
            ptr++;
        }
        return res;
    }
}
