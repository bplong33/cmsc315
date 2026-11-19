"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create an empty dictionary
    host = {}
    # method 1: generally preferred in Python
    # adds the key "hostname" with value "host-9574"
    host["hostname"] = "host-9574"  # create the key hostname, which
    # adds key "os" with value "Rocky"
    host["os"] = "Rocky"
    # asdds key "storage" with value "1 TB"
    host["storage"] = "1 TB"
    # method 2: Allows updating or adding multiple key/value pairs at a time
    # adds 2 keys, "ram", and "ip", with the respective values
    host.update({"ram": "32 GB", "ip": "192.168.15.74"})

    # Python dictionaries use Open Addressing, using a different hashing method
    # depending on the data type of the key. For example a string key would use
    # a string-hash method. Collisions are handled with a "deterministic pseudo
    # random" probing sequence, basically meaning it doesn't simply check the
    # next neighboring bucket. For each of the above insertions, the string key
    # is hashed, and the lower bits are used to determine which bucket is inserted
    # into. If that bucket is populated, it will probe for the next empty bucket
    # using a specific probing method. The key is stored in the first empty bucket
    # found.

    print("\nCreated Dictionary holding data for a host:")
    for k, v in host.items():
        print(f"  \u2192 {k}: {v}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # For each key accessed, the string key is hashed using the same hash method
    # that was used when it was stored. It will then search for that hashed key,
    # using the probing method discussed previously to determine the next bucket
    # to search. It will continue to search until it either finds the key, or finds
    # an empty-since-start bucket. When the key is found, the value is returned.

    print("\nRetrieved Hostname and IP from the Dictionary:")
    print(f"  \u2192 Hostname: {host['hostname']}; IP: {host.get('ip')}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("\nHost dictionary before update:")
    for k, v in host.items():
        print(f"  \u2192 {k}: {v}")

    print("\nUpdating IP Address...")
    host.update({"ip": "172.16.85.193"})
    # host['ip'] = "172.16.85.193"

    print("\nHost dictionary after update:")
    for k, v in host.items():
        print(f"  \u2192 {k}: {v}")

    # similar to the retrieval in the previous section, the key is hashed, and
    # the buckets are searched for the the matching key based on the hash. Python
    # will check each key in the probe chain. If python finds a bucket where the
    # matches the update key, it will update the value. While searching for the key,
    # if Python finds an empty-since-removal bucket, it will record this spot to
    # save the key to IF the key is not found. It will continue searching until an
    # empty-since-start bucket is found, or the correct hash and key are found.

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("\nHost dictionary before delete:")
    for k, v in host.items():
        print(f"  \u2192 {k}: {v}")

    del host["ram"]

    print("\nHost dictionary after delete:")
    for k, v in host.items():
        print(f"  \u2192 {k}: {v}")

    # The Key is hashed, and the the hash will determine where Python starts
    # looking for the key. It will check each bucket determined by Python's
    # deterministic pseudo-random probing method. If the key is found, it
    # and it's value are removed, marking the bucket empty-since-removal

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # **Lookup Missing Key**

    # using the bracket notation to access a key that does not exist will
    # cause a KeyError.
    print("\nSearch for 'ram' key (deleted in last step) using bracket notation:")
    key = "ram"
    try:
        print(f"  \u2192 RAM: {host[key]}")
    except KeyError:
        print(f"  \u2192 Key {key} could not be found")

    # Alternatively, using the .get method of a dict will allow you to not throw
    # an error

    print("\nSearch for 'ram' key (deleted in last step) using bracket notation:")
    print(f"  \u2192 RAM: {host.get(key)}")
    # you can also set a default return value in the case the key isn't found
    print(f"  \u2192 RAM (with default set): {host.get(key, f'{key} not found')}")


class Host:
    def __init__(
        self,
        hostname: str,
        os: str,
        storage: str = "500 GB",
        ram: str = "8 GB",
        ip: str | None = None,
    ):
        self.hostname = hostname
        self.os = os
        self.storage = storage
        self.ram = ram
        self.ip = ip

    def __str__(self):
        return (
            self.hostname
            + "\n  \u2192 "
            + "\n  \u2192 ".join(
                [f"{k}: {v}" for k, v in vars(self).items() if k != "hostname"]
            )
        )


class HostInventory:
    def __init__(self):
        self.hosts: list[Host] = []  # initialize with empty list

    def add_host(self, host: Host):
        self.hosts.append(host)


def real_world_scenario():
    print("\n=== Real World Scenario ===")
    print("Demonstrate How an API might sent data in a dictionary/json format")

    # in a live api, it is common for data to be sent via json format, which is often
    # converted to a dictionary datatype in python. Lets assume we have multiple hosts
    # being added to an inventory, and the requests come through as shown below
    api_reqs = [
        {
            "hostname": "web-prod-01",
            "os": "Ubuntu 24.04 LTS",
            "storage": "500 GB",
            "ram": "16 GB",
            "ip": "192.168.1.10",
        },
        {
            "hostname": "db-primary-01",
            "os": "Red Hat Enterprise Linux 9",
            "storage": "2 TB",
            "ram": "64 GB",
            "ip": "192.168.1.15",
        },
        {
            "hostname": "app-staging-01",
            "os": "Debian 12",
            "storage": "250 GB",
            "ram": "8 GB",
            "ip": "192.168.1.22",
        },
        {
            "hostname": "dc-win-01",
            "os": "Windows Server 2022",
            "storage": "1 TB",
            "ram": "32 GB",
            "ip": "192.168.1.30",
        },
        {
            "hostname": "cache-redis-01",
            "os": "Alpine Linux 3.20",
            "storage": "100 GB",
            "ram": "32 GB",
            "ip": "192.168.1.45",
        },
        {
            "hostname": "backup-nas-01",
            "os": "TrueNAS SCALE",
            "storage": "16 TB",
            "ram": "64 GB",
            "ip": "192.168.1.50",
        },
    ]

    # when received, each request can be unpacked and passed as arguments, assuming
    # the keys match the arguments for the method or class init
    inventory = HostInventory()
    for req in api_reqs:
        inventory.add_host(Host(**req))

    print("\nCurrent Inventory\n------------------------------")
    print("\n".join([str(h) for h in inventory.hosts]))

    # using this process can streamline the process of parsing an API request into
    # an object. When Paired with something like FastAPI and Pydantic, this process
    # is automated even further.


if __name__ == "__main__":
    main()
    real_world_scenario()
