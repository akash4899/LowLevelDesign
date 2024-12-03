import time

class RateLimiter:
    def __init__(self):
        self.rules = []
        self.requests = {}

    def add_rule(self, rule):
        self.rules.append(rule)

    def is_allowed(self, request):
        current_time = time.time()
        #  print()
         # print(current_time)
        # print()
        client_id = request.client_id
        api = request.api
        current_rule = None
        for rule in self.rules:
            if rule.client_id == client_id and rule.api == api:
                current_rule = rule

        if current_rule is None:
            return True

        current_rule_id = current_rule.id
        current_requests = self.requests.get(current_rule_id)
        print(current_rule.total_requests)
        if current_requests:
            for request in current_requests:
                # print(request.time)
                # print(current_time)
                if current_time-request.time > current_rule.window_size:
                    print(current_time)
                    print(request.time)
                    print(current_time-request.time)
                    current_rule.total_requests -= 1
                    self.requests[current_rule_id].remove(request)

        # print(current_rule.total_requests)
        if current_rule.total_requests < current_rule.max_requests_in_window:
            current_rule.total_requests += 1
            # print(current_rule_id)
            # print(request)
            if current_rule_id not in self.requests:
                self.requests[current_rule_id] = []
            self.requests[current_rule_id].append(request)
            return True

        return False



