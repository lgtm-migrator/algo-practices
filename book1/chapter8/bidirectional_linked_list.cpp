#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    Node *prev;
    Node *next;
    string name;

    Node(string _name = "") : prev(NULL), next(NULL), name(_name) {}
};

Node *nil;

void initialize()
{
    nil = new Node();
    nil->prev = nil;
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

// v: 挿入するノード
// p: 挿入したい場所のノード
// prevも修正する必要がある
void insert(Node *v, Node *p = nil)
{
    v->next = p->next;
    p->next->prev = v;
    v->prev = p;
    p->next = v;
}

void erase(Node *v)
{
    // vが番兵の場合は何もしない
    if (v == nil)
    {
        return;
    }
    v->next->prev = v->prev;
    v->prev->next = v->next;
    // メモリの解放
    delete v;
}

int main()
{
    initialize();

    // データ生成
    vector<string> names = {
        "yamamoto",
        "watanabe",
        "tanaka",
        "yamada",
        "aoki",
    };

    // 削除される予定のノード
    Node *tanaka;
    for (int i = 0; i < (int)names.size(); i++)
    {
        Node *node = new Node(names[i]);
        insert(node);

        if (node->name == "tanaka")
        {
            tanaka = node;
        }
    }
    cout << "before: ";
    printList();
    erase(tanaka);
    cout << "after: ";
    printList();
    return 0;
}