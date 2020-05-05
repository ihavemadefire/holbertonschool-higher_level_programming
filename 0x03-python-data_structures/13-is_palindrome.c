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
	if (tmp1->next == NULL)
		return (1);
	tmp2 = rev_list(tmp1);
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
 * rev_list - reverses a passed linked list
 * @ll: pointer to list to be reversed
 * Return: pointer to reversed list.
 */
listint_t *rev_list(listint_t *ll)
{
	listint_t *tmp1 = ll;
	listint_t *tmp2 = NULL;
	listint_t *revlist = NULL;

	while (tmp1 != NULL)
	{
		tmp2 = tmp1->next;
		tmp1->next = revlist;
		revlist = tmp1;
		tmp1 = tmp2;
	}
	return (revlist);
}
