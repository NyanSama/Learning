#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<string.h>

int main(){

	int filedes[2];
	int result = -1;
	pid_t pid[2];

	result = pipe(filedes);
	if(result == -1)
	  {
	     printf("Pipe Error!\n");
	     return -1;
	  }
	pid[0] = fork();
	if(-1 == pid[0])
	{
	   printf("Fork Error!\n");
	   return -1;
	}
        if(!pid[0])
	{
	  printf("Child1 begin\n");
	  close(filedes[0]);                  //close read
	  if(dup2(filedes[1],STDOUT_FILENO) < 0){
		perror("dup2 error");
		return -1;
		}     //exchange output  
	  execlp("/bin/ls","ls","-l","/etc",(char *)0);
	  exit(0);
	 // fprintf(1,"Child1 finish\n");
	  
	}
	if(pid[0])
	{
	   printf("Parent1 begin pid=%d\n",pid[0]);

	   pid[1] = fork();
	   if(!pid[1])
	   {
	     printf("Child2 begin\n");
    	     close(filedes[1]);                  //close write	  
	     if(dup2(filedes[0],STDIN_FILENO) < 0){
		perror("dup2 Fail!");
		return -1;
		}     //exchange input 
	     //dup(STDOUT_FILENO); 
	     execlp("/bin/more","more",(char *)0);
	     //system("more");
	     //sleep(10);
	     //printf("Child2 finish\n");
	     //exit(0);
	     //dup(STDIN_FILENO);
	   }
	   waitpid(pid[0],NULL,0);
	  // printf("%d Finish\n",pid[0]);
	   waitpid(pid[1],NULL,0);
	  // printf("%d Finish\n",pid[1]);
	}
	
}
