#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>


typedef struct node{
    int number;
    struct node* next;
    struct node* previous;
}node_t;

typedef struct list{
    node_t* head;
    size_t size;
}list_t;


void pushToRare(list_t* newList, int newNumber){

    node_t* newNode = (node_t*)malloc(sizeof(node_t));

    if(newNode == NULL){
        printf("Failure during new node creation!");
        return;
    }
    newNode->number = newNumber;
    newNode->next = NULL;
    newNode->previous = NULL;

    if(newList->head == NULL){
        newList->head = newNode;
        newNode->next = newNode;
        newNode->previous = newNode;
    }
    else{
        node_t* current = newList->head;

        while(current->next != newList->head){
            current = current->next;
        }

        current->next = newNode;
        newNode->previous = current;
        newNode->next = newList->head;
        newList->head->previous = newNode;
    }


    newList->size += 1;

    return;
}


void pushToHead(list_t* newList, int newNumber){

    node_t* newNode = (node_t*)malloc(sizeof(node_t));

    if(newNode == NULL){
        printf("Failure during new node creation!");
        return;
    }

    newNode->number = newNumber;

    if(newList->head == NULL){
        newNode->next = newNode;
        newNode->previous = newNode;
        newList->head = newNode;
    }
    else{
        newNode->next = newList->head;
        newNode->previous = newList->head->previous;
        newList->head->previous->next = newNode;
        newList->head->previous = newNode;
        newList->head = newNode;
    }

    newList->size += 1;

    return;
}

void pop(list_t* newList, int  removedNumber){

    node_t* current = (node_t*)malloc(sizeof(node_t));

    if(newList->head == NULL){
        printf("List is empty!");
        return;
    }

    current = newList->head;

    // remove head of list
    while(newList-> size != 0 && current->number == removedNumber){
         node_t* temp = (node_t*)malloc(sizeof(node_t));
         temp = current;

         newList->head = current->next;
         newList->head->previous = current->previous;
         newList->head->previous->next = newList->head;
         current = current->next;

         free(temp);     
    }
    // remove other element than head
    while(current->next != newList->head){
        
        if(current->next->number == removedNumber){
            node_t* temp = (node_t*)malloc(sizeof(node_t));
            temp = current->next;

            current->next = current->next->next;
            current->next->previous = current;
            
            free(temp);
        }
        current = current->next;
    }
}

void freeList(list_t* newList){
    
    if(newList->head == NULL){
        printf("Lista była pusta!");
        return;
    }

    node_t* current = (node_t*)malloc(sizeof(node_t));
    current = newList->head->next;

    while(current != newList->head){

        node_t* temp = (node_t*)malloc(sizeof(node_t));
        temp = current;
        current = current->next;
        free(temp);
    }

    free(current);
}

void fillList(list_t* newList){
    for(int i = 1; i<=10; i++){
        pushToRare(newList, i);
    }
}

void megre(list_t* l1, list_t* l2){

    node_t* tail1 = (node_t*)malloc(sizeof(node_t));
    node_t* tail2 = (node_t*)malloc(sizeof(node_t));
    

     if(l1->head == NULL || l2->head == NULL){
         printf("Provide non null lists!");
         return;
     }

    tail1 = l1->head->previous;
    tail2 = l2->head->previous;

    // set tail1 next to l2 head and l2 head previous to tail1
    tail1->next = l2->head;
    l2->head->previous = tail1;
    // set tail2 next to l1 head and l1 head previous to tail2
    tail2->next = l1->head;
    l1->head->previous = tail2;
    l1->size = l1->size+ l2->size;
    return;
}

float elementTime(list_t* newList, int specifiedElem){

    if(newList->head == NULL){
        printf("Head is null!");
        return 0;
    }

    node_t* current = (node_t*)malloc(sizeof(node_t));
    current = newList->head;

    clock_t start = clock();
    // iterate through list to find specified elem
    while(current->number != specifiedElem && current->next != NULL){
        current = current->next;
    }

    clock_t stop = clock();

    return (float)(stop - start) / CLOCKS_PER_SEC;
}

void display(list_t* l){
    if( l->head == NULL){
        return;
    }
    node_t* current = (node_t*)malloc(sizeof(node_t));
    current = l->head;
    printf("%d ",current->number);
    while(current->next != l->head){
        current = current->next;
        printf("%d ", current->number);
    }

    printf("\n");
    return;
}

int main(){

    list_t* newList = (list_t*)malloc(sizeof(list_t));
    list_t* newList2 = (list_t*)malloc(sizeof(list_t));

    if(newList == NULL || newList2 == NULL){
        printf("Failure during new list creation!");
        return 0;
    }
    
    newList->head = NULL;
    newList->size = 0;
    newList2->head = NULL;
    newList2-> size = 0;
    //                                                                          TESTING MEGRE FUNCTION
    fillList(newList);
    fillList(newList2);
    pushToRare(newList2, 15);
    pushToRare(newList, 17);
    printf("size of newList before megre: %ld \n", newList->size);
    printf("size of newList2 before megre: %ld \n", newList2->size);
    printf("tail of newList before megre: %d\n", newList->head->previous->number);
    printf("tail of newList2 before megre: %d\n", newList2->head->previous->number);
    megre(newList, newList2);
   // newList has tail of newList2 after megre 
    printf("tail of newList after megre with newList2: %d\n", newList->head->previous->number);
    printf("size of newList after megre: %ld\n", newList->size);



    //                                                                          TESTING TIME MEASURMENT FUNCTIONS


    newList = (list_t*)malloc(sizeof(list_t));
    newList2 = (list_t*)malloc(sizeof(list_t));
    newList->head = NULL;
    newList->size = 0;
    newList2->head = NULL;
    newList2-> size = 0;
    bool randomNumArray[5000];
    for(int i = 0; i < 5000;i++){
        randomNumArray[i] = false;
    }
    for(int i = 0; i < 1000; i++){
        int randNum = rand()%5000;
        while(randomNumArray[randNum] == true){
            randNum = rand()%5000;
        }
        randomNumArray[randNum] = true;
        pushToRare(newList, randNum);
    }

     float specifiedTime = 0;
     float randomTime = 0;

     int specifiedNum = rand()%5000;
     while(randomNumArray[specifiedNum] != true){
         specifiedNum = rand()%5000;
     }

     printf("Specified: %d\n", specifiedNum);

     int randomNum;

    for(int i = 0; i<100000; i++){
        randomNum = rand()%5000;
        specifiedTime += elementTime(newList, specifiedNum);
        while(randomNumArray[randomNum] != true){
         randomNum = rand()%5000;
        }
        randomTime += elementTime(newList, randomNum);
        
    }

    printf("Specified time: %f\n", specifiedTime);
        printf("Random time: %f\n", randomTime);

    freeList(newList);

    return 0;
}