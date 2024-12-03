class Rule:
    def __init__(self, id, client_id, api, max_requests_in_window, window_size):
        self.id = id
        self.client_id = client_id
        self.api  = api
        self.max_requests_in_window = max_requests_in_window
        self.window_size  = window_size
        self.total_requests = 0