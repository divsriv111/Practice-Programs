#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

void push(Node **head_ref, int new_data)
{
    Node *new_node = new Node();
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

void deleteNode(Node **head_ref, int key)
{
    Node *temp = *head_ref;
    Node *prev = NULL;

    if (temp != NULL && temp->data == key)
    {
        *head_ref = temp->next; // Changed head
        delete temp;            // free old head
        return;
    }

    else
    {
        while (temp != NULL && temp->data != key)
        {
            prev = temp;
            temp = temp->next;
        }

        if (temp == NULL)
            return;

        prev->next = temp->next;

        delete temp;
    }
}

void printList(Node *node)
{
    while (node != NULL)
    {
        cout << node->data << " ";
        node = node->next;
    }
}

void deleteGreaterNodes(Node **head_ref)
{
    Node *temp = *head_ref;

    int i = 10;

    if (temp == NULL)
        return;

    while (temp->next->next != NULL)
    {
        cout << temp->data << endl;

        if (temp->data < temp->next->data)
            deleteNode(&*head_ref, temp->data);

        temp = temp->next;

        if (i--)
            return;
    }
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    Node *head = NULL;

    push(&head, 9);
    push(&head, 5);
    push(&head, 6);
    push(&head, 2);
    push(&head, 7);

    puts("Created Linked List: ");
    printList(head);

    deleteGreaterNodes(&head);
    puts("\nLinked List after Deletion of 1: ");

    printList(head);

    return 0;
}
