from rate_limiter_main import RateLimiter
from rule import Rule
from request import Request
import time


class Demo:
    @staticmethod
    def run():
        rule = Rule(1, "e4dbd58c-ad30-11ee-b331-2a4b9f06442a", "POST /products", 10, 5)


        rate_limiter = RateLimiter()
        rate_limiter.add_rule(rule)
        # request = Request("e4dbd58c-ad30-11ee-b331-2a4b9f06442a", "POST /products", time.time())
        for i in range(12):
            request = Request("e4dbd58c-ad30-11ee-b331-2a4b9f06442a", "POST /products", time.time())
            print(rate_limiter.is_allowed(request))

        time.sleep(8)
        print("new requests:")

        for i in range(15):
            request = Request("e4dbd58c-ad30-11ee-b331-2a4b9f06442a", "POST /products", time.time())
            print(rate_limiter.is_allowed(request))



if __name__ == '__main__':
    Demo.run()

