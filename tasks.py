from invoke import task
from plumbum import local
from shutil import copyfile
from pathlib import *

import filecmp
import os
import json

# Global Variables
# ----------------------------------------------------------------------
THESIS_DIR = Path('./src/thesis/')

CONTENT_DIR = Path('content/')
LAYOUT_DIR = Path('layout/')
IMG_DIR = Path('img/')
TBL_DIR = Path('tbl/')
REF_DIR = Path('ref/')

BUILD_DIR = Path('./build/')
TARGET_DIR = Path("./target/")


# Plumbum cmds
# ----------------------------------------------------------------------
cat = local["cat"]
cp = local["cp"]
rm = local["rm"]

pandoc = local["pandoc"]
pdflatex = local["pdflatex"]
bibtex = local["bibtex"]


# Pandoc flags
# ----------------------------------------------------------------------
# constants
pd_from     = '--from=markdown'
pd_to       = '--to=latex'


# functions
def pd_template(template_path : Path) -> str:
    return '--template={}'.format(str(template_path))


def pd_title(title : str) -> str:
    return '--variable=chapter-title:{}'.format(title)


def pd_out(out_path : Path) -> str:
    return '--out={}'.format(str(out_path))


# Base Functions
# ----------------------------------------------------------------------
def get_file_delimeter(file_type = None):
    is_file_check = lambda f : (not f.name.startswith('.')) and f.is_file()

    if file_type:
        if isinstance(file_type, list):
            file_type = (x if x.startswith('.') else '.{}'.format(x) for x in file_type)

            return lambda f : (is_file_check(f) and
                               bool(sum(f.name.endswith(x) for x in file_type)))
        elif isinstance(file_type, str):
            return lambda f : (is_file_check(f) and
                               f.name.endswith((file_type if file_type.startswith('.') else
                                                '.{}'.format(file_type))))
        else:
            raise Exception()
    else:
        return is_file_check


def build_file_entry_list(root_path : str, delimeter):
    if Path(root_path).exists():
        file_entries = []
        file_dir = [root_path]
        while file_dir:
            for entry in os.scandir(file_dir.pop()):
                if not entry.name.startswith('.') and entry.is_dir():
                    file_dir.append(entry.path)
                elif delimeter(entry):
                    file_entries.append(entry)

        return file_entries
    else:
        return []


def update_directory(path_src: Path, path_target: Path, delimiter, verbose: bool):
    if verbose:
        print("  src:    " + str(path_src))
        print("  target: " + str(path_target))
        print("  Building file list src...", end='')

    src = build_file_entry_list(str(path_src), delimiter)
    src.sort(key=(lambda x: x.path[(len(str(path_src)) +1):]))


    if verbose:
        print("[DONE]")
        print("  Building file list target...", end='')

    target = build_file_entry_list(str(path_target), delimiter)
    target.sort(key=(lambda x: x.path[(len(str(path_target)) +1):]))

    if verbose:
        print("[DONE]")
        print("  Updating files:")

    while src and target:
        if src[0].name == target[0].name:
            if not filecmp.cmp(src[0].path, target[0].path):
                if verbose:
                    print("    Copying:  " + src[0].path)
                copyfile(src[0].path, target[0].path)
            else:
                if verbose:
                    print("    Skipping: " + src[0].path)

            src = src[1:]
            target = target[1:]
        else:
            if ( src[0].path[(len(str(path_src)) +1):] <
                 target[0].path[(len(str(path_target)) +1):]):
                entry_path = Path(src[0].path)
                goal_path = path_target / entry_path.relative_to(path_src)

                if verbose:
                    print("    Copying:  " + str(entry_path))

                if not (goal_path.parent.exists() and
                        goal_path.parent.is_dir()):
                    goal_path.parent.mkdir(parents=True)

                copyfile(str(entry_path), str(goal_path))
                src = src[1:]
            else:
                if verbose:
                    print("    Removing: " + target[0].path)
                rm(target[0].path)
                target = target[1:]

    for entry in src:
        entry_path = Path(entry.path)
        goal_path = path_target / entry_path.relative_to(path_src)
        print(str(goal_path))

        if not (goal_path.parent.exists() and goal_path.parent.is_dir()):
            goal_path.parent.mkdir(parents=True)
        if verbose:
            print("    Copying: " + str(entry_path))
        copyfile(str(entry_path), str(goal_path))

    for entry in target:
        if verbose:
            print("    Removing: " + entry.path)
        rm(entry.path)


def update_file(path_src: Path, path_target: Path):
    # Check if path source exists, if not raise error
    if not (path_src.exists() and
            path_src.is_file()):
        raise Exception()

    if not (path_target.parent.exists() and
            path_target.parent.is_dir()):
        path_target.parent.mkdir(parents=True)

    if not (path_target.exists() and
            filecmp.cmp(str(path_src), str(path_target))):
        copyfile(str(path_src), str(path_target))


# Specific functions
# ----------------------------------------------------------------------
def build_markdown_files(chapters, verbose=False):
    if verbose:
        print("Building markdown files:")

    build_dir = BUILD_DIR / Path('md/')

    content_src = THESIS_DIR / CONTENT_DIR

    if not (build_dir.exists() and
            build_dir.is_dir()):
        build_dir.mkdir(parents=True)

    # Build preface
    if verbose:
        print("  updating preface.md ...", end='')

    preface_src = content_src / Path("preface.md")
    preface_target = build_dir / Path("preface.md")

    update_file(preface_src, preface_target)

    if verbose:
        print("[DONE]")
        print("  updating abstract.md ...", end='')

    abstract_src = content_src / Path("abstract.md")
    abstract_target = build_dir / Path("abstract.md")
    update_file(abstract_src, abstract_target)

    if verbose:
        print("[DONE]")
        print("  build chapter files:")

    for chapter in chapters:
        print(chapter)
        if verbose:
            print("    building {}.md ...".format(chapter), end='')

        chapter_src = content_src / Path(chapter)

        with open(str(chapter_src / "chapter.json"), 'r') as f:
            sections = json.loads(f.read())

        section_paths = list(str(chapter_src / Path(s)) for s in sections["sections"])
        #chapter_md = cat(section_paths)

        with open(str(build_dir / Path('{}.md'.format(chapter))), 'w') as f:
            for sp in section_paths:
                with open(sp, 'r') as sp_f:
                    f.write(sp_f.read())

        if verbose:
            print("[DONE]")


def update_basefile(verbose=False, mode='print'):
    if verbose:
        print("Updating thesis_{}.tex ...".format(mode), end='')

    src = THESIS_DIR / LAYOUT_DIR / Path('thesis_{}.tex'.format(mode))
    target = BUILD_DIR / Path('thesis_{}.tex'.format(mode))

    update_file(src, target)

    if verbose:
        print("[DONE]")


def update_bib(verbose=False):
    src = THESIS_DIR / REF_DIR
    target = BUILD_DIR

    if verbose:
        print("Updating ref.bib ...", end='')

    update_file(src / Path('reference.bib'), target / Path('reference.bib'))

    if verbose:
        print("[DONE]")
        print("Updating acm.bst ...", end='')

    update_file(src / Path('acm.bst'), target / Path('acm.bst'))

    if verbose:
        print("[DONE]")


def update_templates(verbose=False):
    layout_src = THESIS_DIR / LAYOUT_DIR
    build_dir = BUILD_DIR / LAYOUT_DIR

    update_directory(path_src=layout_src,
                     path_target=build_dir,
                     delimiter=get_file_delimeter(file_type=".tex"),
                     verbose=verbose)


def compile_markdown(chapters, verbose=False):
    if verbose:
        print("Compiling markdown files to LaTeX:")

    path_src = BUILD_DIR / Path('md')
    path_template = BUILD_DIR / LAYOUT_DIR
    path_target = BUILD_DIR / CONTENT_DIR

    # check if tex folder exists
    if not (path_target.exists() and
            path_target.is_dir()):
        path_target.mkdir(parents=True)

    # compile preface
    if verbose:
        print("  Compiling preface.md ...", end='')
    preface_content = path_src / Path('preface.md')
    preface_template = path_template / Path('preface_template.tex')

    pandoc(pd_from,
           pd_to,
           pd_template(preface_template),
           pd_out(path_target / Path('preface.tex')),
           str(preface_content))

    if verbose:
        print("[DONE]")

    # compile abstract
    if verbose:
        print("  Compiling abstract.md ...", end='')

    abstract_content = path_src / Path('abstract.md')
    abstract_template = path_template / Path('abstract_template.tex')

    pandoc(pd_from,
           pd_to,
           pd_template(abstract_template),
           pd_out(path_target / Path('abstract.tex')),
           str(abstract_content))

    if verbose:
        print("[DONE]")

    # compile chapters
    chapter_template = path_template / Path('chapter_template.tex')

    for chapter in chapters:
        if verbose:
            print("    Compiling {}.md ...".format(chapter), end='')

        pandoc( pd_from,
                pd_to,
                pd_template(chapter_template),
                pd_title(chapter.capitalize()),
                pd_out(path_target / Path('{}.tex'.format(chapter))),
                str((path_src / Path('{}.md'.format(chapter))))
        )

        if verbose:
            print("[DONE]")


def update_images(verbose=False):
    build_dir = BUILD_DIR / IMG_DIR
    img_src = THESIS_DIR / IMG_DIR

    # update tex files
    update_directory(path_src=(img_src / Path("tex")),
                     path_target=(build_dir / Path("tex")),
                     delimiter=get_file_delimeter(file_type=".tex"),
                     verbose=verbose)

    # update raw images
    update_directory(path_src=(img_src / Path("raw/")),
                     path_target=(build_dir / Path("raw/")),
                     delimiter=get_file_delimeter(file_type=None),
                     verbose=verbose)


def update_tables(verbose=False):
    build_dir = BUILD_DIR / TBL_DIR
    tbl_src = THESIS_DIR / TBL_DIR

    update_directory(path_src=tbl_src,
                     path_target=build_dir,
                     delimiter=get_file_delimeter(file_type=None),
                     verbose=verbose)


def compile_tex(verbose=False, mode='print'):
    if verbose:
        print("  Compiling latex: ")
    old_path = Path.cwd()
    os.chdir(str(BUILD_DIR))

    if verbose:
        print("    Compilation 0 ... ", end='')
    output = pdflatex("thesis_{}.tex".format(mode))
    print(output)

    if verbose:
        print("  Compiling bibtex: ")
        print("    Compiling reference.bib ... ", end='')

    output = bibtex("thesis_{}.aux".format(mode))
    print(output)

    if verbose:
        print("  Compiling latex: ")
        print("    Compilation 1 ... ", end='')
    output = pdflatex("thesis_{}.tex".format(mode))

    if verbose:
        print("[DONE]")
        print("    Compilation 2 ... ", end='')

    output = pdflatex("thesis_{}.tex".format(mode))

    if verbose:
        print("[DONE]")

    os.chdir(str(old_path))


def copy_output(verbose=False, mode='print'):
    if verbose:
        print("  Copying result ...", end='')

    output_file = Path('thesis_{}.pdf'.format(mode))
    update_file(BUILD_DIR / output_file,
                TARGET_DIR / output_file)

    if verbose:
        print("[DONE]")

# Invoke Tasks
# ----------------------------------------------------------------------
@task
def build(ctx, verbose=False):
    content_src = THESIS_DIR / CONTENT_DIR
    with open(str(content_src / Path('conf.json')), 'r') as f:
        data = json.loads(f.read())

    # execute commands to build
    build_markdown_files(chapters=data["chapters"], verbose=verbose)
    update_templates(verbose=verbose)
    update_basefile(verbose=verbose)
    update_bib(verbose=verbose)
    compile_markdown(chapters=data["chapters"], verbose=verbose)
    update_images(verbose=verbose)
    update_tables(verbose=verbose)
    compile_tex(verbose=verbose)
    copy_output(verbose=verbose)

