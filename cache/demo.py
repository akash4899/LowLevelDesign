from cache import LRUCache


class Demo:
    @staticmethod
    def run():
        cache = LRUCache(2)

        cache.put(1, 'akash')
        cache.put(2, 'darvin')
        cache.get(2)
        cache.put(3, 'Ankit')
        cache.get(1)

if __name__ == '__main__':
    Demo.run()