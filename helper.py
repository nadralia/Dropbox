import dropbox
import re
import logging


def check_path(path, dbx):
    """Checks if a given dropbox path exists."""
    try:
        return dbx.files_get_metadata(path) is not None
    except dropbox.exceptions.ApiError as e:
        error_object = e.error
        if isinstance(error_object, dropbox.files.GetMetadataError) and error_object.is_path():
            base_error = error_object.get_path()
            if isinstance(base_error, dropbox.files.LookupError) and base_error.is_not_found():
                return False
            else:
                raise base_error
        else:
            raise error_object


def make_directory(path, dbx):
    """Creates a directory at the path. Expects that this does not point to a file."""
    if re.search(r"\.[^.]*$", path) is not None:
        raise ValueError("The path needs to be a directory path and not a file path. "
                         "{path} appears to be a file path.")
    _ = dbx.files_create_folder(path)
    print(f"Created directory at path: \"{path}\"")


def view_all_directory_contents(directory, dbx):
    """Calls dropbox to retrieve contents of a directory."""
    content_to_return = []
    try:
        folder_contents = dbx.files_list_folder(directory)
    except dropbox.exceptions.ApiError as e:
        error_object = e.error
        if isinstance(error_object, dropbox.files.ListFolderError):
            base_error = error_object.get_path()
            if isinstance(base_error, dropbox.files.LookupError) and base_error.is_not_found():
                raise Exception(f"Dropbox cannot locate the object at path \"{directory}\".")
            else:
                raise base_error
        else:
            raise error_object

    directory_contents = folder_contents.entries
    while folder_contents.has_more:
        cursor = folder_contents.cursor
        folder_contents = dropbox.dropbox.Dropbox.files_list_folder_continue(cursor)
        directory_contents += folder_contents.entries

    for fobj in directory_contents:
        if isinstance(fobj, dropbox.files.FileMetadata):
            content_to_return.append(fobj.name)
        else:
            logging.warn(f"The object type for \"{fobj.name}\" is not currently supported. "
                         "The object was not moved to a destination directory.")

    return content_to_return


def upload_file(directory, dbx):
    """upload a file to Dropbox using API v2"""
    print('Enter file name with the file extention like: test.pdf')
    print('make sure the file is in the root directory of this code')
    source_path = str(input())

    destination_path = directory + "/"+ source_path

    with open(source_path, 'rb') as f:
        dbx.files_upload(f.read(), destination_path)

def move_dropbox_file(source_path, dbx):
    """Moves a file from the source path to the destination path."""
    print('Enter file name with the file extention like: test.pdf')
    print('make sure the file is in the root directory of this code')
    dest = str(input())

    destination_path = "/"+ dest + "/"

    print(destination_path)

    dbx.files_move(source_path, destination_path)
    return dbx.files_get_metadata(destination_path).name