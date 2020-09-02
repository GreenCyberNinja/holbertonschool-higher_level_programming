#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* insert_node - inserts node in sorted list
* @head: list to be modded
* @number: number to be added to list
* Return: null or updated list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *ans;

	tmp = *head;
	ans = malloc(sizeof(listint_t));

	if (ans == NULL)
		return (NULL);
	while (tmp != NULL)
	{
		if (tmp->n < number)
		{
			ans->n = number;
			ans->next = tmp->next;
			tmp->next = ans;
			return (ans);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
