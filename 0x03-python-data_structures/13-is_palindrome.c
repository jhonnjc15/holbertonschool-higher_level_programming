#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly LL is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int counter = 0, i, j, k;

	if (tmp == NULL)
		return (1);
	while (tmp != NULL)
		tmp = tmp->next, counter = counter + 1;

	int array1[counter], array2[counter];

	tmp = *head;
	for	(i = 0; i < counter ; i++)
	{
		array1[i] = tmp->n;
		tmp = tmp->next;
	}
	for (j = 0 ; j < counter ; j++)
	{
		array2[j] = array1[counter - j - 1];
	}
	for (k = 0 ; k < counter ; k++)
	{
		if (array1[k] != array2[k])
			return (0);
	}
	return (1);
}
