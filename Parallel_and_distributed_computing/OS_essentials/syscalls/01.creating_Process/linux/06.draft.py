# ================================================================
#  Brainstorming & Notes — Understanding fork() in Linux (Python)
# ================================================================
# This file acts as a rough lab notebook / scratchpad for learning
# how process creation using fork() works in both Python and C logic.
# Comments explain the sequence conceptually.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# 01. Basic Example — Creating a Child Process with os.fork()
# ---------------------------------------------------------------
# In Linux, os.fork() duplicates the current process.
# After duplication:
#   - The parent receives the child’s PID as return value.
#   - The child receives 0 as return value.
# Both processes continue execution independently from the next line.

import os

def main():
    pid = os.fork()  # System call to duplicate the process

    if pid == 0:
        # This branch runs in the child process
        print("Hello from the child process!")
    else:
        # This branch runs in the parent process
        print(f"Hello from the parent process! Child PID: {pid}")

if __name__ == "__main__":
    main()


# ---------------------------------------------------------------
# 02. Inspecting PIDs Before and After fork()
# ---------------------------------------------------------------
# os.getpid() gives the current process’s ID.
# Before fork() → one process only.
# After fork() → both parent and child execute the same code line.

import os

print("Before fork, single process PID:", os.getpid())

def main():
    pid = os.fork()       # Creates a copy of the current process
    print("Value returned by fork():", pid)

if __name__ == "__main__":
    main()

# Expected output pattern:
#   Parent → prints child's PID (e.g., 613)
#   Child  → prints 0


# ---------------------------------------------------------------
# 03. Kernel Pseudocode (Conceptual)
# ---------------------------------------------------------------
# The following illustrates how the kernel internally manages fork().
# This is *not* Python code — only conceptual C-style pseudocode.

# pid_t fork() {
#     pid_t child_pid = create_process_copy();  // duplicate current process
#
#     if (in_parent_process)
#         return child_pid;   // Parent gets child’s PID
#     else
#         return 0;           // Child gets 0
# }


# ---------------------------------------------------------------
# 04. Step-by-Step Conceptual Explanation
# ---------------------------------------------------------------
# Step 1 — Before fork():
#     One process exists (e.g., PID = 1137)
#     The process calls: pid_t pid = fork();
#
# Step 2 — Inside the Kernel:
#     1. Kernel creates a copy of the calling process.
#     2. Assigns a new PID to the child (e.g., 1138).
#     3. Returns to both:
#        - Parent receives 1138.
#        - Child receives 0.
#
# Step 3 — Duplication Moment:
#     The OS now has two processes in memory:
#         Parent (PID 1137)
#         Child  (PID 1138)
#
#     Both start executing from the line *after* the fork() call.
#
# Step 4 — Independent Execution:
#     Each process has its own:
#         - CPU registers
#         - Memory space
#         - Stack
#         - Instruction pointer
#
#     The same code runs in both — but variables differ:
#
#         Parent sees pid = 1138
#         Child  sees pid = 0
#
# So both follow different conditional branches but share the same code structure.


# ---------------------------------------------------------------
# 05. Example — Fork Branch Logic (C-style logic)
# ---------------------------------------------------------------
# In C:
#
#     pid_t pid = fork();
#
#     if (pid == 0) {
#         printf("Child process\n");
#     } else {
#         printf("Parent process\n");
#     }
#
# Output (two lines, one from each process):
#
#     Child process
#     Parent process
#
# Both execute the same code from the same line after fork().


# ---------------------------------------------------------------
# 06. Concept Recap — Why fork() Returns Different Values
# ---------------------------------------------------------------
# In the kernel’s implementation:
#
#     if (in_parent_process)
#         return child_pid;
#     else
#         return 0;
#
# This difference allows the program to know which branch
# is running (parent or child) even though both execute
# the same source code after the fork call.


# ---------------------------------------------------------------
# 07. Optional — Visual Summary (Mental Model)
# ---------------------------------------------------------------
#  Parent (PID 1137) calls fork()
#      ↓
#  Kernel duplicates process
#      ↓
#  Two processes exist:
#      • Parent PID = 1137 (receives child PID = 1138)
#      • Child  PID = 1138 (receives 0)
#
#  Both start executing at the same point in code:
#
#      if (pid == 0):
#          → child path
#      else:
#          → parent path
#
#  Both continue independently after this point.
# ---------------------------------------------------------------

