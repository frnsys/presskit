import os
import yaml
import click
import shutil
from jinja2 import FileSystemLoader, environment

dir = os.path.dirname(os.path.abspath(__file__))
templ_dir = os.path.join(dir, 'assets')
env = environment.Environment()
env.loader = FileSystemLoader(templ_dir)

@click.command()
@click.argument('config', type=click.Path(dir_okay=False, exists=True))
@click.argument('assets', type=click.Path(file_okay=False, exists=True))
@click.argument('outdir', type=click.Path(file_okay=False, writable=True))
@click.option('-s', '--styles',
    type=click.Path(dir_okay=False, exists=True),
    help='Optional styles file to use.')
@click.option('-c', '--copy-assets',
    is_flag=True,
    default=False,
    help='Copy assets instead of symlinking.')
def main(config, assets, outdir, styles, copy_assets):
    conf = yaml.safe_load(open(config, 'r'))
    assert os.path.isdir(assets)

    if styles is None:
        styles = os.path.join(templ_dir, 'style.css')
    styles = open(styles, 'r').read()

    site_title = f'{conf["title"]} : Press Kit'
    templ = env.get_template('template.html')
    html = templ.render(**conf,
            style=styles,
            site_title=site_title)

    prep_build_dir(outdir)
    with open(os.path.join(outdir, 'index.html'), 'w') as f:
        f.write(html)

    assets_dir = os.path.join(outdir, assets)
    if copy_assets:
        shutil.copytree(assets, assets_dir)
    else:
        frm = os.path.abspath(assets)
        to = os.path.abspath(assets_dir)
        os.symlink(frm, to)

def prep_build_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    for f in os.listdir(path):
        fpath = os.path.join(path, f)
        if os.path.isfile(fpath) or os.path.islink(fpath):
            os.remove(fpath)
        elif os.path.isdir(fpath):
            shutil.rmtree(fpath)

if __name__ == '__main__':
    main()