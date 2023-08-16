import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session: nox.Session) -> None:
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("black")
    session.install("ruff")
    session.install("mypy")
    session.run("black", "--check", ".")
    session.run("ruff", "check", ".")
    session.run("mypy", ".")


@nox.session
def format(session: nox.Session) -> None:
    session.install("black")
    session.install("ruff")
    session.run("black", ".")
    session.run("ruff", "--fix", ".")
