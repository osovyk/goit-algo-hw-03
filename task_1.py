import os
import shutil
import sys


def copy_files_recursively(source_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                new_dest_dir = os.path.join(dest_dir, item)
                os.makedirs(new_dest_dir, exist_ok=True)
                copy_files_recursively(source_path, new_dest_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:]
                if file_extension:
                    dest_path = os.path.join(dest_dir, file_extension)
                    os.makedirs(dest_path, exist_ok=True)
                    shutil.copy2(source_path, dest_path)
    except Exception as e:
        print(f"Помилка при обробці файлу або директорії: {e}")


def main():
    if len(sys.argv) not in [2, 3]:
        print("Використання: python task_1.py <вихідна директорія> <директорія призначення>")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) == 3 else "dist"

    if not os.path.exists(source_dir):
        print(f"Вихідна директорія {source_dir} не існує.")
        return

    copy_files_recursively(source_dir, dest_dir)

    print(f"Файли успішно скопійовані та відсортовані у директорії {dest_dir}.")


if __name__ == "__main__":
    main()