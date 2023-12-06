#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * findlength - finds the length of linked list
 * @head: head of linked list
 * Return: length
 */
int findlength(listint_t *head)
{
	listint_t *curr = head;
	int cnt = 0;

	while (curr != NULL)
	{
		cnt++;
		curr = curr->next;
	}
	return (cnt);
}
/**
 * convertArr - converts a linked list to arr
 * @head: head of the linked list
 * @len: the lenght of the linked list
 * Return: array
 */
int *convertArr(listint_t *head, int len)
{
	int *arr = (int *) malloc(len * sizeof(int));
	int index = 0;
	listint_t *curr = head;

	while (curr != NULL)
	{
		arr[index++] = curr->n;
		curr = curr->next;
	}
	return (arr);
}
/**
 * is_palindrome - checks if a linkedlist is a palindrome
 * @head: a pointer to head of linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len, *arr, i, flag = 1;

	if (head == NULL)
		return (0);
	len = findlength(*head);
	if (len == 0)
		return (1);
	arr = convertArr(*head, len);
	for (i = 0; i <= (len / 2); i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			flag = 0;
			break;
		}
	}
	free(arr);
	return (flag);
}
