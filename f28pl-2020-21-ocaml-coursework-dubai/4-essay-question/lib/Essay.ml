(* Coursework template

   Nabeel Alkindy, H00287325          <--- so we know who you are
   F28PL Coursework 2, OCaml        <--- sanity check

   Deadline is 27 November 2020 (end week 11).

   You may assume variables and functions defined in earlier questions
   in your answers to later questions, though you should add comments
   in code explaining this if any clarification might help read your
   code.

   To do this coursework, FORK, THEN CLONE the gitlab project.

   If you do it the other way around, then you'll have cloned *my*
   project (which you can't `git push` to), rather than cloned *your
   fork* of the project (which you can `git push` to).

   Any questions, don't guess: ask.

   This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE. *)

(* Write an essay on the OCaml type system. Be clear, to-the-point, and
   concise. Convince your marker that you understand:

   - Function type signatures.
   - Polymorphism.
   - List types and tuple types (and their differences).
   - OCaml pattern-matching on values (e.g. integers) and structures (e.g. lists).
   - Named and anonymous functions.
   - Recursive functions.
   - Unit and property based tests.

   Include short code-fragments (as in the lectures) to illustrate
   your observations.
   Do this in a literate programming style to include executable code
   to demonstrate the concepts you're writing about, e.g. *)

(*    ESSAY:

   Funtion type signatures in OCaml are essentially a way of defining or declaring what data an object will be and also of what datatype should the result be. 
In Ocaml, we can write a basic function to determine the total number of goals scored during a game:

let total_goals (team1 : int) (team2 : int) : int = team1 + team2

      The function type signature of this function would be: 

val total_goals : int -> int -> int = <fun>

this signature shows that the first 2 variables are of type int and that is also the type that the result should return in. Polymorphism in other languages such as in
Java means that two or more functions can have the same name but also different parameters or different variables. However, in OCaml, a polymorphic fucntion is a function 
that can have paramters of multiple different types. This is achieved by not needing to specify the parameter type. A function can be written to determine the greater value: 

let greater a b = if a > b then a else b

 This function will yield the type signature 




val higher : 'a -> 'a -> 'a = <fun>

and the type 'a is an indication that this is a polymorphic function because it means
"for all types of a". Tuples and list are quite similar as they are both used to store a number of items. In short, tuples have limited capacity but can store objects of 
multiple data types whereas a list can objects of the same type but it has infinite capactiy. Pattern Matching is a very powerful tool. It is an arrangement of a variety 
of different element types that can be used in tandem with value and guides the computation in the right direction. The most basic method of declaring a function is by 
declaring an anonymous function. the 'fun' keyword is an indication of an anonymous function and here is an example "(fun x -> x + 5)". This will yield the following 
type signature in OCaml: 

- : int -> int = <fun>

These anon. functions can be manipulated and worked with in the same way that named functions can. They can be applied
to applied to an argument or even put them into various data structures such as lists. Named functions are the exact same as anonymous functions but they are simply given 
a name. Recursive Functions are very interesting because unlike other languages such as Java where you would have to use 'for' loops for recursion, in OCaml you can use the 
marking word 'rec'. The defining factor of a recursive function is that it calls itself within its own definition. This allows it to loop back to the beginning and
automatically execute its contents without having to manually hard-code the same function over and over.

An example of a recursive function:

let rec fact n = match n with
    | 0 -> 1
    | n -> n * fact (n + 2);;

Notice the 'rec' marking and how the 'fact' function calls itself in its definition.
Unit and Property based tests are the core testing methods within Test-driven developmenting. With Unit tests or as they are called in Ocaml, OUnit tests, we are able to test 
one small piece of functionality without needing to test the whole program at once. We can write Unit tests for specific functions to ensure they are performing the way that 
they should. Property Tests, from my understanding, is to cover the cases in which the main function wont account for such as the multiplication of a tuple by (0, 0).

*)







(* The following function adds two numbers together. It has types ... *)

let add (x:int) (y:int) : int = x + y

(* The following function... *)
