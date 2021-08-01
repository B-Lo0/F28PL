% Coursework template

% Nabeel Alkindy, H00287325       <--- so we know who you are
% F28PL Coursework 3, Prolog    <--- sanity check

% Due: 11th December 2020
% Submit (this file) via GitLab as usual.
% You may assume variables, procedures, and functions defined in
% earlier questions in your answers to later questions, though you
% should add comments in code explaining this if any clarification
% might help read your code.

% For all questions, include testing in comments, so your marker can
% load this file as a database then cut-and-paste any testing into the
% command line.

% Testing on GitLab will NOT be provided for Prolog. Your own test
% will in this case be marked - note this is unlike the Python and
% OCaml coursework.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 1   <--- Yes, so we know what question you think you're answering

% The complex numbers are explained here (and elsewhere):
%   http://www.mathsisfun.com/algebra/complex-number-multiply.html
%
% Represent a complex integer as a two-element list of integers, so
% [4,5] represents 4+5i.  Write Prolog predicates
%
%   cadd/3
%   cmult/3
%
% representing complex integer addition and multiplication. Thus for
% instance, cadd([X1,X2],[Y1,Y2],[Z1,Z2]) succeeds if and only if
% Z1=X1+Y1 and Z2=X2+Y2. Note that complex number multiplication is
% not just like complex number addition. Check the link and read the
% definition.

    cadd([X1,X2], [Y1,Y2], [Z1, Z2]):-      % This represents the complex addition formula and bind the value of X1+Y1 to Z1 and binds X2+Y2 to Z2
    Z1 is X1 + Y1, Z2 is X2 + Y2.           % The asnwer represents the form (__ + __i) with Z1 and Z2 respectively.

%% ?- cadd([1, 5], [9, 3], [Z1, Z2]). Tester Code
%% Z1 = 10,
%% Z2 = 8.

    cmult([X1,X2], [Y1,Y2], [Z1, Z2]):-     % This represents the complex multiplication formula but slightly changed so that Z1 and Z2 represent the appropraite calculations
    Z1 is (X1*Y1)-(X2*Y2),                  % and also maintain the correct positions.
    Z2 is (X1*Y2)+(Y1*X2).                  % The answer represents the form (__ + __i) with Z1 and Z2 respectively.

%% ?- cmult([4,10], [2,8], [Z1, Z2]).   Tester code
%% Z1 = -72,
%% Z2 = 52.
%   <--- always have the question under your nose

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 2

% An integer sequence is a list of integers. Write a Prolog predicate
%
%   seqadd/3
%
% such that seqadd(Xs,Yy,Zs) succeeds when Xs and Ys are lists of
% integers of the same length and Zs is their sequence sum.

    seqadd([],[],[]).
    seqadd([A|B], [A1|B1],[A2|Z]):- 
    A2 is A+A1, seqadd(B,B1,Z).

% This uses pattern matching within prolog. It is structured in a way such that the first element is a list with its own first element and disregrads the rest, adds it
% along with the first element of the second list and appends the result to the list Z, it then backtracks and takes the next element in the list and disregard the first
% original element that was used along with the remaining elements. This iterates through the whole list until all the elements of both lists have been added together.

%% ?- seqadd([2,4,6,8],[1,3,5,7],Z).        Tester code.
%% Z = [3, 7, 11, 15].



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 3

% 3a. Explain what backtracking has to do with Prolog. You might find
% this webpage helpful:
%
%   https://www.doc.gold.ac.uk/~mas02gw/prolog_tutorial/prologpages/search.html
%
%       Answer to 3.a:
%           
%           Backtracking is quite heavily integrated with prolog. Backtracking is essentially the process of retracing one's steps. The way this relates
%       to prolog is for example when you have many entries in a database, you can ask a question with multiple answers byt the top entry will be 
%       outputted, after that occurs, prolog will give us the option of cycling through all the other database entries that also answer the given question.
%       This is considered backtracking because it quite literally retraces it's steps and iterates through to the next databse entry that matches.
%
%
%
%
% 3b. What is Cut in prolog and what does it have to do with
% backtracking? Explain your answer by giving examples of Cut used in
% at least one prolog rule, and explain how it affects the
% execution/resolution process.
%
%     Answer to 3.b:
%              
%           As mentioned in the previous question, backtracking is very heavily integreted within Prolog, however this comes at a cost, backtracking is 
%       extremely inefficient. The Reason behind this is that Prolog actually doesnt know the outcome of said backtracking, this leads to time and 
%       resources being wasted in a pursuit of an outcome that doesn't exist. This is where the Cut (denoted by the symbol "!") is beneficial. It is a 
%       goal that will always succeed no matter what, and secondly but more importantly, it cannot be backtracked past.
%       
%       Consider the following example of Cut:
%
%     If we wanted to find the minimum of 2 numbers in Prolog we would normally write this:
%           
%           max(X,Y,A):- X>=Y.
%           max(X,Y,B):- X<Y.
%
%       This means that A will be assigned the max IF X is greater than or equal to Y. Otherwise, B will be assigned the max value if X is smaller than Y.
%       This is inefficient because only one of these conditions can succeed but Prolog has to backtrack and test all the clauses.
%         
%     This can be rewritten with Cut to prevent the inefficiency cause by backtracking.
%
%           max(X,Y,A):- X>=Y, !.
%           max(X,Y,B).
%
%       This implementation of Cut reads like this: A will be assigned the max value if X is greater than or equal to Y. Otherwise, Cut, and output B instead.
%       Cut stops the backtracking by forcing Prolog to only test the first clause and output the second one if the first fails. It is also more efficient 
%       because it doesn't bother to check the second condition if the first one succeeds.
%
%





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 4
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 4

% Write a database for a predicate cycleoflife/1 such that the query
%
%   cycleoflife(X)
%
% returns the instantiations
%
%   X = eat
%   X = sleep
%   X = code
%   X = eat
%   X = sleep
%   X = code
%   ...
%
% in an endless cycle.
%
% (This question has a beautiful and simple answer. If you find
% yourself writing lines and lines of complex code, there’s probably
% something amiss.)
%
%%  ?- cycleoflife(X).          This will output the following result after pressing TAB in order to cycle thorugh to the next entry in the database.
%%  X = eat ;                   It simply just cycles through the database endlessly.
%%  X = sleep ;
%%  X = code ;
%%  X = eat ;
%%  X = sleep ;
%%  X = code 

    cycleoflife(eat).           
    cycleoflife(sleep).
    cycleoflife(code).

    cycleoflife(X):- cycleoflife(X).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 4
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
