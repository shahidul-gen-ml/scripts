# YOLO Training Data cleaning process after annotation

- Copy the complete list of classes that we are utilizing in the `darknet.yml` file and paste it into the **class name** variable found in the `data_allign.py` file.
- RUN the command in terminal

    ```console
    python test.py -f Test/fold_1
    ```

### For Help

```console
usage: txt_change.py [-h] [-f FOLDER_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER_PATH, --folder_path FOLDER_PATH
                        Folder path to change class id
```

#### Example Folder Structure

```console
Test
├── fold_1
│   ├── 0
│   │   ├── 045.txt
        |── 045.png

Traning
├── fold_1
│   ├── 0
│   │   ├── asdasd.txt
        |── asdasd.png

Validation
├── fold_1
│   ├── 0
│   │   ├── lol.txt
        |── lol.png
```
