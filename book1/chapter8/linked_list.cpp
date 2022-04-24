#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Node
{
    Node *next;
    string name;

    Node(string _name = "") : next(NULL), name(_name) {}
};

Node *nil;

void initialize()
{
    nil = new Node();
    nil->next = nil;
}

void printList()
{
    Node *current = nil->next;
    for (; current != nil; current = current->next)
    {
        cout << current->name << " -> ";
    }
    cout << endl;
}

// ノードpの直後にノードvを挿入する
void insert(Node *v, Node *p = nil)
{
    v->next = p->next;
    p->next = v;
}

int main()
{
    initialize();

    // 配列
    vector<string> names = {
        "yamamoto",
        "watanabe",
        "tanaka",
        "yamada",
        "aoki",
    };
    for (int i = 0; i < names.size(); i++)
    {
        Node *node = new Node(names[i]);
        // 先頭に入れる
        insert(node);
        cout << "step " << i << ": ";
        printList();
    }
    return 0;
}