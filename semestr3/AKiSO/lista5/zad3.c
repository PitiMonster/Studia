#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// executing chdir
int lsh_cd(char **args)
{
  if (args[1] == NULL) {
    fprintf(stderr, "lsh: expected argument to \"cd\"\n");
  } else {
    if (chdir(args[1]) != 0) {
      perror("lsh");
    }
  }
  return 1;
}

// checking whether '&' is last element of input
int ampersand(char *args[]) {
  int i = 0;
  while(args[i] != NULL) {
    if (strcmp(args[i],"&") == 0) {
      if (args[i + 1] == NULL) {
        args[i] = NULL;
        return 1;
      }
    }
    i++;
  }
  return 0;
}

int lsh_launch(char **args)
{
  pid_t pid, wpid;
  int status;
  int amp = ampersand(args);
	// & is getting nulled when it is last element of input
	if(amp == 1){
		args[sizeof(args)/sizeof(args[0])-1] = NULL;
	}
  pid = fork(); // creating child to execute a command process on it
  if (pid == 0) {
    // Child process
    if (execvp(args[0], args) == -1) {
      perror("lsh");
    }
    exit(EXIT_FAILURE);
  } else if (pid < 0) {
    // Error forking
    perror("lsh");
  } else {
  		if(amp == 0){
			// Parent is waiting until child state change
			do {
			  wpid = waitpid(pid, &status, WUNTRACED);
			} while (!WIFEXITED(status) && !WIFSIGNALED(status));
		}
  }

  return 1;
}


int lsh_execute(char **args)
{
  int i;
  // checking whether command is not "cd"
  if (args[0] != NULL){
		if(strcmp(args[0], "cd") == 0){
			lsh_cd(args);
		}
		else{
			return lsh_launch(args);
				}
	}
  else{
	return 0;	
	}
}


//define bufsize and delimiters for strtok function
#define LSH_TOK_BUFSIZE 64
#define LSH_TOK_DELIM " \t\r\n\a"
// creating array of words
char **lsh_split_line(char *line)
{
  int bufsize = LSH_TOK_BUFSIZE, position = 0;
  char **tokens = malloc(bufsize * sizeof(char*));
  char *token;

  if (!tokens) {
    fprintf(stderr, "lsh: allocation error\n");
    exit(EXIT_FAILURE);
  }
	// merging chars into strings delimited by delimiters
  token = strtok(line, LSH_TOK_DELIM);
  while (token != NULL) {
    tokens[position] = token;
	if(position == 0)
		if(strcmp(token, "exit") == 0)
			exit(0);
    position++;
		// increasing bufsize if it is too small
    if (position >= bufsize) {
      bufsize += LSH_TOK_BUFSIZE;
      tokens = realloc(tokens, bufsize * sizeof(char*));
      if (!tokens) {
        fprintf(stderr, "lsh: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }

    token = strtok(NULL, LSH_TOK_DELIM);
  }
  tokens[position] = NULL;
  return tokens;
}


// reading line from stdin
char *lsh_read_line(void)
{
  char *line = NULL;
  ssize_t bufsize = 0; // have getline allocate a buffer for us
  getline(&line, &bufsize, stdin); // stdin read standard input
  return line;
}

// step by step command executing
void lsh_loop(void)
{
  char *line;
  char **args;
  int status;

  do {
    printf("> ");
    line = lsh_read_line();
    args = lsh_split_line(line);
    status = lsh_execute(args);

    free(line);
    free(args);
  } while (status);
}


// Running command loop.
int main(char **argv)
{

  lsh_loop();

  return EXIT_SUCCESS;
}

