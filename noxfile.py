import nox

# These lines make conda the default for ALL sessions
nox.options.sessions = ["tests"]
nox.options.default_venv_backend = "conda"

@nox.session(python=["3.9", "3.10"])  # Will use conda because of default above
def tests(session):
    session.install("pytest")
    session.install("-e", ".")
    session.run("pytest")
