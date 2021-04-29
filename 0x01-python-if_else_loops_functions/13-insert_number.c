#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts new node to a sorted linked list
 * @head: head of linked list
 * @number: value in linked list->n
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;/*temporal de adelante */
	listint_t *tmp_prev;/*temporal de adelante */

	/*Creating the new node and inicia initializing */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	tmp_prev = *head;
	if (tmp_prev == NULL || tmp_prev->n >= new->n)
	{
		new->next = tmp_prev;
		*head = new;
		return (new);
	}
	tmp = tmp_prev->next;
	/*Al salir del while se hace la insercion del nuevo nodo*/
	while (tmp_prev != NULL && tmp_prev->next != NULL && new->n >= tmp->n)
	{
		tmp_prev = tmp_prev->next;
		tmp = tmp_prev->next;
	}
	/* Aqui se introduce el nuevo nodo debido a que se encontró un*/
	/*numero menor que otro o porque llegó al final y se agregará al final*/
	tmp_prev->next = new;
	new->next = tmp;
	return (new);
}
