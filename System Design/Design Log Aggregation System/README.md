# Design Log Aggregation System

------

Implement a Log Aggregation System which aggregates logs from various services in a data center and provides search APIs.

Design the `LogAggregator` class:

- `LogAggregator(int machines, int services)` initializes the object with `machines` and `services` representing the number of machines and services in the data center, respectively.
- `void pushLog(int logId, int machineId, int serviceId, String message)` adds a log with id `logId` notifying that the machine `machineId` sent a string `message` while executing the service `serviceId`.
- `List<Integer> getLogsFromMachine(int machineId)` returns a list of ids of all logs added by machine `machineId`.
- `List<Integer> getLogsOfService(int serviceId)` returns a list of ids of all logs added while running service `serviceId` on any machine.
- `List<String> search(int serviceId, String searchString)` returns a list of messages of all logs added while running service `serviceId` where the message of the log contains `searchString` as a substring.

Note that:

- The entries in each list should be in the order they were added, i.e., the older logs should precede the newer logs.
- A machine can run multiple services more than once. Similarly, a service can be run on multiple machines.
- All `logId` may not be ordered.
- A substring is a contiguous sequence of characters within a string.

**Example:**

```
Input:
["LogAggregator", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "getLogsFromMachine", "getLogsOfService", "search", "search"]
[[3, 3], [2322, 1, 1, "Machine 1 Service 1 Log 1"], [2312, 1, 1, "Machine 1 Service 1 Log 2"], [2352, 1, 1, "Machine 1 Service 1 Log 3"], [2298, 1, 1, "Machine 1 Service 1 Log 4"], [23221, 1, 2, "Machine 1 Service 2 Log 1"], [23121, 1, 2, "Machine 1 Service 2 Log 2"], [23222, 2, 2, "Machine 2 Service 2 Log 1"], [23122, 2, 2, "Machine 2 Service 2 Log 2"], [23521, 1, 2, "Machine 1 Service 2 Log 3"], [22981, 1, 2, "Machine 1 Service 2 Log 4"], [23522, 2, 2, "Machine 2 Service 2 Log 3"], [22982, 2, 2, "Machine 2 Service 2 Log 4"], [2], [2], [1, "Log 1"], [2, "Log 3"]]
Output:
[null, null, null, null, null, null, null, null, null, null, null, null, null, [23222, 23122, 23522, 22982], [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982], ["Machine 1 Service 1 Log 1"], ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]]

Explanation:
LogAggregator logAggregator = new LogAggregator(3, 3);      // There are 3 machines and 3 services
logAggregator.pushLog(2322, 1, 1, "Machine 1 Service 1 Log 1");
logAggregator.pushLog(2312, 1, 1, "Machine 1 Service 1 Log 2");
logAggregator.pushLog(2352, 1, 1, "Machine 1 Service 1 Log 3");
logAggregator.pushLog(2298, 1, 1, "Machine 1 Service 1 Log 4");
logAggregator.pushLog(23221, 1, 2, "Machine 1 Service 2 Log 1");
logAggregator.pushLog(23121, 1, 2, "Machine 1 Service 2 Log 2");
logAggregator.pushLog(23222, 2, 2, "Machine 2 Service 2 Log 1");
logAggregator.pushLog(23122, 2, 2, "Machine 2 Service 2 Log 2");
logAggregator.pushLog(23521, 1, 2, "Machine 1 Service 2 Log 3");
logAggregator.pushLog(22981, 1, 2, "Machine 1 Service 2 Log 4");
logAggregator.pushLog(23522, 2, 2, "Machine 2 Service 2 Log 3");
logAggregator.pushLog(22982, 2, 2, "Machine 2 Service 2 Log 4");
logAggregator.getLogsFromMachine(2);    // return [23222, 23122, 23522, 22982]
                                        // Machine 2 added 4 logs, so we return them in the order
                                        // they were added.
logAggregator.getLogsOfService(2);      // return [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982]
                                        // 8 logs were added while running service 2 on a machine.
logAggregator.search(1, "Log 1");       // return ["Machine 1 Service 1 Log 1"]
                                        // There is only one log that was added while running service 1
                                        // and contains "Log 1".
logAggregator.search(2, "Log 3");       // return ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]
```

**Constraints:**

- All `logId` are unique.