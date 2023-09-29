#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - fiven function.
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main entrydisplays Zombie process created,
 * PID: ZOMBIE_PID.
 * Return: 0.
 */
int main(void)
{
	int pid, i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}
