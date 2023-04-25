import os
import sys

FOLDER_STRUCTURE = {
    'assets': {
        'audio': {
            'music': None,
            'sound_effects': None
        },
        'images': None,
        'video_footage': None,
        'thumbnails': None,
        'captions': None
    },
    'project_files': None,
    'graphics': {
        'logos': None,
        'lower_thirds': None,
        'titles': None
    },
    'other': None
}


def create_folder_structure(path, folder_structure):
    for folder_name, subfolders in folder_structure.items():
        folder_path = os.path.join(path, folder_name.lower().replace(' ', '_'))
        os.makedirs(folder_path, exist_ok=True)
        print(f'Created folder: {folder_path}')

        if subfolders is not None:
            create_folder_structure(folder_path, subfolders)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify the path where the folder structure should be created.')
        print(f'Example usage: python {__file__} /path/to/folder')
        sys.exit(1)

    path = sys.argv[1]
    create_folder_structure(path, FOLDER_STRUCTURE)
