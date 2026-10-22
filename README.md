# Cloud and Distributed Computing Lab Experiments

This repository contains twelve networking, distributed-systems, and cloud lab experiments. Run Python examples with Python 3.10 or later. Unless noted otherwise, the examples use localhost and are intended to run on one computer.

### Experiment 1: Socket-based Client-Server IPC

The basic pair sends a list of integers from a client and returns their sum. Start the server, then run the client in separate terminals:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/client.py"
```
To run
```powershell
python .\exp1_ipc_communication\server.py  # Terminal 1
python .\exp1_ipc_communication\client.py  # Terminal 2
```

The folder also contains a pickle-based object serialization variant. Start the matching server and client in separate terminals:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/server_pickel.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/client_pickel.py"
```

```powershell
python .\exp1_ipc_communication\server_pickel.py  # Terminal 1
python .\exp1_ipc_communication\client_pickel.py  # Terminal 2
```

Pickle can execute code while loading; only use this variant with trusted local clients.

### Experiment 2: Remote Method Invocation (RMI)

This experiment uses Pyro4 to call remote calculator methods. Install its dependency first:

```powershell
python -m pip install Pyro4
```

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp2_rmi/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp2_rmi/client.py"
```

Run the server, copy its printed URI, and provide that URI to the client in a second terminal:

```powershell
python .\exp2_rmi\server.py  # Terminal 1
python .\exp2_rmi\client.py  # Terminal 2
```

### Experiment 3: Ricart-Agrawala distributed mutual exclusion

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp3_ricart_agrawala/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp3_ricart_agrawala/client.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp3_ricart_agrawala/rechart.py"
```
To run
```powershell
python .\exp3_ricart_agrawala\server.py
python .\exp3_ricart_agrawala\client.py --id A
python .\exp3_ricart_agrawala\client.py --id B
```

### Experiment 4: Lamport and vector clocks

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp4_clocks/lamportclock.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp4_clocks/vectorclock.py"
```
To run
```powershell
python .\exp4_clocks\lamportclock.py
python .\exp4_clocks\vectorclock.py
```

### Experiment 5

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp5_virtual_instances/README.md"
```

### Experiment 6

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp6_task_scheduling/README.md"
```

### Experiment 7

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp7_hypervisor_clustering/README.md"
```

### Experiment 8: RMI Calculator and Bank Service

Objective: use remote method invocation to calculate a factorial, find the most frequent value in an integer array, and perform bank deposits and withdrawals. The service starts with a balance of `1000.00`; its balance is held in memory and resets when the server stops.

View the source with curl:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp8_rmi_calculator_bank/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp8_rmi_calculator_bank/client.py"
```

Run the server in one terminal and the client in another. Use the client menu to select `factorial`, `mode`, `deposit`, `withdraw`, or `balance`; enter `quit` to exit. If values tie for the mode, the first such value in the input array is returned.

```powershell
python .\exp8_rmi_calculator_bank\server.py
python .\exp8_rmi_calculator_bank\client.py
```

This RMI demo uses JSON messages over TCP sockets and requires only Python 3.10 or later.

### Experiment 9: One-to-Many TCP Message Broadcast

Objective: run one TCP server that accepts multiple clients and broadcasts each client's messages to all connected clients.

View the source with curl:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp9_broadcast_messaging/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp9_broadcast_messaging/client.py"
```

Start the server in one terminal, then run the client in two or more additional terminals. Enter a name for each client, then type messages to broadcast them. Enter `/quit` to disconnect a client; press Ctrl+C in the server terminal to stop the server.

```powershell
python .\exp9_broadcast_messaging\server.py
python .\exp9_broadcast_messaging\client.py
```

The sample binds to `127.0.0.1:6009` for clients on the same computer. To connect from another computer, set `HOST` in both files to the server's LAN address and allow TCP port 6009 through its firewall.

### Experiment 10: Socket Communication with Object Serialization

Objective: serialize a Python object, send it from a client to a server over TCP, and return a serialized response. The example sends a name and a list of integers; the server calculates their sum.

View the source with curl:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp10_socket_object_serialization/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp10_socket_object_serialization/client.py"
```

Run the server in one terminal, then run the client in another terminal. Enter a name and integers separated by spaces.

```powershell
python .\exp10_socket_object_serialization\server.py
python .\exp10_socket_object_serialization\client.py
```

This pickle-based example is for trusted local connections only: never unpickle data from unknown or untrusted clients. It uses TCP port `6010`.

### Experiment 11: Client-Server Distinct Vowel Counter

Objective: send text from a client to a server and count how many different vowels (`a`, `e`, `i`, `o`, `u`) appear. The count is case-insensitive, so repeated or uppercase vowels count once.

View the source with curl:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp11_distinct_vowel_counter/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp11_distinct_vowel_counter/client.py"
```

Start the server in one terminal, then run the client in another and enter text when prompted:

```powershell
python .\exp11_distinct_vowel_counter\server.py
python .\exp11_distinct_vowel_counter\client.py
```

The server listens on `127.0.0.1:6011` and can process multiple client connections sequentially.

### Experiment 12: Threaded Message Passing and Critical-Section Demo

Objective: accept multiple TCP clients on a threaded server, forward messages between clients, and serialize critical-section requests with a server-side lock. The client menu offers message passing and labeled Ricart-Agrawala, token-ring, and centralized-coordinator examples; all three critical-section options in this script use the same server-side lock for demonstration.

View the source with curl:

```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp12_threading/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp12_threading/client.py"
```

Start the server in one terminal and run two or more clients in separate terminals. Select **1** to send a message to other connected clients, or select **2**, **3**, or **4** to request the critical section. Select **5** to exit the client.

```powershell
python .\exp12_threading\server.py  # Terminal 1
python .\exp12_threading\client.py  # Terminal 2 and additional terminals
```

This example binds to `127.0.0.1:5000`, the same address and port used by Experiment 1's basic socket demo. Run those experiments separately, or change the port consistently in the server and client before running them together.
