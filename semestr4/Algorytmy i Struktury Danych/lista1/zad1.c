#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int number;     // int value stored by node
    struct node* next;  // pointer to the next element of queue
} node_t;

typedef struct queue{
    node_t* front;  // pointer to front element of queue
    node_t* rare;   // pointer to rare element of queue
    size_t size;    // size of queue
} queue_t;

void push(queue_t* newQueue, int newNumber);
int pop(queue_t* newQueue);


void push(queue_t* newQueue, int newNumber){

    node_t* newNode = (node_t*)malloc(sizeof(node_t));

    if(newNode == NULL){
        printf("Failure during new node creation!");
        return;
    }

    // set default values to new node
    newNode->number = newNumber;
    newNode->next = NULL;


    if(newQueue->size == 0){
        // if queue is empty then set front and rare to indicate on new node
        newQueue->front = newNode;
        newQueue->rare = newNode;
    }
    else{
        // if queue is not empty then set rare->next to new node and rare to new node 
        newQueue->rare->next = newNode;
        newQueue->rare = newNode;
    }

    newQueue->size += 1;
    
    return;
}


int pop(queue_t* newQueue){
    
    if(newQueue->size == 0){
        printf("There is no element in the queue!");
        return 0;
    }

    int poppedNumber = newQueue->front->number;

    if(newQueue->size == 1){
        // if queue has one element then set front and rare to NULL
        free(newQueue->front);
        newQueue->front = NULL;
        newQueue->rare = NULL;
    }
    else{
        // otherwise change queue front
        node_t* temp = newQueue->front;      
        newQueue->front = newQueue->front->next;
        free(temp);
    }
    
    newQueue->size -= 1;

    return poppedNumber;
}

// clear all queue
void freeQueue(queue_t* newQueue){

    if(newQueue->size == 0){
        return;
    }
    node_t* current = newQueue->front;

    while(current->next != NULL){
        node_t* temp = current;
        current = current->next;
        free(temp);
    }
}



int main(){

    queue_t* newQueue = (queue_t*)malloc(sizeof(queue_t));

    if(newQueue == NULL){
        printf("Failure during new queue creation!");
        return 0;
    }

    newQueue->front = NULL;
    newQueue->rare = NULL;
    newQueue->size = 0;

    push(newQueue, 5);
    push(newQueue,6);
    printf("size: %zu\n",newQueue->size);
    printf("head: %d\n",newQueue->front->number);
    int poppedNumber = pop(newQueue);
    poppedNumber = pop(newQueue);
    printf("head: %p\n",newQueue->front);
    printf("popped: %d\n",poppedNumber);

    push(newQueue,6);
    freeQueue(newQueue);
    printf("head: %p\n",newQueue->front);

    return 0;
}