#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>


typedef struct node{
    int number;
    struct node* next;
}node_t;

typedef struct list{
    node_t* head;
}list_t;

void pushToRare(list_t* newList, int newNumber){

    node_t* newNode = (node_t*)malloc(sizeof(node_t));

    if(newNode == NULL){
        printf("Failure during new node creation!");
        return;
    }

    newNode->number = newNumber;
    newNode->next = NULL;

    if(newList->head == NULL){
        newList->head = newNode;
    }
    else{
        node_t* current = newList->head;

        while(current->next != NULL){
            current = current->next;
        }

        current->next = newNode;
    }
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
        newNode->next = NULL;
        newList->head = newNode;
    }
    else{
        newNode->next = newList->head;
        newList->head = newNode;
    }

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
    while(current != NULL && current->number == removedNumber){
         node_t* temp = (node_t*)malloc(sizeof(node_t));
         temp = current;

         newList->head = current->next;
         current = current->next;

         free(temp);     
    }

    while(current != NULL && current->next != NULL){
        if(current->next->number == removedNumber){
            node_t* temp = (node_t*)malloc(sizeof(node_t));
            temp = current->next;

            // remove last element of list
            if(current->next->next == NULL){
                current->next = NULL;
            }
            else{
                // remove middle element of list
                current->next = current->next->next;
            }
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
    current = newList->head;

    while(current->next != NULL){

        node_t* temp = (node_t*)malloc(sizeof(node_t));
        temp = current;
        current = current->next;
        free(temp);
    }

    free(current);
}

void fillList(list_t* newList){
    for(int i = 1; i<=1000; i++){
        pushToRare(newList, i);
    }
}
// measure time with clock_t
float specifiedElementTime(list_t* newList, int specifiedElem){

    if(newList->head == NULL){
        printf("Head is null!");
        return 0;
    }

    node_t* current = (node_t*)malloc(sizeof(node_t));
    current = newList->head;

    clock_t start = clock();

    while(current->number != specifiedElem && current->next != NULL){
        current = current->next;
    }

    clock_t stop = clock();

    return (float)(stop - start) / CLOCKS_PER_SEC;
}


void megre(list_t* l1, list_t* l2){
     
     node_t* tail= (node_t*)malloc(sizeof(node_t));
    // check whether non of lists are empty
     if(l1->head == NULL || l2->head == NULL){
         printf("Provide non null lists!");
         return;
     }

    tail = l1->head;
    // looking for tail of l1
    while(tail->next != NULL){
        tail = tail->next;
    }

    tail->next = l2->head;

    return;
}

void display(list_t* l){
    if( l->head == NULL){
        return;
    }
    node_t* current = (node_t*)malloc(sizeof(node_t));
    current = l->head;
    printf("%d ",current->number);
    while(current->next != NULL){
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
    //                                                                          TESTING MEGRE FUNCTION
    printf("Testing megre function\n");
    newList->head = NULL;
    newList2->head = NULL;

    pushToHead(newList, 5);
    pushToHead(newList,4);
    pushToHead(newList2,2);
    pushToHead(newList2,1);
    printf("Lists before megre:\n");
    display(newList);
    display(newList2);

    megre(newList, newList2);


    printf("List after megre:\n");
    display(newList);
    
                     //                                              TESTING PUSH AND POP FUNCTIONS
    
    newList = (list_t*)malloc(sizeof(list_t));
    newList2 = (list_t*)malloc(sizeof(list_t));
    printf("c");
    printf("Testing push and pop functions\n");
    newList->head = NULL;
    newList2->head = NULL;
    pushToHead(newList, 5);
    pushToRare(newList, 5);
    pushToRare(newList, 4);
    printf("Head: %d\n", newList->head->number);
    pop(newList, 5);
    printf("Head: %d\n", newList->head->number);

    freeList(newList);
    printf("Head: %d\n", newList->head->number);


    //                                                                          TESTING TIME MEASURMENT FUNCTIONS
    
    newList = (list_t*)malloc(sizeof(list_t));
    newList2 = (list_t*)malloc(sizeof(list_t));

    newList->head = NULL;
    newList2->head = NULL;

    bool randomNumArray[5000];

    // set all values of randomNumArray to false
    for(int i = 0; i < 5000;i++){
        randomNumArray[i] = false;
    }
    // select 1000 random numbers out of 5000 
    for(int i = 0; i < 1000; i++){
        int randNum = rand()%5000;
        while(randomNumArray[randNum] == true){
            randNum = rand()%5000;
        }
        randomNumArray[randNum] = true;
        pushToRare(newList, randNum);
    }
    // fillList(newList);

     float specifiedTime = 0;
     float randomTime = 0;
    // select one specified number
     int specifiedNum = rand()%5000;
     while(randomNumArray[specifiedNum] != true){
         specifiedNum = rand()%5000;
     }

     printf("Specified: %d\n", specifiedNum);

     int randomNum;
    // measure time of 100000 searches
    for(int i = 0; i<100000; i++){
        randomNum = rand()%5000;
        specifiedTime += specifiedElementTime(newList, specifiedNum);
        while(randomNumArray[randomNum] != true){
         randomNum = rand()%5000;
        }
        randomTime += specifiedElementTime(newList, randomNum);
        
    }

    printf("Specified time: %f\n", specifiedTime);
        printf("Random time: %f\n", randomTime);

    freeList(newList);

    return 0;
}