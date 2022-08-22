#include <iostream>
#include <stdio.h>

using namespace std;

class Node{

public:

    int value;
    Node *next = nullptr;
};

class LinkedList{
    Node *head;

    /**bool isEmpty(){
        return head == NULL;
    }*/

public:

    LinkedList(){  // Construtor
        head = NULL;
    } 

    void print_list(){
        Node* temp = new Node;  // Instanciação do nó temp
        temp = head;  // temp percorre a lista
        if (temp == NULL){  // Se temp for nulo, a lista ta vazia
            cout<<"Lista vazia"<<endl;
            return;
        }

        while (temp != NULL){  // Temp percorrendo e printando a lista
            cout << temp->value << endl;
            temp = temp->next;
        }
    }


    Node* busca(int value){  // Busca um valor específico na lista 
        Node* temp = new Node;
        temp = head;  // Temp é do tipo Node que percorre a lista
        while(temp != NULL){  // Mesma iteração da print_list()
            if (temp->value == value){
                return temp;  // Se achar o valor, retorna o nó buscado
            }
            temp = temp->next;
        }
        return NULL;
    }


    void insert(Node* temp, int value){  // Insere um valor na lista, com o temp já percorrido
        Node* new_node = new Node;  // Criação do nó
        new_node->value = value;  // Recebe o valor passado pelo usuário
        new_node->next = temp->next;  // O Próximo do novo nó recebe o valor anterior temp.next. Esse temp é 1 nó atrás do nó que deseja inserir.
        temp->next = new_node;  // O Próximo do temp aponta pro novo nó, e assim reencadeia a lista e insere com sucesso.
    }

    void insert_prepend(int value){  // Inserção no começo da lista O(1)
        Node* new_node = new Node;
        new_node->value = value;
        new_node->next = head; // Novo nó aponta pra cabeça
        head = new_node;  // Cabeça vira o novo nó
    }


    void insert_append(int value){  // Inserção no final da lista
        if (head == NULL){  // Se lista vazia, insere por meio do prepend.
            insert_prepend(value);
            return;
        }
        Node* temp = new Node;  // Crio um nó temp que aponta pra cabeça e percorre a lista
        temp = head;
        while(temp->next != NULL){ // Percorrimento da lista
            temp = temp->next;
        }
        insert(temp, value);  // Ao chegar no final, insere normalmente.
    }


    Node* remove(Node* temp){  // Remove o nó e retorna o nó removido. Aqui a lista já foi percorrida pelo método de busca.
        if (temp == NULL){  // Se vazio, retorna nada.
            return NULL;
        }
        temp->next = temp->next->next;  // O próximo do temp aponta pro próximo do próximo, pois entre eles é o valor que se deseja remover.
        return temp->next;
    }


    bool inverter_lista(){
        if (head == NULL){  // Se a lista estiver vazia, retorna False, ou seja, não é possível inverter.
            return false;
        }
        Node* temp = new Node;  // Criação de 3 auxiliares para inverter a lista.
        Node* after = new Node;
        Node* before = new Node;
        before = head;  // Antes aponta pra cabeça
        temp = before->next;  // Iterador aponta pro depois do antes
        after = temp->next;  // E o depois aponta pro depois do atual
        before->next = NULL;  // Faço o de antes apontar pra nada
        while(temp != NULL){
            temp->next = before;  // Depois o próximo do meio inverte o polo, aponta pro anterior
            before = temp;  // o anterior aponta pro do meio
            temp = after;  // Temp percorre pra direita
            after = after->next;  // O depois pecorre pra direita também
        }
        return true;  // True significa que inverteu a lista.
    }

};

int main(){
    LinkedList l;
    l.print_list();
    l.insert_append(5);
    l.insert_append(7);
    l.insert_append(10);
    l.inverter_lista();
    l.print_list();
}