// Code by SoundOfSpouting#6980 (UID: 151149148639330304)
// Usage: interpreter.exe [input file] [program file]

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int debug = 0;

int randInt (int m, int M) {
	return 4; // stub
}
void doBetter () {
	puts ("Please Just Do Better");
	exit (randInt (1, 69420));
}

void printList (int* list, int length) {
	printf ("[");
	for (int i = 0; i < length - 1; i++) printf("%d, ", list[i]);
	if (length < 1) puts ("]");
	else printf ("%d]\n", list[length - 1]);
}
void printDisks (int** disks, int* tops, int pegs) {
	puts ("{");
	for (int i = 0; i < pegs; i++) {
		printf ("    %d ", i);
		printList (disks[i], tops[i] + 1);
	}
	puts ("}");
}

int listToDisks (const int* list, const int length, int*** _disks, int** _tops) {
	int pegs = 2;
	for (int i = 0; i < length - 1; i++) if (list[i] > list[i + 1]) pegs++;

	int** disks = (int**) malloc (pegs * sizeof (int*));
	int* tops = (int*) malloc (pegs * sizeof (int));
	for (int i = 0; i < pegs; i++) {
		tops[i] = -1;

		disks[i] = (int*) malloc (length * sizeof (int));
		for (int j = 0; j < length; j++) disks[i][j] = -1; // Not necessary
	}

	int i = pegs - 2, j = 0;
	for (int k = length - 1; k > 0; k--) {
		disks[i][j] = list[k];
		if (list[k-1] > list[k]) {
			tops[i] = j;
			i--;
			j = 0;
		} else j++;
	}
	disks[i][j] = list[0];
	tops[i] = j;

	*_disks = disks;
	*_tops = tops;
	return pegs;
}
void disksToList (int* list, int** disks, const int* tops, const int pegs) {	
	for (int j = 0; j < pegs; j++) for (int k = tops[j]; k >= 0; k--) (list++)[0] = disks[j][k];
}
int move (int** disks, int* tops, const int pegs, const int length, int i, int j) {
	i = i % pegs;
	j = j % pegs;

	if (i == j || tops[i] < 0 || tops[j] > length - 2 || tops[j] > -1 && (disks[i][tops[i]] > disks[j][tops[j]])) return 0;

	tops[j]++;
	disks[j][tops[j]] = disks[i][tops[i]];
	disks[i][tops[i]] = -1; // Not necessary
	tops[i]--;

	return 1;
}

int loadBytes (char* file, int** _list) {
	FILE* fp = fopen (file, "rb");
	if (fp == NULL) doBetter ();

	fseek (fp, 0, SEEK_END);
	const int length = ftell (fp);
	fseek (fp, 0, SEEK_SET);

	int* list = (int*) malloc (length * sizeof (int));
	for (int i = 0; i < length; i++) list[i] = fgetc (fp);
	fclose (fp);

	*_list = list;
	return length;
}

void execute (int* list, int length, int* program, int programLength) {
	if (debug > 5) printList (list, length);

	int** disks;
	int* tops;
	const int pegs = listToDisks (list, length, &disks, &tops);

	if (debug > 6) printDisks(disks, tops, pegs);

	for (int i = 0; i < programLength - 1; i += 2) {
		int s = move (disks, tops, pegs, length, program[i], program[i+1]);
		if (debug > 7) {
			printf ("(%d, %d)%s\n", program[i], program[i+1], s ? "" : " invalid");
			if (s) printDisks (disks, tops, pegs);
		}
	}

	disksToList (list, disks, tops, pegs);

	for (int i = 0; i < pegs; i++) free (disks[i]);
	free (disks);
	free (tops);
}
int isSorted (int* list, int length) {
	int sorted = 1;
	for (int i = 0; i < length - 1; i++) if (list[i] > list[i+1]) {
		sorted = 0;
		break;
	}
	return sorted;
}
void sort (int* list, int length) {
	for (int i = 0; i < length; i++) for (int j = 0; j < length; j++) if (list[i] < list[j]) {
		int x = list[i];
		list[i] = list[j];
		list[j] = x;
	}
}

int* tests[] = {
	(int[]) {},
	(int[]) {172},
	(int[]) {203, 35},
	(int[]) {18, 13, 94},
	(int[]) {193, 46, 26, 129},
	(int[]) {77, 108, 182, 111, 242},
	(int[]) {88, 159, 106, 233, 87, 30},
	(int[]) {151, 106, 165, 236, 180, 249, 113},
	(int[]) {117, 238, 17, 93, 165, 76, 166, 15},
	(int[]) {115, 7, 181, 141, 13, 205, 86, 231, 135},
	(int[]) {118, 23, 77, 47, 177, 48, 15, 111, 25, 75},
	(int[]) {106, 220, 114, 44, 57, 117, 169, 56, 198, 109, 165},
	(int[]) {30, 15, 164, 86, 18, 200, 93, 145, 224, 249, 134, 160},
	(int[]) {167, 230, 10, 83, 226, 93, 97, 218, 98, 51, 115, 236, 94},
	(int[]) {248, 106, 26, 120, 32, 72, 218, 78, 178, 37, 76, 15, 137, 218},
	(int[]) {214, 158, 209, 243, 75, 148, 216, 195, 223, 137, 169, 90, 142, 109, 1}
};
void TRAILS (int* list, int length, int** subprograms, int* subprogramsLengthJ, int subprogramsLengthI) {
	const int requiredComplete = 3;

	int** cases[] = {
		(int*[]) { (int[]) {2,3,0,1}, (int[]) {1,3,0,2}, (int[]) {1,2,0,3}, (int[]) {0,3,1,2}, (int[]) {0,2,1,3} },
		(int*[]) { (int[]) {0,0,1,0,0}, (int[]) {0,1,0,1,0}, (int[]) {0,1,1,1,0}, (int[]) {0,1,2,1,0}, (int[]) {0,2,1,2,0}, (int[]) {1,0,0,0,1}, (int[]) {1,0,1,0,1}, (int[]) {1,0,2,0,1}, (int[]) {1,1,0,1,1}, (int[]) {1,2,0,2,1}, (int[]) {2,0,1,0,2}, (int[]) {2,1,0,1,2} },
		(int*[]) { (int[]) {} }
	};
	int* casesLengthK[] = {
		(int[]) {4,4,4,4,4}, (int[]) {5,5,5,5,5,5,5,5,5,5,5,5}, (int[]) {0}
	};
	int casesLengthJ[] = {5,12,1};
	int casesLengthI = 3;

	int randCase = randInt (0, 14);
	cases[2][0] = tests[randCase];
	casesLengthK[2][0] = randCase;
	
	int complete = 0;
	for (int i = 0; i < casesLengthI && i < subprogramsLengthI; i++) {
		if (debug > 4) printf ("TRAIL %d Begins\n", i);
		int flag = 1;
		for (int j = 0; j < casesLengthJ[i]; j++) {
			for (int k = i; k >= 0; k-=2) execute (cases[i][j], casesLengthK[i][j], subprograms[i], subprogramsLengthJ[i]);
			for (int k = i; k >= 0; k-=2) {
				if (debug > 5) {
					printf(" :: ");
					printList (cases[i][j], casesLengthK[i][j]);
				} if (!isSorted (cases[i][j], casesLengthK[i][j])) {
					if (debug > 4) printf ("You Have Failed TRAIL %d\n", i);
					flag = 0;
					break;
				}
			}
			if (flag == 0) break;
			if (i > 1) {
				execute (subprograms[i], subprogramsLengthJ[i], subprograms[i], subprogramsLengthJ[i]);
				if (debug > 5) {
					printf(" :: ");
					printList (subprograms[i], subprogramsLengthJ[i]);
				} if (!isSorted (subprograms[i], subprogramsLengthJ[i])) {
					if (debug > 4) printf ("You Have Failed TRAIL %d\n", i);
					flag = 0;
					break;
				}
			}
			if (flag == 0) break;
		}
		if (flag) {
			if (debug > 4) printf ("You Have Passed TRAIL %d\n", i);
			complete++;
		}
	}
	if (debug > 4) for (int i = subprogramsLengthI; i < casesLengthI; i++) printf ("You Have Failed TRAIL %d By Default\n", i);

	if (complete >= requiredComplete) {
		if (debug > 4) puts ("You Have Completed The TRAILS\nThe Input Will Now Be Sorted");
		sort (list, length);
	} else if (debug > 4) printf ("You Have Not Completed Enough TRAILS\nPlease Complete %d More TRAILS", requiredComplete - complete);
	return;
}
int main (int argc, char** argv) {
	if (argc != 3) doBetter ();

	int* list;
	const int length = loadBytes (argv[1], &list);

	int* program;
	const int programLength = loadBytes (argv[2], &program);

	if (programLength > 100) doBetter ();

	if (program[0] == 255) {
		if (debug > 5) printList (list, length);
		if (debug > 4) puts ("TRAILS MODE ENGAGED");

		int subprogramsLengthI = 0;
		for (int i = 0; i < programLength; i++) if (program[i] == 255) subprogramsLengthI++;

		int** subprograms = (int**) malloc (subprogramsLengthI * sizeof (int*));
		int* subprogramsLengthJ = (int*) malloc (subprogramsLengthI * sizeof (int));
		
		int j = programLength - 1, k = subprogramsLengthI - 1;
		for (int i = j; i >= 0; i--) if (program[i] == 255) {
			subprograms[k] = program + i + 1;
			subprogramsLengthJ[k] = (j - i);
			k--;
			j = i - 1;
		}
		
		TRAILS (list, length, subprograms, subprogramsLengthJ, subprogramsLengthI);

		free (subprograms);
		free (subprogramsLengthJ);
	} else execute (list, length, program, programLength);

	printList (list, length);

	int notSorted = 1 - isSorted (list, length);
	if (notSorted && debug > 5) {
		puts ("Not Sorted!");
		if (debug > 8) {
			sort (list, length);
			printList (list, length);
		}
	}

	free (list);
	free (program);
	return notSorted;
}
