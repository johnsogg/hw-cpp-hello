//
// hello_test.cpp
//
// This is the unit test file for this homework. It is documented in
// order to give you a little guided tour of what this is all
// about. Future test files won't be documented, but they will work in
// the same general way as this one.

// First we define a flag for the pre-processor that says we're using
// the Catch unit testing framework. This is a fairly advanced, fairly
// magical thing, and you won't need to understand it.
#define CATCH_CONFIG_MAIN

// Now include the entire contents of the file 'catch.hpp'. It
// includes the entire unit testing framework. You won't need to
// understand Catch, but you _will_ need to understand what the
// #include statement does. Eventually.
#include "catch.hpp"

// Include the entire contents of the file 'hello.h'. That's where we
// provide function signatures for all of the functions you will
// implement. Think of it as a sort of checklist that the compiler
// uses to know what to expect.
#include "hello.h"

// After this we have two "macros", which look like functions, but
// aren't. Again, this is advanced and magical and you won't need to
// understand them. The important thing about the test cases is what
// happens inside of them.

TEST_CASE("Hello World: sanity check", "[sanity]") {
  // Inside a test case we'll have one or more assertions. An
  // assertion just takes a simple expression, and if the expression
  // evaluates to true, it passes; otherwise it fails the entire test
  // case. This test case is super boring because it always passes
  // (that's why I call it a sanity check, so I know that if it works,
  // then I've at least set things up correctly).
  //
  // If you want to run just this test case, build the project and run
  // it like this, from the command line:
  //
  // $ make
  // $ ./hello_test [sanity]
  //
  // If it builds and runs correctly, it will say "All tests passed (1
  // assertion in 1 test case)".
  REQUIRE(true);
}

TEST_CASE("Hello World: get greeting", "[greeting]") {
  // This is a different test case, and it can be run independently of
  // the sanity check case.
  //
  // It is less boring than the sanity check, because it actually runs
  // the 'get_greeting' function that you should implement. It checks
  // to see if the return value is equivalent to "Hello!". If not, the
  // test case fails.
  //
  // Try playing with your implementation. Have it return an incorrect
  // value, and see what happens when you run it directly:
  //
  // $ make
  // $ ./hello_test [greeting]
  REQUIRE(get_greeting() == "Hello!");
}
