#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts node in a sorted list at correct place
 * @head: pointer to a pointer to the head
 * @number: number contained in new node
 * Return: Return address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	/*Declare vars*/
	listint_t *new;
	listint_t *current;
	/*malloc and check for fail*/
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	/*Null list edge case*/
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	/*Loop through entire list, checking for place to insert*/
	while (current->next != NULL)
	{
		/*edge case for num being less that first node*/
		if (current->n > number)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		/*loop until the node before the number is less than*/
		if (number <= current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	/*Final case, if number is greatest in the list*/
	new->next = NULL;
	current->next = new;
	return (new);
}
