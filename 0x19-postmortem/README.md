# POSTMORTEM

![](./no_internet.jpg)
### ISSUE SUMMARY
An incident was reported on Tuesday 5th December 2022 involving internet connectivity issues by majority of the users in the office. The incident started at 8:45 AM EAT and lasted until 9:10 AM EAT. The root cause was later diagnosed to be a damaged router affected by overvoltage in the server room after a power blackout.

### TIMELINE (ALL TIMES EAT)
8:45 AM : First report of no internet connectivity by users
8:47 AM : Escalation to the network administrator after multiple reports by users
8:49 AM : Network administrator starts investigation from networking monitoring software
8:55 AM : The damaged router identified and replaced
9:00 AM : Configuration on replacement router started
9:05 AM : Configuration on replacement router complete
9:06 AM : Network restarted
9:10 AM : Internet connectivity restored

### ROOT CAUSE
At 8:40 AM EAT a power blackout was experienced in the whole building. On power restoration at 8:42 AM EAT all systems were booted up and started running normally. At 8:45 AM EAT the first case of no internet connectivity was reported and a few minutes later several other users reported of the same. It was after inspection of the router that it was clear some components had been burnt and therefore damaging the router from the power blackout.

### RESOLUTION AND RECOVERY
The network administrator was notified of the issue and was able to identify the router being offline despite power retoration. He was able to disconnect and inspect it fully as damaged from overvoltage as some internal components were charred. The router had suffered damaged as it is the only device connected directly to the wall outlet. The solution was to replace it with another router which was able to restore all intenet connectivity fully.

### CORRECTIVE AND PREVENTATIVE MEASURES
To prevent such occurences from happening again, a UPS was purchased to provide cover in case of any other power abnormalities. Also the addition of another router in the networking setup to provide failover in case of any other unforeseen circumstances.
Additional measures to be taken include:
    - Configuring alerts and notifications for network related issues
    - Getting an electrician to inspect the state of the electical circuitry in the office
    - Regularly monitoring the power voltage
    - Inspecting devices after a power incidence
