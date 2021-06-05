#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
int size=0,counter=0;
void** addresses;
int index__;

    struct node* newNode(int data)
    {
        struct node* node = (struct node*)malloc(sizeof(struct node));
        node->data = data;
        node->left = NULL;
        node->right = NULL;
        return(node);
    }
    void add_address(void* node){ /* add node address to array */
    	addresses[index__]=(void*)&node;
    	index__++;
    }


    void treeTravel(struct node* node) {
        if (node != NULL) {
            add_address((void*)&node);
            treeTravel(node->left);
            treeTravel(node->right);
        }
    }
    

    void findSize(struct node* node) {
        if (node != NULL) {
            findSize(node->left);
            size++;
            findSize(node->right);
        }
    }
    int anomaly_detection(){
        int i,j;
        for (i = 0; i < size; ++i)
        {
            for (j = i+1; j <size ; ++j)
            {
                if (addresses[i]==addresses[j])
                {
                    printf("I have found one duplicated link!!!\n");
                    return 1;
                }
            }
        }
        return 0; 
    }
    void deleteTree(struct node* node) 
    {
        if (node == NULL){
            return;
        }
        deleteTree(node->left);
        deleteTree(node->right);
        free(node);
    } 
  
int main()
{
	int i;
	struct node *root;
    root = newNode(40);
    root->left        = root;
    root->right       = newNode(80);
    root->left->left  = newNode(10);
    root->left->right = newNode(30);
    root->right->right = newNode(100);
    root->right->right->right = newNode(90);
    index__=0;

   	findSize(root);
    addresses=(void**)malloc(sizeof(void*)*size);
    for (i = 0; i < size; ++i)
    {
    	addresses[i]=NULL;
    }
    treeTravel(root);
    anomaly_detection();
    free(addresses);
    deleteTree(root);
	return 0;
}
