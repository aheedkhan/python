# This file is purely conceptual (not executed).
# It demonstrates what the kernel does internally during fork().

"""
pid_t fork() {
    pid_t child_pid = create_process_copy();  // Duplicate current process memory, stack, registers
    if (in_parent_process)
        return child_pid;  // Parent receives child's PID
    else
        return 0;          // Child receives 0
}
"""
