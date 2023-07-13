class HashMap:
    def __init__(self):
        self.size = 10  # Initial size of the hashmap
        self.map = [[] for _ in range(self.size)]

    def _get_bucket_index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                # Key already exists, update the value
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")

    def contains_key(self, key):
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for existing_key, _ in bucket:
            if existing_key == key:
                return True
        return False

    def size(self):
        count = 0
        for bucket in self.map:
            count += len(bucket)
        return count

    def keys(self):
        all_keys = []
        for bucket in self.map:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.map:
            for _, value in bucket:
                all_values.append(value)

        return all_values

    def items(self):
        all_items = []
        for bucket in self.map:
            all_items.extend(bucket)
        return all_items


category = HashMap()

category.put("green", 1)
category.put("blue", 120)
category.put("yellow", 5)
category.put("yellow", 12)

print(category.items())
print(category.values())
print(category.keys())
