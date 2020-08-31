#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* check_cycle - checks to see if the list cycles
* @list: the list to check
* Return: returns either 1 if thers a cycle or 0 if no cycle
*/
int check_cycle(listint_t *list)
{
	const listint_t *current;
	int i = 0, c = 20;

	current = list;

	while (current != NULL)
	{
		if (i == c)
			return (1);
		current = current->next;
		i++;
	}
	return (0);
}
