#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for Holberton School students.
 * @head: list to be scanned for palindrome
 * Return: 0 if palindrome and 1 if not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = *head;
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	tmp2 = copyll(tmp1);
	while (tmp1 != NULL)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	return (1);
}
/**
 * copyll - copy linked list
 * @ll: list to be scanned for palindrome
 * Return: a new malloced list
 */
listint_t *copyll(listint_t *ll)
{
	listint_t *current;
	listint_t *new_list;
	listint_t *stash;

	current = ll;
	new_list = malloc(sizeof(listint_t));
	if(new_list == NULL)
		return (NULL);
	new_list->n = current->n;
	new_list->next = NULL;
	current = current->next;
	while (current != NULL)
	{
		stash = new_list;
		new_list = malloc(sizeof(listint_t));
		if (new_list == NULL)
			return (NULL);
		new_list->n = current->n;
		new_list->next = stash;
		current = current->next;
	}
	return (new_list);
}
