from typing import List, Tuple, Any


class HashMap:
    def __init__(self):
        self._size: int = 10  # Initial size of the hashmap
        self.map = [[] for _ in range(self._size)]

    def _get_bucket_index(self, key: str) -> int:
        return hash(key) % self._size

    # def __init__(self, size=10):
    #     self._size: int = size  # Initial size of the hashmap
    #     self._num_elements: int = 0
    #     self.map: List[List[Tuple[str, Any]]] = [[] for _ in range(self._size)]
    #
    # def _calculate_load_factor(self) -> float:
    #     return self._num_elements / self._size

    # def _resize_map(self, new_size: int) -> None:
    #     new_map: List[List[Tuple[str, Any]]] = [[] for _ in range(new_size)]
    #
    #     for bucket in self.map:
    #         for key, value in bucket:
    #             bucket_index = hash(key) % new_size
    #             new_map[bucket_index].append((key, value))
    #
    #     self.map = new_map
    #     self._size = new_size

    def put(self, key: str, value: Any) -> None:
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                # Key already exists, update the value
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        # self._num_elements += 1

        # load_factor = self._calculate_load_factor()
        # if load_factor > 0.7:
        #     new_size = self._size * 2
        #     self._resize_map(new_size)

    def get(self, key: str) -> Any:
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: str) -> None:
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                # self._num_elements -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def contains_key(self, key: str) -> bool:
        bucket_index = self._get_bucket_index(key)
        bucket = self.map[bucket_index]
        for existing_key, _ in bucket:
            if existing_key == key:
                return True
        return False

    def size(self) -> int:
        count: int = 0
        for bucket in self.map:
            count += len(bucket)
        return count

    def keys(self) -> List[str]:
        all_keys = []
        for bucket in self.map:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    def values(self) -> List[Any]:
        all_values = []
        for bucket in self.map:
            for _, value in bucket:
                all_values.append(value)
        return all_values

    def items(self) -> List[Tuple[str, Any]]:
        all_items = []
        for bucket in self.map:
            all_items.extend(bucket)
        return all_items


programming = HashMap()

test = {}

programming.put("python", "Cool programming language")
programming.put("programmers", 2)

print(programming.contains_key("python"))  # True
print(programming.contains_key("javascript"))  # False
print(programming.items())  # [("python", "Cool programming language"), ("programmers", 2)]
print(programming.values())  # ["Cool programming language", 2]
print(programming.keys())  # ["python", "programmers"]
print(programming.size())  # 2
programming.remove("python")
print(programming.items())  # [('programmers', 2)]
