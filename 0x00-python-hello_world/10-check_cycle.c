#include "lists.h"

/**
 * check_cycle - function that checks if a singly LL has a cycle in it.
 * @list: pointer of the start of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temporal;
	listint_t *checks;

	if (list == NULL || list->next == NULL)
		return (0);
	checks = list;
	temporal = list;

	while (checks != NULL && checks->next != NULL)
	{
		checks = checks->next->next;
		temporal = temporal->next;
		if (checks == temporal)
			return (1);
	}
	return (0);
}
