"""Several tools to deal with QC calculations."""

import os.path.isfile

def find(code_or_file, path_to_start_the_search='.', recursivity=True ):
    """This function find the path of all folders with calculations.
    In fact, if code_or_file is a code it select folder with the code output
    file, if code_or_file is not a code (so it is a filename), it select folders
    with a file named equal to code_or_file.

    code_or_file: str with the code name (VASP of fhi) or a file name.
    path_to_start_the_search: str with the path to the folder to start the seach
                              for folders with calculations.
    recursivity: if True the search is completely recursive, if False, the seach
                 run over the forder within the folder path_to_start_the_search.

    Example:
    >>> list_with_calculations_path = find('VASP', '.')
    """

    logging.info("Initializing find_calculation function...")

    # Variables unit tests
    logging.info('code_or_file: ' + str(code_or_file) )
    if code_or_file != str :
        logging.error("code_or_file must be a string! Aborting...")
        sys.exit(1)

    logging.info('path_to_start_the_search: ' + str(path_to_start_the_search) )
    if path_to_start_the_search != str :
        logging.error("path_to_start_the_search must be a string! Aborting...")
        sys.exit(1)

    logging.info('recursivity: ' + str(recursivity))
    if recursivity != bool :
        logging.error("recursivity must be an bool! Aborting...")
        sys.exit(1)

    # Other verification tests
    if os.path.isdir(path_to_start_the_search) == False :
        logging.error("The path_to_start_the_search is not a directory!
                       Aborting...")
        sys.exit(1)
    else:
        logging.debug('path_to_start_the_search is a directory!')

    # Geting the output_file_name from the code input var
    if code_or_file == 'VASP': output_file_name = 'OUTCAR'
    if code_or_file == 'fhi': output_file_name = 'aims.out'
    if code_or_file not in ['VASP', 'fhi'] :
        logging.debug('code_or_file variable is not an avaliable code.')
        logging.debug('code_or_file will be considered as the output file name.')
        output_file_name = code_or_file
    logging.debug('The output_file_name variable were selected to '
                   + output_file_name + '.' )

    # Find the list with paths
    if recursivity == True:
        list_of_folders = [ x[0] for x in
                            os.walk(path_to_start_the_search + '/') ]
    if recursivity == False:
        list_of_folders = [ x for x in os.listdir(path_to_start_the_search +'/')
                             if os.path.isdir(path_to_start_the_search + '/' + x) ]
    logging.debug('list_of_folders were find, it present len of'
                  + str(len(list_of_folders)) + '.')

    # Test
    if len(list_of_folders) == 0 :
        logging.error('No one folder were found! Aborting...')
        sys.exit(1)

    # Finding the folders with calculations
    list_with_all_calculations_folder = []
    for folder in list_of_folders :
        if os.path.isfile( folder + '/' + output_file_name ) :
            list_with_all_calculations_folder.append(folder)

    # Test
    if len(list_with_all_calculations_folder) == 0 :
        logging.warning('No one folder were found with calculations!')
    else:
        # Printing folders with calculations
        logging.debug('The following folders present calculation:')
        for folder in list_with_all_calculations_folder :
            logging.debug( '    ' + folder )

    logging.debug('The function finished sucsessfuly!')

    return list_with_all_calculations_folder # It must be the full name of the path, without abbreviations!


def cp_folders(list_with_all_calculations_folder, final_folder) :
    """This function copy the each folder in the
    list_with_all_calculations_folder to the final_folder.

    Arguments:
    list_with_all_calculations_folder: list of stings with the path to the
                                       folders.
    final_folder: path to the final folder. If it does not exist, it will be
                  created

    Example:
    >>> cp_folders(list_of_calculations_folders, './all_calculations')
    """
