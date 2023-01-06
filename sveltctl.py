import click
import node

node.run_npm_install(['tailwindcss'])
tailwindcss = node.require('tailwindcss')
node.run_npm_install(['sveltekit'])
sveltekit = node.require('sveltekit')


@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("helllloooo")

@cli.command()
@cli.argument("config")
@cli.argument("output_file")
def tailbuild(config,output_file):
    with open(config, 'r') as f:
        config = f.read()
    css = tailwindcss.build(config)
    with open(output_file, 'w') as f:
        f.write(css)


@cli.command()
@click.argument('input_file')
@click.argument('output_file')
def render(input_file, output_file):
    with open(input_file, 'r') as f:
        component = f.read()
    output = sveltekit.render(component)
    with open(output_file, 'w') as f:
        f.write(output)

if __name__ =="__main__":
    cli()