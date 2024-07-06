from glob import glob

workers = 1
loglevel = 'info'
reload = True
reload_extra_files = sum(
    [
        glob('src/webapp/static/**/*.' + ext, recursive=True)
        for ext in ['html', 'css', 'js']
    ],
    []
)
errorlog = '-'
accesslog = '-'
