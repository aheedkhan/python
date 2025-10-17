import os

# Print the current process ID before any fork.
# At this point, only one process exists — the parent.
print("Before fork, single process PID:", os.getpid())


