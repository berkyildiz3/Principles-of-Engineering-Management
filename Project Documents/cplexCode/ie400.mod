/*********************************************
 * OPL 12.10.0.0 Model
 * Author: aatah
 * Creation Date: May 10, 2020 at 12:26:30 PM
 *********************************************/
 
 float temp;
 execute{
	var before = new Date();
	temp = before.getTime();
}

// Parameters
int nRange = ...;

range studyRange = 1..nRange;
range iRange = 1..nRange;
range jRange = 1..nRange;
range test = 2..nRange;

int y[studyRange] = ...;
int D[iRange][jRange] = ...;


// Decision Variables
dvar boolean X[iRange][jRange];
dvar int u[iRange];
 
// Decision expressions
dexpr int TotalDistance = (sum(i in iRange, j in jRange) X[i][j] * D[i][j] ) + sum(i in studyRange)y[i];

// Objective Function
minimize TotalDistance;
 
// Constraints
subject to{
	forall(i in iRange)
	  visitOnce1:
	  sum(j in jRange) X[i][j] == 1;  
	forall(j in jRange)
	  visitOnce2:
	  sum(i in iRange) X[i][j] == 1;  
	forall(i in iRange)
	  samePoint:
	  X[i][i] == 0; 	
	u[1] == 0;
	forall(i in test, j in test)
	    noCycle:   u[i]-u[j] + 1 <= (nRange+1)*(1-X[i][j]) ;    
}

execute{
	var after = new Date();
	writeln("solving time ~= ",after.getTime()-temp);
}