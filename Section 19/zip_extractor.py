import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:\\Users\\Jorda\\PycharmProjects\\Lessons\\Section 19\\compressed.zip",
                    "C:\\Users\\Jorda\\PycharmProjects\\Lessons\\dir_for_testing")
