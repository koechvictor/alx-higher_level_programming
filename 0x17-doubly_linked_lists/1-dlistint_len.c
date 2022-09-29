#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 *@h: doubly linked list node
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	for (; h; h = h->next; size++)
		;
	return (size);
}
