### Experiment 1: Socket-based client-server IPC
```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp1_ipc_communication/client.py"
```
To run
```powershell
python .\exp1_ipc_communication\server.py  # Terminal 1
python .\exp1_ipc_communication\client.py  # Terminal 2
```
### Experiment 2: Remote Method Invocation (RMI)
```powershell
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp2_rmi/server.py"
curl.exe --ssl-no-revoke -L "https://raw.githubusercontent.com/deadcorpse1/cloud/main/exp2_rmi/client.py"
```
To run
```powershell
python .\exp2_rmi\server.py
python .\exp2_rmi\client.py
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
