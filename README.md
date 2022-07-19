# python-coding-task

This project will generate a new CSV file, called masked_clients.csv, with the values of the csv file customers.csv masked.The fields "ID,Name,Email,Billing,Location" are masked. All numeric values are replaces with the average "Billing" of each cell. And all "Email" and "Name" cells are masked with the value "X" (Except for characters @', ',' or '.'). Finally, the maximum, minimum and average of "Name" and "Billing" field will be displayed.

To run the file

```console
python3 challenge.py
```

To run the test file

```console
python3 -m unittest -v test_challenge
```
