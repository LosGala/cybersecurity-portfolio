# Algorithm for File Updates in Python

## Project Description

As a security professional at a health care company, I developed a Python algorithm to manage access to restricted content containing personal patient records. The algorithm reads an allow list of IP addresses permitted to access a restricted subnetwork, then removes any IP addresses that appear on a remove list of employees who should no longer have access. This automated process helps maintain security compliance by ensuring only authorized personnel can access sensitive patient data. The algorithm efficiently opens, reads, modifies, and writes to the allow list file using core Python file handling and data manipulation techniques.

## Open the File That Contains the Allow List

```python
import_file = "allow_list.txt"
with open(import_file, "r") as file:
```

The `import_file` variable stores the filename as a string. The `with` statement is used to open the file and automatically close it after the indented block executes, even if an error occurs. The `open()` function takes the filename and the mode (`"r"` for read), and returns a file object assigned to the variable `file`.

## Read the File Contents

```python
    ip_addresses = file.read()
```

The `.read()` method converts the entire contents of the file into a string. This string, containing all IP addresses from the allow list, is stored in the variable `ip_addresses` so it can be processed further.

## Convert the String Into a List

```python
    ip_addresses = ip_addresses.split()
```

The `.split()` method converts the `ip_addresses` string into a list of individual IP address elements. By default, `.split()` separates the string at whitespace characters (spaces and newlines), which is ideal since each IP address in the file is on its own line or separated by spaces.

## Iterate Through the Remove List

```python
remove_list = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]  # example remove list

for element in remove_list:
```

The `for` loop iterates through each item in the `remove_list`. The loop variable `element` takes on the value of each IP address in the remove list one at a time, allowing the loop body to process each address individually.

## Remove IP Addresses That Are on the Remove List

```python
    if element in ip_addresses:
        ip_addresses.remove(element)
```

Inside the loop, a conditional statement checks whether the current `element` exists in the `ip_addresses` list. If it does, the `.remove()` method deletes the first occurrence of that IP address from the list. This approach works correctly because there are no duplicate IP addresses in the `ip_addresses` list, so each call to `.remove()` targets exactly the intended entry.

## Update the File With the Revised List of IP Addresses

```python
    ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

The `.join()` method concatenates the elements of the `ip_addresses` list into a single string, with each IP address placed on a new line (separated by `"\n"`). Then, a second `with` statement opens the same file in write mode (`"w"`), which overwrites the existing contents. The `.write()` method writes the updated string of IP addresses back to the file, completing the update.

## Summary

This algorithm automates the removal of unauthorized IP addresses from a restricted access file. It begins by opening and reading the allow list file into a string, then converts that string into a list for individual address manipulation. A `for` loop iterates through a separate remove list, and for each IP address found in the allow list, the `.remove()` method deletes it. After all removals are complete, the list is converted back into a newline-separated string using `.join()`. Finally, the file is opened in write mode and the updated contents are saved using `.write()`. This efficient workflow ensures the allow list remains current and secure, supporting the organization's access control requirements.
