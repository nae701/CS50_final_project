// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define NUM_BUCKETS 125000

int count;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[NUM_BUCKETS];

/**
 * Thank you to Thomas Ballatore for posting this hash function on Discourse at
 * https://discourse.cs50.net/t/finding-a-new-hashing-function-online/12718/2
 *
 *
 * Hash function suggested by Alan Xie during section. A link is:
 *
 * https://github.com/hathix/cs50-section/blob/master/code/7/
 * sample-hash-functions/good-hash-function.c
 *
 * "A case-insensitive implementation of the djb2 hash function.
 * Change NUM_BUCKETS to whatever your number of buckets is.
 *
 * Adapted by Neel Mehta from
 * http://stackoverflow.com/questions/2571683/djb2-hash-function."
 */

unsigned int hash_word(const char* word)
{
    unsigned long hash = 5381;

    for (const char* ptr = word; *ptr != '\0'; ptr++)
    {
        hash = ((hash << 5) + hash) + tolower(*ptr);
    }

    return hash % NUM_BUCKETS;
}

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}


// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < NUM_BUCKETS; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));

        // Return error if no more memory
        if (!new_node)
        {
            unload();
            return false;
        }

        strcpy(new_node->word, word);

        new_node->next = hashtable[hash_word(new_node->word)];
        hashtable[hash_word(new_node->word)] = new_node;

        count++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Iterate through hashtable
    node *cursor = hashtable[hash_word(word)];
    while (cursor != NULL)
    {
        // Check length first in order to reduce time
        if(strlen(cursor->word) == strlen(word))
        {
            // Compare equal sized strings
            if (strcasecmp(cursor->word,word) == 0)
            {
                return true;
            }

        }
        cursor = cursor->next;
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Iterate through hashtable array
    for (int i = 0; i < NUM_BUCKETS; i++)
    {
        // Go through the linked list and free each node
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
