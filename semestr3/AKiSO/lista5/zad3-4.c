#define DELIM " \t\r\a"
#define PIPE_DELIM "|"
#define _GNU_SOURCE
#define PROMPT_COLOR "\033[36;1m"
#define COLOR "\033[33;0m"
#include <assert.h>
#include <fcntl.h>
#include <linux/limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <signal.h>
#include <unistd.h>
#include <stdbool.h>




enum Values{
	FLAG_NONE	= (1<<0),
	FLAG_FIRST	= (1<<1), // nie ma poprzednika
	FLAG_MIDDLE	= (1<<2), // ma i poprzednika i nastepnika
	FLAG_LAST	= (1<<3) // nie ma poprzednika
};

int count = 1;
char * directory;
int amp;
int sizeAwesome;
int commandNumAwesome;

void cd(char *dir) {
  if (chdir(dir) < 0) {
    perror("cd failed.");
  } else {
    directory = dir;
  }
}

void signal_handler(int n) {
  signal(n, signal_handler);
	// if signal is SIGCHLD, let's wait for it
	if (n==17) {
		waitpid(-1, NULL, WNOHANG);
	// ignore SIGINT
	} else if (n == 2) {
    printf("klikam ctrl c");
    }
}

int ampersand(char *string) {
  int i = 0;
  while(string[i] != NULL) {
    if (string[i]=='&') {
      if (string[i + 1] == NULL) {
        string[i] = NULL;
        return 1;
      }
    }
    i++;
  }
  return 0;
}

char** split(char *string, char *delim, int *num, size_t *sizeOfArray) {
  if (string == NULL) {
    return NULL;
  }
  char** result;
  int i = 0, j = 0;
  int len = 0;
  int maksLen = 0;
  int precount;
  count = 1;
  // counting number of tokens
  while(string[i] != '\0') {
    j = 0;
    precount = count;
    while(delim[j] != '\0') {
      if (string[i] == delim[j]) {
        count++;
      }
      j++;
    }

    if (precount == count) {
      len++;
      if (len > maksLen) {
        maksLen = len;
      }
    } else {
      len = 0;
    }
      
    i++;
  }
  int size = maksLen * count * sizeof(char*);
  *sizeOfArray = maksLen * count * sizeof(char*);;
  result = malloc(size);
  *num = count;

  // spliting into tokens
  if (result != NULL) {
    size_t idx = 0;
    char* token = strtok(string, delim);

    while (token != NULL) {
        result[idx] = token;
        token = strtok(0, delim);
        idx++;
    }
    result[idx] = NULL;
  }

  // dibadzer(result, maksLen);
  return result;
}

char*** splitPipes(char *string, int *num) {
  int size;
  size_t arraySize;
  char **pipedCommands = split(string, PIPE_DELIM, &size, &arraySize);
  *num = size;
  char *** result = malloc(arraySize * size);

  for (int i = 0; i < size; i++) {
    int s;
    size_t aS;
    result[i] = split(pipedCommands[i], DELIM, &s, &aS);
    amp = ampersand(result[i]);

  }
  
  return result;
}

void removeRedirects(char **words){

	int index=0;
	while(words[index]!=NULL){
		if(words[index][0]=='<' || words[index][0]=='>' || (words[index][0]=='2' && words[index][1]=='>')){
			words[index] = NULL;
			return;
		}
		index++;
	}
	
}

void execute(char *line) {
  int amp = ampersand(line);
  int size;
  char ***commands = splitPipes(line, &size);
  if (strcmp(commands[0][0], "cd") == 0) {
      printf("CD");
      cd(commands[0][1]);
      return;
  }
  else if(strcmp(commands[0][0], "exit") == 0){
    kill(0,9);
    exit(0);
  }
  pid_t child = fork();
  int status, wpid;
  if (child == 0) {
    int fd[size-1][2];
    
    for (int i = 0; i < size - 1; i++) {
      if (pipe(fd[i]) == -1) {
        perror("pipe error");
      }
    }

    int pids[size];
   

    //connect pipes
    for (int i = 0; i < size; i++) {
      if ((pids[i] = fork()) == 0) {
        int flag = 0;
        if (i == 0)
          flag |= FLAG_FIRST;
        if (i== size - 1)
          flag |= FLAG_LAST;
        //if (i > 0 && i < size - 1)
        //  flag |= FLAG_MIDDLE;

      	if(!(flag & FLAG_FIRST)){ // if not first
          if (dup2(fd[i-1][0], 0) == -1) {
                perror("dup2 error");
          }
        }

        if(!(flag & FLAG_LAST)) { // if not last
          if (dup2(fd[i][1], 1) == -1) {
            perror("dup2 error");
          }
        }

	      addRedirects(size, commands, i, flag);

        // we close all unused fds - important!
        for (int j = 0; j < size - 1; j++) {
          close(fd[j][0]);
          close(fd[j][1]);
        }
        
        //remove redirections from commands before executing them
        removeRedirects(commands[i]);
        // we execute the command - process is replaced by it and dies off eventually, freeing resources
        execvp(commands[i][0], commands[i]);
        // if we get to this part, execvp failed
        perror("execvp erroor");
        _exit(1);
      }
    }

    // close fds in parten
    for (int j = 0; j < size - 1; j++) {
      close(fd[j][0]);
      close(fd[j][1]);
    }
    
    // if we decided to wait, wait for all
    if(amp == 0) {
      for(int i = size - 1; i > -1; i--) {
        if(pids[i] > 0) {
          int status;
          waitpid(pids[i], &status, 0);
        }
      }
    }
    _exit(EXIT_SUCCESS);
  } else {
      if(amp == 0) {
          int wpid = waitpid(child, &status, 0);
      }
  }
}

void commandLoop() {
  int status = 1;
  int num;
  char *line = NULL;
  size_t len = 0;
  ssize_t nread;
  char directory[256];
  do { 
    printf("%slsh@%s> ", PROMPT_COLOR, getcwd(directory, sizeof(directory)));
    printf("%s", COLOR);
    nread = getline(&line, &len, stdin);

    if (strlen(line) == 1) {
      continue;
    }

    if (strlen(line) > 0 && line[strlen(line) - 1] == '\n') {
      line[strlen(line)-1] = '\0';
    }

    char tmpLine[len];
    strcpy(tmpLine, line);

    execute(tmpLine);
    
  } while (1);
}

int main() {
  signal(SIGCHLD, signal_handler);
	signal(SIGINT, signal_handler);
  commandLoop();
  return 0;
}

void addRedirects(int size, char*** commands, int index, int flag) {
	int commandLength = 0;
	while (commands[index][commandLength] != NULL) commandLength++;
	
	for(int j = 0; j < commandLength; j++) {
		if(commands[index][j][0] == '>' && (flag & FLAG_LAST)) { //jest koncem
		
			char path[PATH_MAX];
			for(int k = 1; k < strlen(commands[index][j]); k++) {
				path[k-1] = commands[index][j][k];
			}
			
			int file;
			if ((file = open(path, O_RDWR | O_CREAT | O_APPEND, 0777)) == -1) {
				perror("> error");
				_exit(1);
			}
			
			if (dup2(file, 1) == -1) {
				perror("dup2 error when tryging to redirect to file");
			}
						
			commands[index][j] = NULL;
							
		} else if (commands[index][j][0] == '2' && commands[index][j][1] == '>') { 
					
			char path[PATH_MAX];
			for(int k = 2; k < strlen(commands[index][j]); k++) {
				path[k-2] = commands[index][j][k];
			}
						
			int file;
			if ((file = open(path, O_RDWR | O_CREAT | O_APPEND, 0777)) == -1) {
				perror("2> error");
				_exit(1);
			}
			if (dup2(file, 2) == -1) {
				perror("dup2 error when tryging to redirect to file");
			}
					
			commands[index][j] = NULL;
			
		} else if (commands[index][j][0] == '<' && (flag & FLAG_FIRST)) { // jest poczatkiem
			
			char path[PATH_MAX];
			for(int k = 1; k < strlen(commands[index][j]); k++) {
				path[k-1] = commands[index][j][k];
			}
			
			int file;
			if ((file = open(path, O_RDWR | O_CREAT | O_APPEND, 0777)) == -1) {
				perror("> error");
				_exit(1);
			}
			
			if (dup2(file, 0) == -1) {
				perror("dup2 error when tryging to redirect to file");
			}
						
			commands[index][j] = NULL;

		}
	}
}
