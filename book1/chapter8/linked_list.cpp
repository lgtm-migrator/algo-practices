#include <iostream>

using namespace std;

struct Node
{
    Node *next;
    string name;

    Node(string _name = "") : next(NULL), name(_name) {}
};

// ノードpの直後にノードvを挿入する
void insert(Node *v, Node *p)
{
    v->next = p->next;
    p->next = v;
}

int main()
{
    return 0;
}