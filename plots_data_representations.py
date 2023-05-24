import webbrowser
from tempfile import NamedTemporaryFile
# from IPython.display import HTML, display

def df_to_html(df, description):
    html = df.style.set_table_attributes('style="font-size: 12px"').to_html()
    html = f"<h2>{description}</h2>" + html
    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        f.write(html.encode())
        filepath = f.name
    webbrowser.open('file://' + filepath)