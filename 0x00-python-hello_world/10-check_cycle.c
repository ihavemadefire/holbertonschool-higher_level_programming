#include <stdlib.h>
#include "lists.h"

/*
 *check_cycle - checks to see is a LL has a loop in it
 *@list: the LL to be scanned
 *Return: Returns 1 if found, and 0 if there is no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	/*check for NULL or LL with length 1*/
	if (list == NULL || list->next == NULL)
		return (0);
        /*initial assignment*/
	tortoise = list->next;
	hare = list->next->next;
	/*loop until match or list is done*/
	while (tortoise && hare && hare->next)
	{
		/*if there is a match, there is a loop*/
		if (tortoise == hare)
			return(1);
		/*advance the animals*/
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	/*not loop was found return 0*/
	return(0);
}
