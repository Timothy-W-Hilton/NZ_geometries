import nox

# These lines make conda the default for ALL sessions
nox.options.sessions = ["tests"]
nox.options.default_venv_backend = "conda"

@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"])  # Will use conda because of default above
def tests(session):
    session.install("pytest")
    session.install("-e", ".")
    session.run("pytest")
