#include <iostream>

using namespace std;

class Node{
public:
    int value;
    Node *next = nullptr;
};

class LinkedList{
    Node *head;

    bool isEmpty(){
        return head == NULL;
    }

public:
    LinkedList(){  // Construtor
        head = NULL;
    } 

    int print_list(){
        Node* temp = new Node;
        temp = head;
        if (temp == NULL){
            cout<<"Lista vazia"<<endl;
            return NULL;
        }

        while (temp != NULL){
            cout << temp->value << endl;
            temp = temp->next;
        }
    }


    Node* busca(int value){
        Node* temp = new Node;
        temp = head;
        while(temp != NULL){
            if (temp->value == value){
                return temp;
            }
            temp = temp->next;
        }
        return NULL;
    }


    int insert(Node* p, int value){
        Node* new_node = new Node;
        new_node->value = value;
        new_node->next = p->next;
        p->next = new_node;
    }

    int insert_prepend(int value){
        Node* new_node = new Node;
        new_node->next = 
    }
};

int main(){
    LinkedList l;
    l.print_list();
}