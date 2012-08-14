#!/usr/bin/python

import distutils.core
import glob
import os
import sys

"""
Author: Zach Rohde (zach@zachrohde.com)

For more information go to: http://zachrohde.com
"""

ACTIONS = {
    0 : 'copy',
    1 : 'move',
}
COPY = 0
MOVE = 1

def get_include_subdirs():
    """Asks user whether they wish to include subdirectories or not."""
    question = '\n%s\n\t%s\n' % (
        "Do you wish to include subdirectories?",
        "Please enter: [Yes / No]",
    )
    
    while True:
        sys.stdout.write(question)
        anwser = raw_input().lower()
        
        if anwser == "yes":
            return True
        elif anwser == "no":
            return False
        else:
            sys.stdout.write("\nPlease try again.\n")

def get_action():
    """Asks user whether they wish to copy or move the files/directory(s)."""
    question = '\n%s\n\t%s\n' % (
        "Do you wish to copy or move the file(s)/directory(s)?",
        "Please enter: [Copy / Move]",
    )
    valid_responses = {
        "copy" : COPY,
        "move" : MOVE,
    }
    True
    
    while True:
        sys.stdout.write(question)
        anwser = raw_input().lower()
        
        if anwser in valid_responses:
            return valid_responses[anwser]
        else:
            sys.stdout.write("\nPlease try again.\n")
            
def get_source_paths():
    """Asks user for source path(s)"""
    question = '\n%s\n\t%s\n' % (
        "Enter the full source path of the directories or files.",
        "Note: if you are adding multiple directories or files, seperate them by comma.",
    )
    
    sys.stdout.write(question)
    answer = raw_input()
    unclean_paths = answer.split(',')
    paths = map(lambda x: x.strip(), unclean_paths)
    
    return paths
    
def get_dest_path():
    """Asks user for destination path(s)"""
    question = '\n%s\n' % (
        "Enter the full destination path of the directories or files.",
    )
    
    while True:
        sys.stdout.write(question)
        path = raw_input()
        
        if (os.path.exists(path) and os.path.isdir(path)) or not os.path.exists(path):
            return path
        else:
            sys.stdout.write("\nDesgination path must be a directory or non-existing path.\n")

def copy_files(source_paths, dest_path):
    """Copies files from source path (no subdirectories) into the destination path"""
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    for path in source_paths:
        if os.path.isfile(path):
            distutils.file_util.copy_file(path, dest_path)
        else: #os.path.isdir(path)
            files = glob.iglob(os.path.join(path, "*"))
            for file in files:
                if os.path.isfile(file):
                    distutils.file_util.copy_file(file, dest_path)

def copy_files_recursive(source_paths, dest_path):
    """Recursively copies files from source path (with subdirectories) into the destination path"""
    for path in source_paths:
        distutils.dir_util.copy_tree(path, dest_path)

def move_files(source_paths, dest_path):
    """Moves file(s) from source path (no subdirectories) into the destination path"""
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    for path in source_paths:
        if os.path.isfile(path):
            distutils.file_util.move_file(path, dest_path)
        else: #os.path.isdir(path)
            files = glob.iglob(os.path.join(path, "*"))
            for file in files:
                if os.path.isfile(file):
                    distutils.file_util.move_file(file, dest_path)

def move_files_recursive(source_paths, dest_path):
    """Recursively moves files from source path (with subdirectories) into the destination path"""
    for path in source_paths:
        distutils.dir_util.create_tree(dest_path, path)
        distutils.dir_util.copy_tree(path, dest_path)
        distutils.dir_util.remove_tree(path, dest_path)

def main():
    """This is the main function that is run on command-line execution."""
    
    # Check to see if they wish to include subdirectories
    include_subdirs = get_include_subdirs()
    
    # Ask user whether they wish to copy or move
    action = get_action()
    
    sys.stdout.write("\nNOTICE: You have chosen to %s the source file(s)/directory(s).\n" % (
        ACTIONS[action],
    ))
    
    # Prompt user to enter the source of the directories or files
    source_paths = get_source_paths()    
    
    sys.stdout.write("\nNOTICE: You selected source path(s): %s.\n" % (
        ', '.join(source_paths),
    ))
    
    # Prompt user to enter the destination of the directories or files
    dest_path = get_dest_path()
    
    sys.stdout.write("\nNOTICE: You entered the destination path: %s.\n" % (
        dest_path,
    ))
    
    if action == COPY:
        # Copy directories without subdirectories
        if include_subdirs == False:
            copy_files(source_paths, dest_path)
            
            sys.stdout.write("\nThe files within %s have been successfully copied into %s.\n" % (
                ', '.join(source_paths),
                dest_path,
            ))
        # Copy directories with subdirectories
        else: #include_subdirs == True
            copy_files_recursive(source_paths, dest_path)
            
            sys.stdout.write("\nThe files and subdirectories within %s have been successfully copied into %s.\n" % (
                ', '.join(source_paths),
                dest_path,
            ))
    else: #action == MOVE:
        # Move directories without subdirectories
        if include_subdirs == False:
            move_files(source_paths, dest_path)
            
            sys.stdout.write("\nThe files within %s have been successfully moved into %s.\n" % (
                ', '.join(source_paths),
                dest_path,
            ))
        # Move directories with subdirectories
        else: #include_subdirs == True
            move_files_recursive(source_paths, dest_path)
            
            sys.stdout.write("\nThe files and subdirectories within %s have been successfully moved into %s.\n" % (
                ', '.join(source_paths),
                dest_path,
            ))

if __name__ == '__main__':
    main()