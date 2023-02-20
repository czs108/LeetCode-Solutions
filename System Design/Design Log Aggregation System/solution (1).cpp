// Design Log Aggregation System


class LogAggregator {
public:
    LogAggregator(int machines, int services) {}

    void pushLog(int logId, int machineId, int serviceId, string message) {
        logs_.insert({logId, move(message)});
        logIdsByServices_[serviceId].push_back(logId);
        logIdsByMachines_[machineId].push_back(logId);
    }

    vector<int> getLogsFromMachine(int machineId) {
        return logIdsByMachines_[machineId];
    }

    vector<int> getLogsOfService(int serviceId) {
        return logIdsByServices_[serviceId];
    }

    vector<string> search(int serviceId, string searchString) {
        vector<string> logs;
        for (int id : logIdsByServices_[serviceId]) {
            if (logs_[id].find(searchString) != string::npos) {
                logs.push_back(logs_[id]);
            }
        }

        return logs;
    }

private:
    unordered_map<int, string> logs_;
    unordered_map<int, vector<int>> logIdsByServices_;
    unordered_map<int, vector<int>> logIdsByMachines_;
};

/**
 * Your LogAggregator object will be instantiated and called as such:
 * LogAggregator* obj = new LogAggregator(machines, services);
 * obj->pushLog(logId,machineId,serviceId,message);
 * vector<int> param_2 = obj->getLogsFromMachine(machineId);
 * vector<int> param_3 = obj->getLogsOfService(serviceId);
 * vector<string> param_4 = obj->search(serviceId,searchString);
 */