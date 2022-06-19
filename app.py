from flask import Flask, render_template, request, url_for
import pyvista
import os
static_image_path = os.path.join('static')
template_path = os.path.join('templates')

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        meshtype = request.form['meshtype']
        if meshtype == 'Sphere':
            mesh = pyvista.Sphere()
        elif meshtype == 'Cube':
            mesh = pyvista.Cube()
        elif meshtype == 'Bohemian Dome':
            mesh = pyvista.ParametricBohemianDome()
        elif meshtype == 'Cylinder':
            mesh = pyvista.Cylinder()
        else:
            # invalid entry
            raise ValueError('Invalid Option')

        # generate screenshot
        filename = f'{meshtype}.png'
        filepath = os.path.join(static_image_path, filename)
        plotter = pyvista.Plotter(off_screen=True)
        actor = plotter.add_mesh(mesh)
        plotter.screenshot(filepath)
        return render_template('index.html', img_src=filepath)


@app.route('/submit3d', methods=['POST'])
def submit3d():
    if request.method == "POST":
        meshtype = request.form['meshtype']
        if meshtype == 'Sphere':
            mesh = pyvista.Sphere()
        elif meshtype == 'Cube':
            mesh = pyvista.Cube()
        elif meshtype == 'Bohemian Dome':
            mesh = pyvista.ParametricBohemianDome()
        elif meshtype == 'Cylinder':
            mesh = pyvista.Cylinder()
        else:
            # invalid entry
            raise ValueError('Invalid Option')
        filename = meshtype + '.html'
        filepath = os.path.join(static_image_path, filename)

        # create a plotter and add the mesh to it
        pl = pyvista.Plotter(window_size=(600, 600))
        pl.add_mesh(mesh)
        pl.background_color = 'white'
        pl.export_html(filepath)
        return render_template('index.html', img_src=filepath)


@app.route('/<meshtype>', methods=['GET', 'POST'])
def getimage(meshtype):
    if meshtype == 'Sphere':
        mesh = pyvista.Sphere()
    elif meshtype == 'Cube':
        mesh = pyvista.Cube()
    elif meshtype == 'Bohemian Dome':
        mesh = pyvista.ParametricBohemianDome()
    elif meshtype == 'Cylinder':
        mesh = pyvista.Cylinder()
    else:
        # invalid entry
        raise ValueError('Invalid Option')
    filename = meshtype + '.html'
    filepath = os.path.join(static_image_path, filename)

    # create a plotter and add the mesh to it
    pl = pyvista.Plotter(window_size=(600, 600))
    pl.add_mesh(mesh)
    pl.background_color = 'white'
    pl.export_html(filepath)
    return filepath


if __name__ == '__main__':
    app.run(debug=True)
