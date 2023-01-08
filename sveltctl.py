import click
import pytailwindcss
import importlib
import sys
import trpc
sys.path.append('node_modules')

sveltekit = importlib.import_module('svelte')


@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("helllloooo")


@cli.command()
@click.argument("config")
@click.argument("output_file")
@click.option("--style",help="Additional styles to be included in the css file")
def tailbuild(config,output_file,style):
    with open(config, 'r') as f:
        config = f.read()
    css = pytailwindcss.build(config,style=style)
    with open(output_file, 'w') as f:
        f.write(css)


@cli.command()
@click.argument('input_file')
@click.argument('output_file')
def render(input_file, output_file): #for rendering a sveltefile and then producing the output to a output file
    with open(input_file, 'r') as f:
        component = f.read()
    output = sveltekit.render(component)
    with open(output_file, 'w') as f:
        f.write(output)

@cli.command()
@click.argument('appdir')
def run_dev(appdir): #for starting a development server with hot reloading enabled
    sveltekit.dev({
        'rootDir': appdir,
        'hotReloading': True,
    })


@cli.command()
@click.option('--app-path', required=True, type=click.Path(exists=True),help="Enter the app path")
@click.option('--output-dir', required=True, type=click.Path(),help="enter the output dir that you want to store the output in")
def build(app_path,output_path):# for building the application for production 
    sveltekit.build(app_path, {
        'output': output_path,
        'minify': True
    })

@cli.command()
@click.option("--app-path")
def format(app_path):
    sveltekit.__format__(app_path)
    


if __name__ =="__main__":
    cli()
