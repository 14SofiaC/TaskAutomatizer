FILE_TYPE = { 
    'Images': ['.jpg', '.jpeg', '.png', '.gif', 'webp', '.tiff', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg'],
}

# This dictionary categorizes different file types based on their extensions. Each key represents a category (e.g., 'Images', 'Videos', 'Documents'), and the corresponding value is a list of file extensions associated with that category. This structure allows for easy classification of files based on their extensions when used in conjunction with the 'classify_file' function from 'functions.py'.