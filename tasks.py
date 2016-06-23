from invoke import task
from plumbum import local

from pathlib import *
import importlib.util

import os


# Global Variables
# ----------------------------------------------------------------------
THESIS_DIR = Path('./src/thesis/')

CONTENT_DIR = Path('content/')
LAYOUT_DIR = Path('layout/')

BUILD_DIR = Path('./build/')


# Plumbum cmds
# ----------------------------------------------------------------------
cat = local["cat"]
cp = local["cp"]
rm = local["rm"]

pandoc = local["pandoc"]


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


# Functions
# ----------------------------------------------------------------------
def _clean():
    # TODO
    pass

# Build Utility Functions
# ----------------------------------------------------------------------
def copy_base_file(mode='print'):
    cp(Path(THESIS_DIR, LAYOUT_DIR, 'thesis_{}.tex'.format(mode)),
       Path(BUILD_DIR),
       '-u')

def inspect_build_structure():
    # Check if build directory exists
    if not BUILD_DIR.exists():
        BUILD_DIR.mkdir()
    elif BUILD_DIR.is_file():
        # TODO
        raise Exception()

    # Check if content directory exists
    content_path = Path(BUILD_DIR, CONTENT_DIR)
    if not content_path.exists():
        content_path.mkdir()
    elif content_path.is_file():
        # TODO
        raise Exception()


def compile_markdown():
    build_dir = Path(BUILD_DIR, CONTENT_DIR)

    content_src = Path(THESIS_DIR, CONTENT_DIR)
    layout_src = Path(THESIS_DIR, LAYOUT_DIR)

    # build preface
    preface_content = Path(content_src, Path('preface.md')) #TODO
    preface_template = Path(layout_src, Path('preface_template.tex'))

    pandoc(pd_from,
           pd_to,
           pd_template(preface_template),
           pd_out(Path(build_dir, Path('preface.tex'))),
           str(preface_content))

    # build abstract
    abstract_content = Path(content_src, Path('abstract.md')) #TODO: remove hardcodedness?
    abstract_template = Path(layout_src, Path('abstract_template.tex'))

    pandoc(pd_from,
           pd_to,
           pd_template(abstract_template),
           pd_out(Path(build_dir, Path('abstract.tex'))),
           str(abstract_content))

    # load chapter conf_file
    spec = importlib.util.spec_from_file_location('', str(Path(THESIS_DIR,
                                                               CONTENT_DIR,
                                                               'conf.py')))
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)

    # template
    chapter_template = Path(layout_src, Path('chapter_template.tex'))

    # TODO: add proper testing
    # build chapters
    for chapter in c.chapters:
        chapter_path = Path(THESIS_DIR, CONTENT_DIR, chapter)

        # load conf file of a chapter
        chapter_spec = importlib.util.spec_from_file_location(
            '',
            str( Path(chapter_path, 'chapter.py')))
        chapter_conf = importlib.util.module_from_spec(chapter_spec)
        chapter_spec.loader.exec_module(chapter_conf)

        section_paths = list(Path(chapter_path, section) for section in chapter_conf.sections)
        # execute pandoc
        pandoc_chain = ( cat[section_paths] |
                         pandoc[ pd_from,
                                 pd_to,
                                 pd_template(chapter_template),
                                 pd_title(chapter_conf.title),
                                 pd_out(Path(build_dir, '{}.tex'.format(chapter)))
                         ])
        pandoc_chain()


def compile_tex():
    #TODO
    pass


# Tasks
# ----------------------------------------------------------------------
@task
def clean(ctx):
    _clean()


@task
def build(ctx, clean=False):
    if clean:
        _clean()
    inspect_build_structure()
    compile_markdown()
    copy_base_file()


