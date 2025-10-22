# 🧩 Process Creation — Windows & Linux  
*Parallel and Distributed Computing: Module 01*

This module introduces how **processes** are created in modern operating systems — focusing on both **Linux** (`fork()`) and **Windows** (`CreateProcess()`).

It forms the foundation of **parallel** and **distributed computing**, where multiple processes (or systems) work together to achieve concurrency and scalability.

---

## 🧠 Why Process Creation Matters

In **parallel computing**, multiple processes or threads run *simultaneously* on one or more CPUs.  
In **distributed computing**, processes run across *different machines* connected through a network.

Understanding how an OS *creates, manages, and isolates* these processes is critical — it’s the first step toward building systems that can:

- Run multiple tasks concurrently  
- Communicate across nodes  
- Manage synchronization, scheduling, and shared resources efficiently  

Before exploring threads, IPC (Inter-Process Communication), or distributed systems, you must understand how an OS **spawns a new process**.

---

## ⚙️ Process Creation in Linux — `fork()`

In Linux and UNIX-like systems, `fork()` is used to **create a child process** by duplicating the parent.  

When `fork()` is called:
- The OS **copies the parent’s memory space** (using Copy-on-Write optimization)
- Both **parent and child continue** execution from the same point
- The **child** gets a return value of `0`
- The **parent** gets the **child’s PID**

This mechanism allows Linux to create independent processes efficiently.

---

## ⚙️ Process Creation in Windows — `CreateProcess()`

Windows uses a more explicit system call — `CreateProcess()` — which:
- Loads a **new executable image** into memory  
- Initializes a **new process context**
- Starts a **main thread** inside that process  

Unlike `fork()`, it doesn’t clone the parent; it starts a **completely new program**.  
This makes Windows process creation more modular but also slightly heavier compared to Linux `fork()`.

---

## 🧩 OS Concepts Involved

| Concept | Description |
|----------|-------------|
| **Process Control Block (PCB)** | OS data structure storing process state, registers, PID, etc. |
| **Memory Layout** | Each process gets its own code, data, heap, and stack segments. |
| **Copy-on-Write (COW)** | Linux optimization where parent and child share memory until one modifies it. |
| **Instruction Pointer (IP)** | Points to the next instruction — both parent and child resume at the same location after fork. |
| **Context Switching** | OS mechanism to switch CPU control between processes. |
| **Isolation** | Each process runs in its own protected address space for safety. |

These are **fundamental OS behaviors** that make concurrent execution possible — forming the basis for higher-level parallel and distributed models.

---

## 🔗 Relation to Parallel and Distributed Computing

| Domain | Relation to Process Creation |
|--------|-------------------------------|
| **Parallel Computing** | Multiple processes on the *same system* share CPU cores to perform tasks concurrently. |
| **Distributed Computing** | Processes may run on *different systems* but coordinate through networking (e.g., RPC, sockets). |
| **Process Management** | Knowing how to create, synchronize, and terminate processes is essential for scaling workloads. |
| **Resource Sharing** | Each process has isolated memory, requiring controlled sharing via IPC or message passing. |

Process creation is the **entry point** to both — without processes, there’s no concurrency, parallelism, or distribution.

---


Each example demonstrates how the OS spawns a child process and how the system allocates memory and identifiers.

---

## 🧠 Summary

- Process creation is **step one** of concurrency.
- Linux uses `fork()` to duplicate processes.
- Windows uses `CreateProcess()` to launch new executables.
- Both rely on the OS for memory isolation, scheduling, and synchronization.
- Understanding this sets the stage for exploring **threads**, **IPC**, and **distributed computation**.

---

## 👨‍💻 Message from the Author

**Aheed Khan** — Cybersecurity & Systems enthusiast  
Exploring AI, Operating Systems, and Distributed Systems through hands-on code and research.  
Always learning how the *core of computing* powers everything above it.

---


