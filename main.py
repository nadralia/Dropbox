import dropbox
import config
import helper


def display():
    print("1) Check if directory exists")
    print("2) Create Directory")
    print("3) View contents in the directory")
    print("4) upload file")
    print("5) move file")
    print("0) Exit")


def main(dbx):
    while 1:
        display()
        command = 0
        try:
            command = int(input())
        except ValueError:
            print('Not a number!')
            exit(0)
        print()
        if command == 1:
            check = helper.check_path(config.SOURCE_DIR, dbx)
            if check:
                print('Directory exists')
            else:
                print("Directory doesn't exists, make sure to create it")
        elif command == 2:
            helper.make_directory(config.SOURCE_DIR, dbx)
        elif command == 3:
            source_files = helper.view_all_directory_contents(config.SOURCE_DIR, dbx)
            print(source_files)
        elif command == 4:
            source_files = helper.upload_file(config.SOURCE_DIR, dbx)
            print(helper.view_all_directory_contents(config.SOURCE_DIR, dbx))
        elif command == 5:
            source_files = helper.move_dropbox_file(config.SOURCE_DIR, dbx)
            print(source_files)
        elif command == 0:
            print('\nBye!')
            exit(0)

if __name__ == '__main__':
    with dropbox.Dropbox(config.TOKEN) as dbx:
        main(dbx)